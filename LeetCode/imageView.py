import logging

from iqe_platform_ui.views import NotificationsPortal
from widgetastic.widget import Checkbox, ConditionalSwitchableView, Text, TextInput, View
from widgetastic_patternfly5 import (
    BreadCrumb,
    Button,
    CheckboxSelect,
    Dropdown,
    Modal,
    Pagination,
    PatternflyTable,
    Select,
    Tab,
)

from iqe_edge import ApplicationEdgeException
from iqe_edge.widgetastic_iqe import (
    CheckSelect,
    DescriptionList,
    DualListSelector,
    EdgeSearchableTableMixin,
    NameURL,
    ReleaseSelect,
)

LOGGER = logging.getLogger(__name__)


class WizardView(View):
    ROOT = ".//div[contains(@class, 'main-body')]"
    title = Text(locator=".//h1")
    body = Text(locator=".//p")


class CloseModalView(Modal):
    """
    Simple modal view to be used for teardowns
    """

    cancel = Button("Cancel")


class ImageAllView(View, EdgeSearchableTableMixin):
    """
    Represent the "Manage images" page
    """

    COMPACT_PAGINATION = True
    SEARCH_RELOADS_TABLE = False
    title = Text(
        locator=(
            ".//h1[@widget-type='InsightsPageHeaderTitle' or contains(@class, 'pf-v5-c-title')]"
        )
    )
    table = PatternflyTable(
        locator=".//table[contains(@class, 'pf-v5-c-table')]",
        column_widgets={
            "Name": Button(),
            6: Dropdown(locator=".//div[contains(@class, 'pf-c-dropdown')]"),
        },
    )
    clear_filter = Button("Reset filters")
    create_button = Button("Create new image")
    notifications_portal = View.nested(NotificationsPortal)

    column_selector = Select()
    _input_box = TextInput(locator=".//input[@placeholder='Filter by name']")
    _status_selector = CheckboxSelect(locator="(.//div[contains(@class, 'pf-c-select')])[3]")

    find_input_box = ConditionalSwitchableView(reference="column_selector")
    find_input_box.register("Name", default=True, widget=_input_box)
    find_input_box.register("Status", widget=_status_selector)

    def reset_search(self):
        if self.clear_filter.is_displayed:
            self.clear_filter.click()

    @View.nested
    class EmptyState(View):
        ROOT = ".//div[contains(@class, 'pf-v5-c-empty-state')]"
        title = Text(locator=".//h4")
        create_new_image = Button("Create new image")
        clear_all_filters = Button("Clear all filters")

        @property
        def is_displayed(self):
            return self.title.text == "No match found"

    @property
    def is_displayed(self):
        return self.title.is_displayed and self.title.text == "Images" and self.table.is_displayed


class ImageDetailsView(View):
    """
    Represent the image set details page
    """

    ROOT = "//main[contains(@class, 'page__main')]"
    clear_filter = Button("Reset filters")
    breadcrumb = BreadCrumb()
    name = Text(locator=".//dl/h1")
    status = Text(locator=".//dl/dd")
    last_updated = Text(locator=".//p[contains(text(), 'Last updated')]")
    more_actions = Dropdown(locator="(.//div[contains(@class, 'pf-c-dropdown')])[1]")

    def reset_search(self):
        if self.clear_filter.is_displayed:
            self.clear_filter.click()

    @View.nested
    class details(Tab):
        details = DescriptionList(locator=".//div[contains(@class, 'pf-v5-c-content')]")
        ostree_commit_hash = TextInput(
            locator=".//div[@id = 'ostree-commit-hash-clipboard-copy']//input"
        )

    @View.nested
    class versions(Tab):
        paginator = Pagination(
            locator=".//div[@id='toolbar-header')]//div[contains(@class, 'pf-c-pagination')]"
        )
        table = PatternflyTable(
            locator=".//table[contains(@class, 'pf-v5-c-table')]",
            column_widgets={
                "Version": Button(),
                5: Dropdown(locator=".//div[contains(@class, 'pf-c-dropdown')]"),
            },
        )
        filter_by_status = CheckboxSelect()

        @View.nested
        class EmptyState(View):
            ROOT = ".//div[contains(@class, 'pf-v5-c-empty-state')]"
            title = Text(locator=".//h4")
            clear_all_filters = Button(
                locator=".//button[contains(@class, 'pf-v5-c-button pf-m-link')]"
            )

            @property
            def is_displayed(self):
                return self.title.text == "No match found" and self.clear_all_filters.is_displayed

        @property
        def is_displayed(self):
            return self.table.is_displayed

    @property
    def is_displayed(self):
        return self.name.is_displayed

    @View.nested
    class EmptyState(View):
        ROOT = ".//div[contains(@class, 'pf-v5-c-empty-state')]"
        title = Text(locator=".//h4")
        body = Text(locator=".//div[@class = 'pf-v5-c-empty-state__body']")
        back_button = Button("Back to Manage Images")

        @property
        def is_displayed(self):
            return (
                self.title.text == "Image not found"
                and self.back_button.is_displayed
                and self.body.text
                == "Please check you have the correct link with the correct image Id."
            )


