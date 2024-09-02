from collections import Counter, namedtuple

import fauxfactory
import pytest
from iqe.base.application.implementations.web_ui import navigate_to
from iqe_platform_ui.views import LoginPage
from selenium.common.exceptions import NoSuchElementException
from wait_for import wait_for
from widgetastic.exceptions import RowNotFound

from iqe_edge.utils.images_utils import RESERVED_USERNAMES
from iqe_edge.utils.ui_utils import create_custom_browser_download, wait_and_assert_image_download
from iqe_edge.views.image import ImageAllView, ImageDetailsView, ImageVersionDetailsView

pytestmark = pytest.mark.usefixtures("edge_universal_ui_teardown")

OutputType = namedtuple("OutputType", ["id", "text"])
Filter = namedtuple("Filter", ["id", "column", "value", "filter_name"])
VersionFilter = namedtuple("VersionFilter", ["id", "ui_status", "filter_status"])
Distribution = namedtuple("Distribution", ["name", "id", "selector"])

VERSION_FILTERS = [
    VersionFilter("status-created", "Created", "Created"),
    VersionFilter("status-success", "Ready", "Ready"),
]
OUTPUT_TYPES = [
    OutputType("installer", "rhel-edge-installer"),
    OutputType("commit", "rhel-edge-commit"),
]
DISTRIBUTIONS = [
    Distribution("RHEL 8.9", "rhel-89", "Red Hat Enterprise Linux (RHEL) 8.9"),
    Distribution("RHEL 9.3", "rhel-93", "Red Hat Enterprise Linux (RHEL) 9.3"),
]
DEFAULT_OUTPUT_TYPE = "rhel-edge-installer rhel-edge-commit"
DEFAULT_DISTRO = "RHEL 8.9"
PACKAGES = "gcc"
CUSTOM_PACKAGES = "Elephant"
EDIT_PACKAGES = "git"
SORT_BY = ["Name"]
VERSIONS_TABLE_SORT = ["Version", "Created"]
FILTERS = [
    Filter("name", "Name", "IQE-test-image", ""),
    Filter("status-ready", "Status", "Ready", "SUCCESS"),
    Filter("status-error", "Status", "Error", "ERROR"),
]


@pytest.mark.core
@pytest.mark.stage_ui
def test_ui_image_details(application, latest_image_iso):
    """
    Test that image details page is displayed

    metadata:
        importance: high
        assignee: tpapaioa
        requirements: EDGE-IMAGES-UI-CORE

    """
    latest_image, imageset = latest_image_iso
    image = application.edge.collections.image.instantiate(
        name=latest_image.name, set_name=latest_image.name
    )
    view = navigate_to(image, "Details")
    assert view.is_displayed

    # Validate image with status Ready is displaying Ostree Commit Hash
    assert (
        view.details.ostree_commit_hash.value == latest_image.commit.os_tree_commit
    ), "OSTree commit hash not displayed"

    # validate breadcrumb elements and link to all images view
    assert ["Manage Images", image.name] == view.breadcrumb.locations
    view.breadcrumb.click_location("Manage Images")
    view = view.browser.create_view(ImageAllView)
    assert view.is_displayed

    view = image.create_view(ImageDetailsView)
    # Validate image set not found
    application.web_ui.widgetastic_browser.url = (
        f"{application.edge.ui_address}/manage-images/9999999999"
    )
    wait_for(
        lambda: view.EmptyState.title.is_displayed, timeout=20, delay=0.5, handle_exception=True
    )
    assert view.EmptyState.is_displayed


# @pytest.mark.core
@pytest.mark.parametrize(
    "output_type, distribution",
    zip(OUTPUT_TYPES, DISTRIBUTIONS),
    ids=["installer-rhel-89", "commit-rhel-93"],
)
def test_ui_create_image(application, output_type, distribution, remove_image_set_by_name_teardown):
    """Test creating a new image
    metadata:
        importance: high
        assignee: tshinhar
        requirements: EDGE-IMAGES-UI-CORE
    """

    image_name = fauxfactory.gen_alphanumeric(start=f"test_image_ui_{distribution.id}_", length=28)
    remove_image_set_by_name_teardown(image_name)
    image_description = fauxfactory.gen_alphanumeric(15, start="image_desc_")
    username = fauxfactory.gen_alphanumeric(start="usr_")
    ssh_key = fauxfactory.gen_alphanumeric(start="ssh-rsa test")
    collection = application.edge.collections.image
    # create image with given parameters
    image, alert_err = collection.create(
        name=image_name,
        description=image_description,
        username=username,
        ssh_key=ssh_key,
        release=distribution.selector,
        output_type=output_type.text,
    )
    # verify the image was created correctly
    view = image.create_view(ImageAllView)
    row = view.find_row(name=image_name)
    assert row["Version"].text == "1"
    assert row["Status"].text == "Image build in progress"
    assert alert_err == "", f"alert error: {alert_err}"


