from typing import Any

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtNetwork import QNetworkRequest

from ...network import network_access_manager, sslConfig
from ...network.api import Api, ApiReply, ComponentRequest, getApi
from ..states import BrowserQueryStateManager, PageState, PageStateManager


class StateManager:
	QueryManager = BrowserQueryStateManager()
	PageManager = PageStateManager()


class BrowserManager(QObject):
	component_loaded = Signal()
	tags_loaded = Signal(list)

	def __init__(self, api_url: str, state_manager: StateManager) -> None:
		self.api: Api = getApi(api_url, network_access_manager, sslConfig)
		self.state: StateManager = state_manager


	def get_components(self):
		reply: ApiReply = self.api.get(ComponentRequest(self.state.QueryManager.query_states))
		reply.finished.connect(self.__component_response_handler)


	def get_tags(self):
		reply: ApiReply = self.api.get(QNetworkRequest("tag"))
		reply.finished.connect(self.__tags_list_response_handler)


	Slot(dict)
	def __component_response_handler(self, json_data: dict[str, Any]):
		page: PageState = self.state.PageManager.load_page(json_data)
		self.state.QueryManager.set_page(page.page_no)
		self.state.QueryManager.set_page_size(page.size)
		self.component_loaded.emit()


	Slot(dict)
	def __tags_list_response_handler(self, json_data: dict):
		word_list: list[str] = [tag.get("label") for tag in json_data.get("items", [])]
		self.tags_loaded.emit(word_list)