class ImageVersionDetailsView(ImageDetailsView):
    """
    Represent the image version details page
    """

    @View.nested
    class details(Tab):
        details = DescriptionList(locator=".//div[contains(@class, 'pf-c-content')]")

    @View.nested
    class packages(Tab, EdgeSearchableTableMixin):
        find_input_box = TextInput(locator=".//input[@placeholder='Filter by name']")
        additional_button = Button(locator=".//button[normalize-space(.)= 'Additional']")
        all_button = Button(locator=".//button[normalize-space(.)= 'All']")
        paginator_footer = Pagination(locator=".//div[contains(@data-testid, 'pagination-footer')]")
        table = PatternflyTable(
            locator=".//table[contains(@class, 'pf-v5-c-table')]",
            column_widgets={3: Button("More information")},
        )

        @View.nested
        class EmptyState(View):
            ROOT = ".//div[contains(@class, 'pf-v5-c-empty-state')]"
            title = Text(locator=".//h4")
            body = Text(locator=".//div[@class = 'pf-v5-c-empty-state__body']")

            @property
            def is_displayed(self):
                return self.title.text == "No packages to display" or (
                    self.title.text == "Package data currently unavailable"
                    and self.body.text
                    == "Packages will be displayed as soon as the image is finished being built."
                )

    @property
    def is_displayed(self):
        return self.name.is_displayed