@pytest.mark.core
@pytest.mark.stage_ui
@pytest.mark.usefixtures("teardown_close_wizard")
def test_ui_create_image_details_validation(application):
    """Test validation error when creating a new image without name and description limit overflow

    metadata:
        importance: high
        assignee: tshinhar
        requirements: EDGE-ERROR-HANDLING-UI
    """

    image_name = fauxfactory.gen_alphanumeric(start="image_")
    image_description = fauxfactory.gen_alphanumeric(15, start="image_desc_")
    view = navigate_to(application.edge.collections.image, "Create")
    view.details.fill({"name": image_name, "description": image_description})
    # need to interact with the input in order for the error to show
    view.details.fill({"name": ""})

    assert view.details.name_error.text == "Required"
    assert view.next.disabled, "Error- 'next' button should be disabled"

    image_description_overflow = fauxfactory.gen_alphanumeric(251, start="image_desc_")
    view.details.fill({"name": image_name, "description": image_description_overflow})
    assert view.details.description_error.text == "Can have maximum of 250 characters."
    assert view.next.disabled, "Error- 'next' button should be disabled"
    view.cancel.click()


@pytest.mark.core
@pytest.mark.usefixtures("teardown_close_wizard")
def test_ui_create_image_no_ssh(application):
    """Test errors when creating a new image with bad  ssh-key/username

    metadata:
        importance: high
        assignee: tshinhar
        requirements: EDGE-ERROR-HANDLING-UI
    """
    image_name = fauxfactory.gen_alphanumeric(start="image_")
    image_description = fauxfactory.gen_alphanumeric(15, start="image_desc_")
    username = fauxfactory.gen_alphanumeric(start="usr_")
    ssh_key = "not valid"

    view = navigate_to(application.edge.collections.image, "Create")
    view.details.fill({"name": image_name, "description": image_description})
    view.next.click()

    # iso is selected by default
    view.next.click()
    view.registration.fill({"username": username, "ssh_key": ssh_key})

    # test errors for empty fields
    view.registration.fill({"username": "", "ssh_key": ""})
    view.title.click()
    assert view.registration.user_required_error.text == "Required"
    assert view.registration.ssh_key_required_error.text == "Required"
    assert view.next.disabled, "Error- 'next' button should be disabled"

    # test errors for invalid ssh key
    view.registration.fill({"ssh_key": ssh_key})
    assert "Value does not match pattern" in view.registration.ssh_key_invalid_error.text
    assert view.next.disabled, "Error- 'next' button should be disabled"

    # test errors for valid ssh key but reserved username
    view.registration.fill({"ssh_key": "ssh-rsa xxx"})
    errs = []
    for name in RESERVED_USERNAMES:
        view.registration.fill({"username": name})
        if not (
            view.registration.user_reserved_names_error.is_displayed
            and view.registration.user_reserved_names_error.text
            == "This is a username reserved for the system"
        ):
            errs.append(f"Error message not displayed for username {name}")
        if not view.next.disabled:
            errs.append(f"Next button not disabled for username {name}")
    assert not errs
    view.cancel.click()


