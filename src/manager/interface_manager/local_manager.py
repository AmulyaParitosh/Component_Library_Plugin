from typing import Any

from PySide6.QtCore import Signal

from src.data.factory import DataFactory

from ...api.local_api import LocalApi, LocalComponentQuery
from ...data import Component, DTypes, FileTypes
from ..page_manager import PageStates
from .base import ManagerInterface


class LocalStorageManager(ManagerInterface):
    component_loaded = Signal()
    api : LocalApi

    # query : LocalComponentQuery = LocalComponentQuery()
    page_states = PageStates()

    def __init__(self) -> None:
        super().__init__()
        self.api = LocalApi()

    def request_components(self):
        """Method to request components from the API using the current query."""
        components = self.api.read()
        self.page_states.load_page(components)
        self.component_loaded.emit()

    def reload_page(self):
        return self.request_components()

    def load_from_db(self, dtype: DTypes):
        match dtype:
            case DTypes.TAG:
                return DataFactory.load_many(self.api.get_tags(), dtype)

    def remove_file(self, component: Component, filetype: FileTypes):
        self.api.delete(component, filetype)