class UpdateImageView(View):
    """This class represent the modal for updating an image"""

    ROOT = ".//div[contains(@id, 'pf-modal')]"
    title = Text(locator=".//h2")
    close_button = Button(
        locator="//div[contains(@id, 'pf-modal')]//button[contains(@class, 'close')]"
    )
    next = Button("Next")
    back = Button("Back")
    cancel = Button("Cancel")
    create = Button("Update image")

    @View.nested
    class details(WizardView):
        description = TextInput(locator=".//textarea[@id='description']")

        @property
        def is_displayed(self):
            return self.title.text == "Details"

    @View.nested
    class output(WizardView):
        release_select = ReleaseSelect(locator=".//div[contains(@class, 'pf-c-select')]")
        output_type = CheckSelect()
        name_error = Text(locator="//span[contains(text(), 'Required')]")

        @property
        def is_displayed(self):
            return self.title.text == "Options"

    @View.nested
    class registration(WizardView):
        username = TextInput(locator=".//input[@id='username']")
        ssh_key = TextInput(locator=".//textarea[@id='credentials']")
        user_required_error = Text(locator="//span[contains(text(), 'Required')]")
        user_reserved_names_error = Text(locator="//span[contains(text(), 'username reserved')]")
        ssh_key_required_error = Text(locator="//span[contains(text(), 'Required')]")
        ssh_key_invalid_error = Text(locator="//span[contains(text(), 'match pattern')]")
        learn_more = Button(locator=".//a[contains(@class, 'pf-m-visited')]")

        @property
        def is_displayed(self):
            return self.title.text == "System registration"

    @View.nested
    class custom_repos(WizardView, EdgeSearchableTableMixin):
        COMPACT_PAGINATION = True
        SEARCH_RELOADS_TABLE = False

        bulk_select = Dropdown(locator=".//div[contains(@class, 'pf-c-dropdown')]")
        find_input_box = TextInput(locator=".//input[@placeholder='Filter by name']")
        table = PatternflyTable(
            locator=".//table",
            column_widgets={
                0: Checkbox(locator=".//input[@type='checkbox']"),
                "Name": NameURL(locator="."),
            },
        )

        def get_row_by_name(self, name, search=False):
            def _get_row(name):
                self.table.clear_cache()
                for row in self.table:
                    if row.name.widget.get_name() == name:
                        return row

            if search:
                self.search(name)

            return None if self.is_empty else _get_row(name)

        @property
        def is_displayed(self):
            return self.title.text == "Custom repositories" and self.table.is_displayed

    @View.nested
    class custom_packages(WizardView):
        selector = DualListSelector(locator="(.//div[contains(@class, 'pf-c-dual-list-selector')])")

        @property
        def is_displayed(self):
            return self.title.text == "Additional custom packages"

    @View.nested
    class packages(WizardView):
        selector = DualListSelector(
            locator="(.//div[contains(@class, 'pf-v5-c-dual-list-selector')])[1]"
        )

        @property
        def is_displayed(self):
            return self.title.text == "Additional Red Hat packages"

    @View.nested
    class review(WizardView):
        details = DescriptionList(locator=".//div[@class='pf-c-content']")

        @property
        def is_displayed(self):
            return self.title.text == "Review"

    @property
    def is_displayed(self):
        return self.title.is_displayed and "Update image" in self.title.text

    def fill_wizard(self, **kwargs):
        """Fill the create/update image wizard

        Kwargs:
            description: (str) image description
            username: (str) username
            ssh_key: (str) ssh_key
            release: (str) release
            output_type: (str) output_type
            custom_repos: (list) custom repo names to select for the image
            custom_packages: (str) custom package to select for the image
            custom_packages_filter: (str) used to search for custom packages
            packages: (list) packages to select for the image
            packages_filter: (str) used to search for packages
            remove_packages: (list) packages to remove from the image
            remove_filter: (str) used to search for packages
            name: name for the image (for creation only)
        """
        INSTALLER_OUTPUT_TYPE = "rhel-edge-installer"
        username = kwargs.get("username", None)
        ssh_key = kwargs.get("ssh_key", None)
        name = kwargs.get("name", None)
        description = kwargs.get("description", None)
        release = kwargs.get("release", None)
        output_type = kwargs.get("output_type", INSTALLER_OUTPUT_TYPE)
        custom_repos = kwargs.get("custom_repos", [])
        custom_packages = kwargs.get("custom_packages", [])
        custom_packages_filter = kwargs.get("custom_packages_filter", None)
        packages = kwargs.get("packages", [])
        packages_filter = kwargs.get("packages_filter", None)
        remove_packages = kwargs.get("remove_packages", [])
        remove_filter = kwargs.get("remove_filter", None)

        # Details step
        if name:
            self.details.fill({"name": name})
        self.details.fill({"description": description})
        self.next.click()

        # Options step
        self.output.wait_displayed()
        if release:
            self.output.release_select.select_item(release, close=False)
        # FIXME: Workaround to avoid Selenium issue where Next button is initially disabled.
        self.output.output_type.clear_selected()
        if INSTALLER_OUTPUT_TYPE in output_type:
            self.output.output_type.select(output_type)
        self.next.click()

        # System registration step
        if INSTALLER_OUTPUT_TYPE in output_type:
            self.registration.wait_displayed()
            self.registration.fill({"username": username, "ssh_key": ssh_key})
            self.next.click()

        # Additional Red Hat packages step
        self.packages.wait_displayed()
        if packages:
            self.packages.selector.add_to_chosen(packages, filter_text=packages_filter)
        if remove_packages:
            self.packages.selector.remove_chosen(packages, filter_text=remove_filter)
        self.next.click()

        # Custom repositories step
        try:
            self.custom_repos.wait_displayed()

            # If this is an update, unselect any previously-selected custom repos
            if self.browser.text(self.custom_repos.bulk_select):
                item_select_text = ""
                for item in self.custom_repos.bulk_select.items:
                    if "Select none" in item:
                        item_select_text = item
                        break
                self.custom_repos.bulk_select.item_select(item_select_text)

            # only use custom packages when using custom repos
            if custom_repos:
                for repo in custom_repos:
                    row = self.custom_repos.get_row_by_name(repo, search=True)
                    if not row:
                        raise ApplicationEdgeException("Custom repo not found")
                    row[0].widget.fill(True)
                self.next.click()

                # Custom packages step
                self.custom_packages.wait_displayed()
                if custom_packages:
                    self.custom_packages.selector.add_to_chosen(
                        custom_packages, filter_text=custom_packages_filter
                    )
                if remove_packages:
                    self.custom_packages.selector.remove_chosen(
                        custom_packages, filter_text=remove_filter
                    )

            self.next.click()
        except:  # noqa
            self.next.click()

        # During an update, we unselect any previously-selected custom repos.
        # Also remove any existing custom packages.
        # TODO: fix fill() call after
        # https://github.com/RedHatQE/widgetastic.core/issues/226 is resolved
        # clear() and fill("") do not properly clear the text element, but sending space +
        # backspace to fill() does.
        if self.custom_packages.is_displayed and not custom_repos:
            self.custom_packages.packages.fill(" \b")
            self.next.click()

        # Review step
        self.review.wait_displayed()


class CreateImageView(UpdateImageView):
    """This class represent the modal for creating a new image"""

    create = Button("Create image")

    @View.nested
    class details(WizardView):
        name = TextInput(locator=".//input[@id='name']")
        name_error = Text(locator="//span[contains(text(), 'Required')]")
        description = TextInput(locator=".//textarea[@id='description']")
        description_error = Text(locator="//span[contains(text(), 'characters')]")

        @property
        def is_displayed(self):
            return self.title.text == "Details"

    @property
    def is_displayed(self):
        return self.title.text == "Create image"


class SelectedReposView(View):
    title = Text(".//h1")
    names = DescriptionList()

    @property
    def is_displayed(self):
        return self.title.text == "Custom Repositories"


class UnlinkRepoView(View):
    title = Text(".//h1")
    packages = DescriptionList()
    name = Text(".//p")
    url = Text(".//a")
    unlink = Button("Unlink")
    cancel = Button("Cancel")

    @property
    def is_displayed(self):
        return self.title.text == "Unlink repository?"