# @pytest.mark.core
def test_ui_create_image_with_packages(application, remove_image_set_by_name_teardown):
    """Test creating a new image with extra packages

    metadata:
        importance: high
        assignee: tshinhar
        requirements: EDGE-IMAGES-UI-CORE
    """

    image_name = fauxfactory.gen_alphanumeric(start="test_image_ui_", length=20)
    remove_image_set_by_name_teardown(image_name)
    image_description = fauxfactory.gen_alphanumeric(15, start="image_desc_")
    username = fauxfactory.gen_alphanumeric(start="usr_")
    ssh_key = fauxfactory.gen_alphanumeric(start="ssh-rsa test")
    # TODO: add teardown if api to delete images becomes available
    collection = application.edge.collections.image
    # create process with given parameters
    image, alert_err = collection.create(
        name=image_name,
        description=image_description,
        username=username,
        ssh_key=ssh_key,
        packages=PACKAGES,
        packages_filter=PACKAGES,
    )
    # verify the image was created correctly
    view = image.create_view(ImageAllView)
    row = view.find_row(name=image_name)
    assert row, "Error - image not found"
    view = navigate_to(image, "Details")
    assert "Last updated Just now" in view.last_updated.text
    params = view.details.details.read()
    assert params["Description"] == image_description
    assert params["Release"] == DEFAULT_DISTRO
    for output_type in DEFAULT_OUTPUT_TYPE.split(" "):
        assert output_type in params["Type(s)"]
    assert params["Version"] == "1"
    assert params["Created"] == "Just now"
    assert params["Username"] == username
    assert params["Total additional packages"] == "1"
    row = view.versions.table.row(version="1")
    row["Version"].widget.click()
    view = image.create_view(ImageVersionDetailsView)
    assert view.packages.EmptyState.is_displayed
    assert alert_err == "", f"alert error: {alert_err}"


@pytest.mark.core
@pytest.mark.stage_ui
@pytest.mark.parametrize("output_type", OUTPUT_TYPES, ids=[o.id for o in OUTPUT_TYPES])
def test_ui_create_image_custom_repo(
    application,
    output_type,
    big_zoo_repo,
    remove_image_set_by_name_teardown,
    content_sources_feature_flag,
):
    """Test creating a new image with custom repos and packages

    metadata:
        importance: high
        assignee: tpapaioa
        requirements: EDGE-IMAGES-UI-CORE
    """
    image_name = fauxfactory.gen_alphanumeric(start="test_image_ui_", length=20)
    remove_image_set_by_name_teardown(image_name)
    image_description = fauxfactory.gen_alphanumeric(15, start="image_desc_")
    username = fauxfactory.gen_alphanumeric(start="usr_")
    ssh_key = fauxfactory.gen_alphanumeric(start="ssh-rsa test")

    collection = application.edge.collections.image
    image, alert_err = collection.create(
        name=image_name,
        description=image_description,
        username=username,
        ssh_key=ssh_key,
        custom_repos=[big_zoo_repo.name],
        custom_packages=CUSTOM_PACKAGES,
        custom_packages_filter=CUSTOM_PACKAGES,
        packages=PACKAGES,
        packages_filter=PACKAGES,
    )

    view = navigate_to(collection, "All")
    row = view.find_row(name=image.name)
    # TODO: Validate custom repo and package details when added to UI
    assert row["Status"].text == "Image build in progress"
    assert alert_err == "", f"alert error: {alert_err}"


