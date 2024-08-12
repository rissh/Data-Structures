import json
import logging
from collections import namedtuple

import boto3
import pytest
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from google.cloud import compute_v1
from google.oauth2 import service_account
from iqe.utils import get_plugin_from_item_or_node
from wait_for import wait_for


@pytest.fixture()
def get_current_plugin(request, application):
    plugin_name = get_plugin_from_item_or_node(request.node)
    return getattr(application, plugin_name)


@pytest.fixture()
def cloud_creds(get_current_plugin, application):
    """Get Cloud creds
    :return: Credentials as an object
    """
    AWS = namedtuple("AWS", ["arn_role", "access_key", "secret_access_key"])
    AWS = AWS(
        get_current_plugin.config.default_cloud_settings.aws.arn_role,
        get_current_plugin.config.default_cloud_settings.aws.access_key_id,
        get_current_plugin.config.default_cloud_settings.aws.secret_access_key,
    )

    AZURE = namedtuple(
        "Azure", ["subscription_id", "client_id", "client_secret", "tenant_id", "resource_group"]
    )
    AZURE = AZURE(
        get_current_plugin.config.default_cloud_settings.azure.subscription_id,
        get_current_plugin.config.default_cloud_settings.azure.client_id,
        get_current_plugin.config.default_cloud_settings.azure.client_secret,
        get_current_plugin.config.default_cloud_settings.azure.tenant_id,
        get_current_plugin.config.default_cloud_settings.azure.resource_group,
    )

    GCP = namedtuple("GCP", ["project_id", "service_account_json"])
    GCP = GCP(
        get_current_plugin.config.default_cloud_settings.gcp.project_id,
        json.loads(get_current_plugin.config.default_cloud_settings.gcp.service_account_json),
    )

    Creds = namedtuple("Creds", ["AWS", "AZURE", "GCP"])

    return Creds(AWS, AZURE, GCP)


@pytest.fixture()
def terminate_instance(application):
    """Terminate instance after verifying it's status.
    :return: None. VM gets terminated.
    """

    def _terminate(
        cloud_creds,
        instance_ids,
        **kwargs,
    ):
        if not kwargs.get("hyperscaler"):
            pytest.fail("Hyperscaler missing")

        # AWS clean up
        if kwargs.get("hyperscaler") == "aws":
            ec2_client = boto3.client(
                service_name="ec2",
                region_name=kwargs.get("region"),
                aws_access_key_id=cloud_creds.AWS.access_key,
                aws_secret_access_key=cloud_creds.AWS.secret_access_key,
            )

            for instance in instance_ids:
                wait_for(
                    lambda: ec2_client.describe_instances(InstanceIds=[instance])["Reservations"][
                        0
                    ]["Instances"][0]["State"].get("Name")
                    in ["running", "stopped"],
                    delay=5,
                    num_sec=240,
                )
            ec2_client.terminate_instances(InstanceIds=instance_ids)

        # Azure clean up
        if kwargs.get("hyperscaler") == "azure":
            azure_logger = logging.getLogger("azure.core.pipeline")
            azure_logger.setLevel(logging.WARNING)
            credential = ClientSecretCredential(
                tenant_id=cloud_creds.AZURE.tenant_id,
                client_id=cloud_creds.AZURE.client_id,
                client_secret=cloud_creds.AZURE.client_secret,
            )
            subscription_id = cloud_creds.AZURE.subscription_id
            resource_group = kwargs.get("resource_group") or cloud_creds.AZURE.resource_group

            compute_client = ComputeManagementClient(credential, subscription_id)
            network_client = NetworkManagementClient(credential, subscription_id)

            for vm_id in instance_ids:
                vm_name = vm_id.split("/")[-1]
                vm_instance = compute_client.virtual_machines.instance_view(resource_group, vm_name)
                wait_for(
                    lambda: vm_instance.statuses[1].display_status.lower()
                    in ["vm running", "vm deallocated"],
                    delay=10,
                    num_sec=360,
                )

                vm = compute_client.virtual_machines.get(resource_group, vm_name)
                disk_name = vm.storage_profile.os_disk.managed_disk.id.split("/")[-1]
                nic_ids = "".join([nic.id for nic in vm.network_profile.network_interfaces])
                nic_name = nic_ids.split("/")[-1]
                ip_name = (
                    network_client.network_interfaces.get(resource_group, nic_ids.split("/")[-1])
                    .ip_configurations[0]
                    .public_ip_address.id.split("/")[-1]
                )

                # Delete resource in the correct order
                vm_delete = compute_client.virtual_machines.begin_delete(resource_group, vm_name)
                vm_delete.wait()

                disk_delete = compute_client.disks.begin_delete(resource_group, disk_name)
                disk_delete.wait()

                nic_delete = network_client.network_interfaces.begin_delete(
                    resource_group, nic_name
                )
                nic_delete.wait()

                ip_delete = network_client.public_ip_addresses.begin_delete(resource_group, ip_name)
                ip_delete.wait()

        # GCP clean up
        if kwargs.get("hyperscaler") == "gcp":
            credentials = service_account.Credentials.from_service_account_info(
                cloud_creds.GCP.service_account_json
            )
            compute_client = compute_v1.InstancesClient(credentials=credentials)
            for instance in instance_ids:
                compute_client.delete(
                    project=cloud_creds.GCP.project_id,
                    zone=kwargs.get("region"),
                    instance=instance,
                )

    return _terminate


---------
@main.command()
@click.argument("spec", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.argument("output_dir", type=click.Path(file_okay=False, path_type=Path))
@click.argument("module_name")
@click.option("--generator-version", default=SUPPORTED_OPENAPI_VERSIONS[-1], help="Specify the version of the OpenAPI generator to use. Defaults to the latest supported version.")
@click.option("--cleanup/--no-cleanup", is_flag=True, help="Option to clean up the generated files after running the generator.")
def run_code_generator(
    spec: Path,
    output_dir: Path,
    module_name: str,
    generator_version: str,
    cleanup: bool,
) -> None:
    """
    Generate a client using the provided OpenAPI specification.

    SPEC: Path to the OpenAPI spec file.

    OUTPUT_DIR: Directory where the generated code will be saved.

    MODULE_NAME: Name of the Python module to be generated.
    """
    purge_old_package(output_dir=Path(output_dir), module_name=module_name)
    run_openapi_generator(
        api_spec=spec,
        output_dir=output_dir,
        module_name=module_name,
        skip_validate=False,
        generator_version=generator_version,
        backend=Backend.direct,
    )
    if cleanup:
        prepare_plugin_for_commit(
            output_dir=Path(output_dir), module_name=module_name, api_spec=spec
        )


