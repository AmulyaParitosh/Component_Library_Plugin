from PySide6.QtCore import Signal

from ...api import ApiInterface, ComponentQueryInterface
from ...utils import ABCQObject
from ..page_manager import PageStates


class ManagerInterface(ABCQObject):
    # A base abstract class representing the interface of a manager.

    component_loaded: Signal

    api: ApiInterface
    page_states: PageStates
    query: ComponentQueryInterface

    def reload_page(self):
        """Method to reload the current page."""

    def next_page(self):
        """Method to load the next page of data."""

    def prev_page(self):
        """Method to load the previous page of data."""

    def search(self, search_key: str):
        """Method to search for components using the given search_key."""

    def sort(self, /, by: str, order: str):
        """Method to sort components based on the given criteria."""

    def filter(self, /, filetypes: list[str], tags: list[str]):
        """Method to filter components based on filetypes and tags."""