# @pytest.mark.core
@pytest.mark.parametrize(
    "output_type, distribution",
    zip(OUTPUT_TYPES, DISTRIBUTIONS),
    ids=["installer-rhel88", "commit-rhel-92"],
)
def test_ui_update_image(
    application,
    api_client,
    output_type,
    distribution,
    latest_image_iso,
    remove_image_set_by_name_teardown,
):
    """Test updating an image

    metadata:
        importance: high
        assignee: tshinhar
        requirements: EDGE-IMAGES-UI-CORE
    """
    latest_image, image_set = latest_image_iso

    latest_image = api_client.default_api.get_image(image_set.images[0].id)
    remove_image_set_by_name_teardown(latest_image.name)

    distro = distribution.name

    # we take the name of the image-set in case the image name was changed
    image = application.edge.collections.image.instantiate(
        name=latest_image.name, set_name=latest_image.name
    )

    new_description = fauxfactory.gen_alphanumeric(15, start="edited_desc_")
    new_username = fauxfactory.gen_alphanumeric(start="edited_")
    new_ssh_key = fauxfactory.gen_alphanumeric(30, start="ssh-rsa edited")

    remove_packages = ""
    add_packages = ""
    if (
        latest_image.packages is not None
        and len(latest_image.packages) > 0
        and EDIT_PACKAGES in [package.name for package in latest_image.packages]
    ):
        remove_packages = EDIT_PACKAGES
    else:
        add_packages = EDIT_PACKAGES
    # update image with given parameters
    image.update(
        description=new_description,
        release=distribution.selector,
        username=new_username,
        ssh_key=new_ssh_key,
        packages=add_packages,
        packages_filter=add_packages,
        remove_packages=remove_packages,
        output_type=output_type.text,
    )
    # verify the image was updated correctly
    view = navigate_to(image, "Details")
    params = view.details.details.read()
    assert params["Release"] == distro
    # commit should always be an output type
    assert DEFAULT_OUTPUT_TYPE.split(" ")[1] in params["Type(s)"]
    # this is to verify installer as well
    assert output_type.text in params["Type(s)"]
    if remove_packages == EDIT_PACKAGES:
        assert int(params["Total additional packages"]) == len(latest_image.packages) - 1
    elif latest_image.packages is None:
        assert int(params["Total additional packages"]) == 1
    else:
        assert int(params["Total additional packages"]) == len(latest_image.packages) + 1
    assert int(params["Version"]) == latest_image.version + 1
    assert params["Description"] == new_description
    row = view.versions.table.row(version=params["Version"])
    row["version"].widget.click()
    view = image.create_view(ImageVersionDetailsView)
    assert view.packages.EmptyState.is_displayed


@pytest.mark.core
@pytest.mark.stage_ui
@pytest.mark.parametrize("output_type", OUTPUT_TYPES, ids=[o.id for o in OUTPUT_TYPES])
def test_ui_update_image_custom_repo(
    application, latest_image_iso, output_type, big_zoo_repo, content_sources_feature_flag
):
    """Test updating an image with custom repos and packages

    metadata:
        importance: high
        assignee: tpapaioa
        requirements: EDGE-IMAGES-UI-CORE
    """
    latest_image, image_set = latest_image_iso

    collection = application.edge.collections.image
    image = collection.instantiate(name=latest_image.name, set_name=image_set.name)

    # Update the image with the given parameters
    alert_err = image.update(
        username=latest_image.installer.username,
        ssh_key=latest_image.installer.ssh_key,
        custom_repos=[big_zoo_repo.name],
        custom_packages=CUSTOM_PACKAGES,
        custom_packages_filter=CUSTOM_PACKAGES,
        output_type=output_type.text,
    )

    view = navigate_to(collection, "All")
    row = view.find_row(name=image.name)
    # TODO: Validate custom repo and package details when added to UI
    assert row["Status"].text == "Image build in progress"
    assert alert_err == "", f"alert error: {alert_err}"


# @pytest.mark.core
def test_ui_update_image_from_details(application, latest_image_iso):
    """Test updating an image from the image details page

    metadata:
        importance: high
        assignee: tshinhar
        requirements: EDGE-IMAGES-UI-CORE
    """
    latest_image, image_set = latest_image_iso
    if latest_image.distribution == "rhel-85":
        distro = "RHEL 8.5"
    elif latest_image.distribution == "rhel-90":
        distro = "RHEL 9.0"
    else:
        distro = DEFAULT_DISTRO
    image = application.edge.collections.image.instantiate(
        name=latest_image.name, set_name=image_set.name
    )
    new_description = fauxfactory.gen_alphanumeric(15, start="edited_desc_")
    new_username = fauxfactory.gen_alphanumeric(start="edited_")
    new_ssh_key = fauxfactory.gen_alphanumeric(start="ssh-rsa ")

    remove_packages = ""
    add_packages = ""
    if (
        latest_image.packages is not None
        and len(latest_image.packages) > 0
        and EDIT_PACKAGES in [package.name for package in latest_image.packages]
    ):
        remove_packages = EDIT_PACKAGES
    else:
        add_packages = EDIT_PACKAGES

    # update image with given parameters
    image.update_from_details(
        description=new_description,
        username=new_username,
        ssh_key=new_ssh_key,
        packages=add_packages,
        packages_filter=add_packages,
        remove_packages=remove_packages,
        output_type=DEFAULT_OUTPUT_TYPE.split(" ")[0],
    )

    # verify the image was updated correctly
    view = navigate_to(image, "Details")
    view.browser.refresh()
    params = view.details.details.read()
    assert params["Release"] == distro
    for output_type in DEFAULT_OUTPUT_TYPE.split(" "):
        assert output_type in params["Type(s)"]
    if remove_packages == EDIT_PACKAGES:
        assert int(params["Total additional packages"]) == len(latest_image.packages) - 1
    elif latest_image.packages is None:
        assert int(params["Total additional packages"]) == 1
    else:
        assert int(params["Total additional packages"]) == len(latest_image.packages) + 1
    assert int(params["Version"]) == latest_image.version + 1
    assert params["Description"] == new_description
    row = view.versions.table.row(version=params["Version"])
    row["version"].widget.click()
    view = image.create_view(ImageVersionDetailsView)
    assert view.packages.EmptyState.is_displayed


