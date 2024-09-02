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
    view.details.fill({"name": image_name, "description": image_description})
    view.next.click()

    # iso is selected by default
    view.next.click()
    view.registration.fill({"username": username, "ssh_key": ssh_key})
    view.next.click()

    # no need to add the activation-key
    view.next.click()

    # select desired package at package selection step
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
    view.cancel.click()
