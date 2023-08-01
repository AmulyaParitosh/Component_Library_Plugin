from dataclasses import dataclass, field
from typing import Any

from PySide6.QtCore import QObject, Signal

from ..api.local_api.storage_adapter import LocalData
from ..config import Config
from ..data import Component, DataFactory, DTypes


@dataclass
class PageStates(QObject):
    # Class representing the state of pagination for a list of components.

    enable_next = Signal(bool)  # Signal to enable or disable the next page button.
    enable_prev = Signal(bool)  # Signal to enable or disable the previous page button.

    data: list[Component] = field(default_factory=list)  # List of components for the current page.
    total_items: int = 0  # Total number of items (components) available.
    page_no: int = 0  # Current page number.
    total_pages = 0  # Total number of pages.
    size: int = 18  # Number of items (components) per page.
    next_page: int | None = None  # Page number for the next page, or None if there's no next page.
    prev_page: int | None = None  # Page number for the previous page, or None if there's no previous page.

    def __init__(self, *args, **kwargs):
        # Initialize the QObject and the dataclass.
        super(QObject, self).__init__()
        super().__init__(*args, **kwargs)

    def load_page(self, json_response: dict[str, Any]):
        """Load the page data from the JSON response and calculate pagination."""
        self.load_page_data(json_response)
        self.calculate_pagination()
        return self

    def load_page_data(self, json_response: dict[str, Any]) -> None:
        """Load the component data for the current page from the JSON response."""
        self.data: list[Component] = DataFactory.load_many(data_list=json_response.get("items", []), dtype=DTypes.COMPONENT) # type: ignore
        self.update_existing_comps(self.data) # type: ignore

        self.total_items = json_response.get("total", 0)
        self.page_no = json_response.get("page", 1)
        self.size = json_response.get("per_page", 18)

    def update_existing_comps(self, components: list[Component]) -> None:
        """Update the existing components with file existence information."""
        with LocalData(Config.LOCAL_COMPONENT_PATH) as local_data:
            for component in components:
                self.update_existing_files_for_component(component, local_data)

    def update_existing_files_for_component(self, component: Component, local_data) -> None:
        """Update the existing files for a component with their existence status."""
        for file in component.files:
            existing_comps = local_data["filetypes"].get(file.value, set())
            # Set the existence status of the file based on whether the component name is in the existing_comps set.
            component.files[file].EXISTS = component.metadata.name in existing_comps

    def calculate_pagination(self) -> None:
        """Calculate the pagination and emit signals to enable/disable next and previous buttons."""
        # Calculate the total number of pages needed to display all items based on the page size.
        self.total_pages = (self.total_items + self.size - 1) // self.size

        if self.page_no == 1:
            # If the current page is the first page, there's no previous page.
            self.prev_page = None
            # Emit a signal to disable the previous page button.
            self.enable_prev.emit(False)
        else:
            # If the current page is not the first page, calculate the previous page number.
            self.prev_page = self.page_no - 1
            # Emit a signal to enable the previous page button.
            self.enable_prev.emit(True)

        if (self.total_items - (self.page_no * self.size)) < 0:
            # If there are no more items beyond the current page, there's no next page.
            self.next_page = None
            # Emit a signal to disable the next page button.
            self.enable_next.emit(False)
        else:
            # If there are more items beyond the current page, calculate the next page number.
            self.next_page = self.page_no + 1
            # Emit a signal to enable the next page button.
            self.enable_next.emit(True)