# @pytest.mark.core
def test_ui_update_image_from_version(application, latest_image_iso):
    """Test updating an image from the image details page

    metadata:
        importance: high
        assignee: tshinhar
        requirements: EDGE-IMAGES-UI-CORE
    """
    latest_image, image_set = latest_image_iso
    if latest_image.distribution == "rhel-85":
        distro = "RHEL 8.5"
    elif latest_image.distribution == "rhel-90":
        distro = "RHEL 9.0"
    else:
        distro = DEFAULT_DISTRO
    version = application.edge.collections.image_version.instantiate(
        image_name=image_set.name, version=latest_image.version
    )
    new_description = fauxfactory.gen_alphanumeric(15, start="edited_desc_")
    new_username = fauxfactory.gen_alphanumeric(start="edited_")
    new_ssh_key = fauxfactory.gen_alphanumeric(start="ssh-rsa ")

    remove_packages = ""
    add_packages = ""
    if (
        latest_image.packages is not None
        and len(latest_image.packages) > 0
        and EDIT_PACKAGES in [package.name for package in latest_image.packages]
    ):
        remove_packages = EDIT_PACKAGES
    else:
        add_packages = EDIT_PACKAGES

    # update image with given parameters
    version.update_from_version(
        description=new_description,
        username=new_username,
        ssh_key=new_ssh_key,
        packages=add_packages,
        packages_filter=add_packages,
        remove_packages=remove_packages,
        output_type=DEFAULT_OUTPUT_TYPE.split(" ")[0],
    )

    # verify the image was updated correctly
    version.browser.refresh()
    view = navigate_to(version, "Details")
    view.browser.refresh()
    params = view.details.details.read()
    assert params["Release"] == distro
    for output_type in DEFAULT_OUTPUT_TYPE.split(" "):
        assert output_type in params["Type(s)"]
    if remove_packages == EDIT_PACKAGES:
        assert int(params["Total additional packages"]) == len(latest_image.packages) - 1
    elif latest_image.packages is None:
        assert int(params["Total additional packages"]) == 1
    else:
        assert int(params["Total additional packages"]) == len(latest_image.packages) + 1
    assert int(params["Version"]) == latest_image.version + 1
    assert params["Description"] == new_description


@pytest.mark.core
@pytest.mark.stage_ui
def test_ui_package_more_info_link(application, latest_image_iso, teardown_ui_close_tab):
    """that the link on the packages table is working correctly

    metadata:
        importance: high
        assignee: tshinhar
        requirements: EDGE-IMAGES-UI-CORE
    """
    latest_image, image_set = latest_image_iso
    image = application.edge.collections.image_version.instantiate(
        image_name=image_set.name, version=latest_image.version
    )
    package_name = "glibc"  # this package should always be in the image
    view = navigate_to(image, "Details")

    view.packages.all_button.click()
    view.packages.find_input_box.fill(package_name)
    wait_for(lambda: view.packages.table.is_displayed, timeout=10, delay=0.5, handle_exception=True)
    row = view.packages.table.row(name=package_name)

    more_info_url = view.browser.element(f"{row[3].widget.locator}/..").get_attribute("href")
    assert package_name in more_info_url
    row[3].widget.click()
    # switch selenium to the new tab
    view.browser.selenium.switch_to.window(view.browser.selenium.window_handles[-1])
    help_view = image.create_view(LoginPage)
    wait_for(lambda: help_view.is_displayed, timeout=20, delay=0.5, handle_exception=True)


