from __future__ import annotations

import dataclasses
import json
import os
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Callable

import click
from iqe.base.application.plugins import ApplicationPlugin
from iqe.fixtures.application import PytestContext
from iqe.utils import error_print
from iqe.utils import success_print
from iqe.utils import warning_print

from . import Backend
from . import dynamic_cache
from ._metadata import SUPPORTED_OPENAPI_VERSIONS
from ._metadata import PluginApiCodegenMetadata
from ._metadata import output_dir_override
from .code_fixing.for_codegen import prepare_plugin_for_commit
from .code_fixing.for_codegen import purge_old_package
from .dynamic_cache import cache_appdir_option
from .dynamic_cache import trigger_cache_regen

DATA_PATH = Path(__file__).parent / "data"

SCRIPT_PATH = DATA_PATH / "openapi-generator-cli.sh"


def check_command(*command: str, exit_with: Callable[[str], None] = sys.exit) -> None:
    try:
        subprocess.run([*command, "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        command_str = shlex.join(command)
        exit_with(
            f"{command_str} missing: `{command_str} --version` triggered {e}\n"
            f"please ensure a working installation of {command_str}"
        )


def check_backend(
    backend: Backend,
    generator_version: str,
    exit_with: Callable[[str], None] = sys.exit,
) -> None:
    if backend != Backend.direct:
        check_command(backend.name, exit_with=exit_with)
    else:
        check_command(
            "java",
            "-jar",
            os.fspath(dynamic_cache.download_openapi_jar(generator_version)),
            exit_with=exit_with,
        )


def _get_command(
    *,
    backend: Backend,
    generator_version: str,
    output_dir: Path,
    api_spec: Path,
    generator_name: str = "python",
) -> list[str]:
    if generator_version.startswith("6.2") and generator_name == "python":
        generator_name = "python-prior"  # todo: debug this
    if backend in (Backend.docker, Backend.podman):
        return [
            *(backend.name, "run", "--rm"),
            *(
                f"--volume={output_dir}:/output:Z",
                f"--volume={api_spec.parent}:/spec:Z",
                "--userns=keep-id",
            ),
            f"docker.io/openapitools/openapi-generator-cli:v{generator_version}",
            "generate",
            *("-i", f"/spec/{api_spec.name}"),
            *("-g", generator_name),
            *("-o", "/output"),
        ]
    else:
        assert backend is Backend.direct
        jar = os.fspath(dynamic_cache.download_openapi_jar(generator_version))
        return [
            *("java", "-jar", jar, "generate"),
            *("-i", os.fspath(api_spec)),
            *("-g", generator_name),
            *("-o", os.fspath(output_dir)),
        ]


def print_command(args: list[str], generator_version: str) -> None:
    import pprint

    cmd = pprint.pformat(args)
    print(cmd, flush=True)


def _process_generator_version(generator_version: str | None) -> str:
    if generator_version is None:
        return SUPPORTED_OPENAPI_VERSIONS[-1]
    else:
        return generator_version


def run_openapi_generator(
    *,
    api_spec: Path,
    output_dir: Path,
    module_name: str,
    skip_validate: bool,
    generator_version: str,
    backend: Backend,
) -> None:
    warning_print(f"using OPENAPI_GENERATOR_VERSION={generator_version}")

    my_env = os.environ.copy()
    my_env["OPENAPI_GENERATOR_VERSION"] = generator_version
    my_env["OPENAPI_JAR_DOWNLOAD_CACHE_DIR"] = os.fspath(
        dynamic_cache.OPENAPI_JAR_DOWNLOAD_CACHE_DIR
    )
    validate_args = ["--skip-validate-spec"] if skip_validate else []

    #
    full_command = [
        *_get_command(
            backend=backend,
            generator_version=generator_version,
            output_dir=output_dir,
            api_spec=api_spec,
        ),
        *("--package-name", module_name),
        *validate_args,
        "--global-property="
        "models,supportingFiles,apis,"
        "apiDocs=false,modelDocs=false,"
        "apiTests=false,modelTests=false,",
        "--additional-properties=generateSourceCodeOnly=true,disallowAdditionalPropertiesIfNotPresent=false",
    ]

    print_command(full_command, generator_version)
    try:
        subprocess.check_call(
            full_command,
            env=my_env,
        )
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)


def run_openapi_validator(api_spec: Path) -> None:
    try:
        subprocess.check_call(
            ["bash", os.fspath(SCRIPT_PATH), "validate", "-i", os.fspath(api_spec)]
        )
        success_print("Validation successful")
    except subprocess.CalledProcessError:
        error_print("Validation fails")
        sys.exit(1)


@click.group()
def main() -> None:
    """API client generator with Goatee templates.

    Reference: https://iqe-docs.apps.ocp4.prod.psi.redhat.com/service_objects.html
    """
    pass


plugin_name_arg = click.argument("plugin_name")
service_argument = click.argument("service_name")
backend_option = click.option(
    # todo: figure podman perms and use it by  default
    "--backend",
    type=click.Choice([b.name for b in Backend]),
    default=Backend.direct.name,
)


@main.command()
@click.pass_obj
@plugin_name_arg
@service_argument
@output_dir_override
@backend_option
def generate_api(
    obj: PytestContext,
    plugin_name: str,
    service_name: str,
    output_dir_override: Path | None,
    backend: str,
) -> None:
    """
    Runs the openapi code-generator
    with the required parameters for the given plugin/service object

    PLUGIN_NAME: Name of plugin.

    \b
    SERVICE_NAME: Name of service object.
                  https://iqe-docs.apps.ocp4.prod.psi.redhat.com/service_objects.html
    """

    plugin: ApplicationPlugin = obj.get_plugin(plugin_name)
    _generate_api(
        plugin=plugin,
        service_name=service_name,
        output_dir_override=output_dir_override,
        backend=getattr(Backend, backend),
    )


def _generate_api(
    plugin: ApplicationPlugin,
    service_name: str,
    output_dir_override: Path | None,
    backend: Backend,
) -> None:
    """
    internal helper to run the api-generator

    used for integration tests to avoid click integration issues
    """

    try:
        meta = PluginApiCodegenMetadata.for_service(
            plugin,
            service_name,
            output_dir_override=output_dir_override,
        )
    except LookupError as e:
        error_print(e)
        sys.exit(1)
    config_options = meta.service_options

    if meta.api_spec is None:
        error_print(
            f"the api spec for {meta} is missing, "
            f"please ensure its downloaded to {meta.ensure_api_spec()}"
        )
        sys.exit(1)

    if meta.output_dir is None:
        error_print(
            f"no output dir known for {meta},"
            f" please ensure {plugin.plugin_name} is installed editable"
        )
        sys.exit(1)

    assert meta.api_spec and meta.output_dir

    check_backend(backend, meta.service_options.generator_version)

    purge_old_package(output_dir=meta.output_dir, module_name=meta.module_name)
    run_openapi_generator(
        api_spec=meta.api_spec,
        output_dir=meta.output_dir,
        **dataclasses.asdict(config_options),
        backend=backend,
    )

    if output_dir_override:
        warning_print(f"not preparing git additions for {output_dir_override}")
    else:
        prepare_plugin_for_commit(
            output_dir=meta.output_dir,
            module_name=meta.module_name,
            api_spec=meta.api_spec,
        )


@main.command()
@click.argument("spec", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.argument("output_dir", type=click.Path(file_okay=False, path_type=Path))
@click.argument("module_name")
@click.option("--generator-version", default=SUPPORTED_OPENAPI_VERSIONS[-1])
@click.option("--cleanup/--no-cleanup", is_flag=True)
def run_code_generator(
    spec: Path,
    output_dir: Path,
    module_name: str,
    generator_version: str,
    cleanup: bool,
) -> None:
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


def ensure_json_diff_friendly(spec: str) -> str:
    """ensures a json spec is diff friendly indented"""
    return json.dumps(json.loads(spec), indent=2) + "\n"


@main.command()
@plugin_name_arg
@click.option("--url", default=None)
@service_argument
@click.pass_obj
def download_spec(obj: PytestContext, plugin_name: str, url: str | None, service_name: str) -> None:
    """
    Download API spec file.

    PLUGIN_NAME: Name of plugin.

    \b
    SERVICE_NAME: Name of service object.
    """
    app = obj.primary_application
    # TODO: port to actual app.http apis once feasible,
    #       abusing a different rest client to configure the http fetch is a bad hack
    evil_rest_client = app.base.rest_client.client
    plugin = obj.get_plugin(plugin_name)
    plugin_conf = plugin.config

    if plugin_name.upper() in plugin_conf:
        # TODO: Backward compatibility, remove once we moved to new config.
        plugin_conf = plugin_conf[plugin_name.upper()]

    if url is not None:
        full_url = url
    else:
        spec_url = plugin_conf["service_objects"][service_name].config.get("spec_url", None)
        path = f"/{plugin_conf['service_objects'][service_name]['config']['path']}"
        full_url = spec_url or f"{path}/openapi.json"

    if full_url.startswith("/"):
        print("downloading", f"{app.address.rstrip('/')}{full_url}")
        status_code: int
        body, status_code, _ = evil_rest_client.call_api(full_url, "GET", _preload_content=False)

        if status_code != 200:
            sys.exit(repr(status_code))
        data = body.data
    else:
        print("downloading", full_url)
        import requests

        response = requests.get(full_url)
        if response.status_code != 200:
            sys.exit(repr(response.status_code))
        data = response.content

    meta = PluginApiCodegenMetadata.for_service(plugin, service_name)

    data = ensure_json_diff_friendly(data)
    meta.ensure_api_spec().write_text(data)


@main.command()
@plugin_name_arg
@click.pass_context
@service_argument
@backend_option
def update(
    ctx: click.Context,
    plugin_name: str,
    service_name: str,
    backend: str,
) -> None:
    """
    Update API client with latest spec file.

    PLUGIN_NAME: Name of plugin.

    \b
    SERVICE_NAME: Name of service object.
    """
    ctx.invoke(download_spec, plugin_name=plugin_name, service_name=service_name)
    ctx.invoke(
        generate_api,
        plugin_name=plugin_name,
        service_name=service_name,
        backend=backend,
    )


@main.command()
@click.pass_context
@plugin_name_arg
@service_argument
def validate_spec(ctx: click.Context, plugin_name: str, service_name: str) -> None:
    """
    Validate spec file.

    PLUGIN_NAME: Name of plugin.

    \b
    SERVICE_NAME: Name of service object.
    """
    check_backend(Backend.direct, "6.2.0")  # todo: port docker
    ctx.invoke(download_spec, plugin_name=plugin_name, service_name=service_name)
    meta = PluginApiCodegenMetadata.for_service(ctx.obj.get_plugin(plugin_name), service_name)
    run_openapi_validator(api_spec=meta.api_spec)


@main.group()
def cache() -> None:
    pass


@cache.command("list")
@cache_appdir_option
def list_(cache_appdir: str | Path) -> None:
    cache_appdir = Path(cache_appdir)
    if not cache_appdir.is_dir():
        error_print(f"{cache_appdir} is not a directory")
        sys.exit(1)
    from .dynamic_cache import list_cache

    list_cache(cache_appdir)


@cache.command()
@cache_appdir_option
def clear(cache_appdir: Path) -> None:
    if not cache_appdir.is_dir():
        warning_print(f"{cache_appdir} is not a directory")
        sys.exit(1)
    import shutil

    shutil.rmtree(os.fspath(cache_appdir))


@cache.command()
@cache_appdir_option
@click.pass_obj
def refresh(ctx: PytestContext, cache_appdir: Path | str) -> None:
    cache_appdir = Path(cache_appdir)
    app = ctx.primary_application
    trigger_cache_regen(app, cache_appdir)
