from PySide6.QtCore import Signal

from ...api.local_api import LocalApi, LocalComponentQuery
from ..page_manager import PageStates
from .base import ManagerInterface


class LocalStorageManager(ManagerInterface):
    component_loaded = Signal()
    api : LocalApi

    # query : LocalComponentQuery = LocalComponentQuery()
    page_states = PageStates()

    def request_components(self):
        """Method to request components from the API using the current query."""
        components = self.api.read()
        # reply: CMSReply = self.api.read(ComponentRequest(self.query))
        # reply.finished.connect(self.__component_response_handler)
        # return reply

    def reload_page(self):
        return super().reload_page()