@pytest.mark.core
@pytest.mark.stage_ui
@pytest.mark.parametrize("tab", ["all", "additional"])
def test_ui_package_filter(application, tab, latest_image_iso):
    """test that the packages table can be filtered

    metadata:
        importance: medium
        assignee: tshinhar
        requirements: EDGE-UI-FILTERING
    """
    latest_image, image_set = latest_image_iso
    image = application.edge.collections.image_version.instantiate(
        image_name=image_set.name, version=latest_image.version
    )
    view = navigate_to(image, "Details")
    if tab == "additional":
        view.packages.additional_button.click()
    rand_index = fauxfactory.gen_choice(range(view.packages.table.row_count))
    value = view.packages.table[rand_index]["Name"].text

    # search package we don't have
    view.packages.search("non-existent")
    wait_for(
        lambda: view.packages.EmptyState.is_displayed, timeout=20, delay=0.5, handle_exception=True
    )
    assert view.packages.table.headers
    view.packages.parent.reset_search()

    # search package we have
    view.packages.search(value)
    wait_for(lambda: view.packages.table.is_displayed, timeout=20, delay=0.5, handle_exception=True)
    assert all(value in row["Name"].text for row in view.packages.table)


@pytest.mark.core
@pytest.mark.stage_ui
@pytest.mark.parametrize("filter_type", FILTERS, ids=[f.id for f in FILTERS])
def test_ui_image_filter(application, filter_type, teardown_ui_clear_filter, api_client):
    """Test the filter in the images page

    metadata:
        importance: medium
        assignee: tshinhar
        requirements: EDGE-UI-FILTERING
    """
    column = filter_type.column

    # Skip status filter checking until issue is fixed
    if column == "Status":
        pytest.skip(reason="https://issues.redhat.com/browse/THEEDGE-2953")

    value = filter_type.value
    filter_name = filter_type.filter_name
    view = navigate_to(application.edge.collections.image, "All")
    # pass the view to the teardown fixture
    teardown_ui_clear_filter(view)
    if column == "Name":
        view.search("non-existent", column=column)
        wait_for(lambda: view.is_empty, timeout=20, delay=0.5, handle_exception=True)
        assert view.EmptyState.is_displayed, "Error- empty-state is not displayed correctly"
        assert view.table.headers
        view.clear_filter.click()
        view.search(value)
        wait_for(lambda: view.table.is_displayed, timeout=20, delay=0.5, handle_exception=True)
        assert all(value.lower() in row[column].text.lower() for row in view.table)
    else:
        view.search({value: True}, column=column)
        if column == "Status":
            count = api_client.default_api.list_all_image_sets(status=filter_name).count
            assert all(row[column].text == value for row in view.table)
            assert count == view.results


@pytest.mark.core
@pytest.mark.stage_ui
@pytest.mark.parametrize("sort_order", ["ascending", "descending"])
@pytest.mark.parametrize("sort_by", SORT_BY, ids=[s.lower() for s in SORT_BY])
def test_ui_image_sort(application, sort_by, sort_order):
    """Test the image table sort function

    metadata:
        importance: medium
        assignee: tshinhar
        requirements: EDGE-UI-FILTERING
    """
    view = navigate_to(application.edge.collections.image, "All")
    view.table.sort_by(sort_by, sort_order)
    values = [row[sort_by].text for row in view.table]
    assert (
        sorted(
            values,
            key=lambda v: (
                v.lower().replace("_", "").replace("-", "").replace("'", "").replace(" ", "")
            ),
            reverse=(sort_order == "descending"),
        )
        == values
    )


@pytest.mark.skip(
    reason="Test is failing because of container issue. https://issues.redhat.com/browse/IQE-2046"
)
@pytest.mark.core
@pytest.mark.stage_ui
def test_ui_download_from_details(application, latest_image_iso):
    """
    Download image iso from image details

    metadata:
        importance: high
        assignee: delima
        requirements: EDGE-IMAGES-UI-CORE
    """
    latest_image, image_set = latest_image_iso
    with application.copy_using(user=application.user) as sandbox_app:
        create_custom_browser_download(application, sandbox_app)
        image_name = image_set.name
        image = sandbox_app.edge.collections.image.instantiate(name=image_name, set_name=image_name)
        view = navigate_to(image, "Details")
        view.more_actions.item_select("Download installable .iso for newest image")
        wait_and_assert_image_download(sandbox_app.web_ui.browser_manager.browser, image_name)


