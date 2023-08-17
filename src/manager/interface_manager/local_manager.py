
# SPDX-License-Identifier: MIT
# --------------------------------------------------------------
#|																|
#|             Copyright 2023 - 2023, Amulya Paritosh			|
#|																|
#|  This file is part of Component Library Plugin for FreeCAD.	|
#|																|
#|               This file was created as a part of				|
#|              Google Summer Of Code Program - 2023			|
#|																|
# --------------------------------------------------------------

from typing import Any

from PySide6.QtCore import Signal

from src.data.factory import DataFactory

from ...api.local_api import LocalApi, LocalComponentQuery
from ...data import Component, DTypes, FileTypes
from ..page_manager import PageStates
from .base import ManagerInterface


class LocalStorageManager(ManagerInterface):
    component_loaded = Signal()
    api: LocalApi

    page_states = PageStates()

    def __init__(self) -> None:
        super().__init__()
        self.api = LocalApi()

    def request_components(self):
        """Method to request components from the API using the current query."""
        components = self.api.read()
        self.page_states.load_page(components)
        self.component_loaded.emit()  # Emit signal after components are loaded.

    def reload_page(self):
        return self.request_components()

    def load_from_db(self, dtype: DTypes):
        # Load data from the database based on the data type.
        match dtype:
            case DTypes.TAG:
                return DataFactory.load_many(self.api.get_tags(), dtype)

    def remove_file(self, component: Component, filetype: FileTypes):
        # Remove a file associated with a component.
        self.api.delete(component, filetype)