@pytest.mark.skip(
    reason="Test is failing because of container issue. https://issues.redhat.com/browse/IQE-2046"
)
@pytest.mark.core
@pytest.mark.stage_ui
def test_ui_download_from_manager_images(application, latest_image_iso):
    """
    Download image iso from manager images

    metadata:
        importance: high
        assignee: delima
        requirements: EDGE-IMAGES-UI-CORE
    """
    latest_image, image_set = latest_image_iso
    with application.copy_using(user=application.user) as sandbox_app:
        create_custom_browser_download(application, sandbox_app)
        image_name = image_set.name
        view = navigate_to(sandbox_app.edge.collections.image, "All")
        try:
            row = view.find_row(name=image_name, search=image_name)
        except (RowNotFound, NoSuchElementException):
            wait_for(
                lambda: view.table.is_displayed,
                timeout=10,
                delay=0.5,
                handle_exception=True,
            )
            row = view.find_row(name=image_name, search=image_name)

        row[4].widget.item_select("Download")
        wait_and_assert_image_download(sandbox_app.web_ui.browser_manager.browser, image_name)


# @pytest.mark.core
@pytest.mark.usefixtures("teardown_close_wizard")
def test_ui_create_image_select_packages(application):
    """Test select packages when creating a new image

    metadata:
        importance: medium
        assignee: delima
        requirements: EDGE-IMAGES-UI-CORE
    """
    image_name = fauxfactory.gen_alphanumeric(start="image_")
    image_description = fauxfactory.gen_alphanumeric(15, start="image_desc_")
    username = fauxfactory.gen_alphanumeric(start="usr_")
    ssh_key = fauxfactory.gen_alphanumeric(start="ssh-rsa ")
    package = "vim"

    view = navigate_to(application.edge.collections.image, "Create")
    view.fill_wizard(
        name=image_name,
        description=image_description,
        username=username,
        ssh_key=ssh_key,
    )
    
    view.next.click()
    # 2 clicks to go back to package selection step
    view.packages.selector.available_list.search.fill(package)
    view.packages.selector.available_list.search_button.click()
    packages = view.packages.selector.available_list.list.list_options()

    # Assert packages are selected (>>)
    view.packages.selector.controls.add_all_button.click()
    packages_available = view.packages.selector.available_list.list.list_options()
    packages_chosen = view.packages.selector.chosen_list.list.list_options()
    assert len(packages_available) == 0
    assert len(packages_chosen) > 0
    assert Counter(packages) == Counter(packages_chosen)

    # Assert packages are unselected (<<)
    view.packages.selector.controls.remove_all_button.click()
    packages_available = view.packages.selector.available_list.list.list_options()
    packages_chosen = view.packages.selector.chosen_list.list.list_options()
    assert len(packages_available) > 0
    assert Counter(packages) == Counter(packages_available)
    assert len(packages_chosen) == 0


@pytest.mark.core
@pytest.mark.stage_ui
@pytest.mark.parametrize("sort_order", ["ascending", "descending"])
@pytest.mark.parametrize("sort_by", SORT_BY, ids=[s.lower() for s in SORT_BY])
def test_ui_image_packages_sort(application, latest_image_iso, sort_by, sort_order):
    """Test the image packages table sort function

    metadata:
        importance: medium
        assignee: delima
        requirements: EDGE-UI-FILTERING
    """
    latest_image, image_set = latest_image_iso

    image = application.edge.collections.image_version.instantiate(
        image_name=image_set.name, version=latest_image.version
    )
    view = navigate_to(image, "Details")
    view.packages.table.sort_by(sort_by, sort_order)
    values = [row[sort_by].text for row in view.packages.table]
    assert (
        sorted(
            values,
            reverse=(sort_order == "descending"),
        )
        == values
    )


@pytest.mark.core
@pytest.mark.stage_ui
def test_ui_image_packages_pagination(application, latest_image_iso):
    """Test the image packages table pagination function

    metadata:
        importance: medium
        assignee: delima
        requirements: EDGE-UI-FILTERING
    """
    latest_image, image_set = latest_image_iso

    column_name = "Name"
    image = application.edge.collections.image_version.instantiate(
        image_name=image_set.name, version=latest_image.version
    )
    view = navigate_to(image, "Details")
    view.packages.paginator_footer.next_page()
    items_second_page = [row[column_name].text for row in view.packages.table]
    assert view.packages.paginator_footer.current_page == 2
    view.packages.paginator_footer.previous_page()
    items_first_page = [row[column_name].text for row in view.packages.table]
    assert view.packages.paginator_footer.current_page == 1
    assert view.packages.paginator_footer.is_previous_disabled
    assert Counter(items_first_page) != Counter(items_second_page)

    view.packages.paginator_footer.last_page()
    assert view.packages.paginator_footer.is_next_disabled
    assert view.packages.paginator_footer.current_page == view.packages.paginator_footer.total_pages

    view.packages.paginator_footer.first_page()
    assert view.packages.paginator_footer.current_page == 1
    assert view.packages.paginator_footer.is_previous_disabled


@pytest.mark.core
@pytest.mark.stage_ui
@pytest.mark.parametrize("filter_value", VERSION_FILTERS, ids=[f.id for f in VERSION_FILTERS])
def test_ui_image_versions_filter(
    application, filter_value, latest_image_iso, teardown_ui_clear_filter
):
    """Test the image-set versions table filter function

    metadata:
        importance: medium
        assignee: pkesavar
        requirements: EDGE-UI-FILTERING
    """
    latest_image, image_set = latest_image_iso

    image = application.edge.collections.image_version.instantiate(
        image_name=image_set.name, version=latest_image.version
    )

    view = navigate_to(image, "All")

    # validate version table state URL (THEEDGE-1492)
    current_url = application.web_ui.widgetastic_browser.url
    assert f"{application.edge.ui_address}/manage-images/{image_set.id}/versions" in current_url

    # versions table filter test
    view.reset_search()
    teardown_ui_clear_filter(view)
    view.versions.filter_by_status.item_select(filter_value.filter_status)

    if filter_value.filter_status == "Ready":
        assert all(row["Status"].text == filter_value.ui_status for row in view.versions.table)
    else:
        # filter_status "Created" will always return EmptyState
        assert view.versions.EmptyState.is_displayed
        assert view.versions.table.headers


@pytest.mark.core
@pytest.mark.stage_ui
@pytest.mark.parametrize("sort_order", ["ascending", "descending"])
@pytest.mark.parametrize(
    "sort_by", VERSIONS_TABLE_SORT, ids=[s.lower() for s in VERSIONS_TABLE_SORT]
)
def test_ui_image_versions_sort(application, sort_by, sort_order, latest_image_iso):
    """Test the image-set versions table sort function

    metadata:
        importance: medium
        assignee: pkesavar
        requirements: EDGE-UI-FILTERING
    """
    latest_image, image_set = latest_image_iso

    image = application.edge.collections.image_version.instantiate(
        image_name=image_set.name, version=latest_image.version
    )

    view = navigate_to(image, "All")
    view.versions.table.sort_by(sort_by, sort_order)
    values = [row[sort_by].text for row in view.versions.table]
    assert (
        sorted(
            values,
            key=lambda v: (
                v.lower().replace("_", "").replace("-", "").replace("'", "").replace(" ", "")
            ),
            reverse=(sort_order == "descending"),
        )
        == values
    )


@pytest.mark.skip(
    reason="Test is failing because of container issue. https://issues.redhat.com/browse/IQE-2046"
)
@pytest.mark.core
@pytest.mark.stage_ui
def test_ui_download_from_versions(application, latest_image_iso):
    """
    Download image iso from image details

    metadata:
        importance: high
        assignee: pkesavar
        requirements: EDGE-IMAGES-UI-CORE
    """

    latest_image, image_set = latest_image_iso
    with application.copy_using(user=application.user) as sandbox_app:
        create_custom_browser_download(application, sandbox_app)
        image_name = image_set.name
        image = sandbox_app.edge.collections.image.instantiate(name=image_name, set_name=image_name)
        view = navigate_to(image, "Details")
        # Go to versions tab and download iso from latest image
        view.versions.table[0][5].widget.item_select("Download")
        wait_and_assert_image_download(sandbox_app.web_ui.browser_manager.browser, image_name)
