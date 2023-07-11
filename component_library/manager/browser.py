from typing import Any

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtNetwork import QNetworkRequest

from ..network import network_access_manager, sslConfig
from ..network.api import Api, ApiReply, ComponentRequest, getApi
from .page import PageState, PageStateManager
from .query import ComponentQueryStateManager
from ..data import DataFactory, DTypes


class StateManager:
	QueryManager = ComponentQueryStateManager()
	PageManager = PageStateManager()


class BrowserManager(QObject):
	component_loaded = Signal()
	tags_loaded = Signal(list)
	license_loaded = Signal(str)
	files_loaded = Signal(dict)


	def __init__(self, api_url: str, state_manager: StateManager) -> None:
		super().__init__()
		self.api: Api = getApi(api_url, network_access_manager, sslConfig)
		self.state: StateManager = state_manager

	def next_page(self):
		self.state.QueryManager.set_next_page(self.state.PageManager.page)
		self.request_components()

	def prev_page(self):
		self.state.QueryManager.set_prev_page(self.state.PageManager.page)
		self.request_components()


	def request_components(self):
		reply: ApiReply = self.api.get(ComponentRequest(self.state.QueryManager.query_states))
		reply.finished.connect(self.__component_response_handler)
		# TODO custom signals are beinf user, try returning thjre reply and search if multiple slots can be added to a signal


	def request_tags(self):
		reply: ApiReply = self.api.get(QNetworkRequest("tag"))
		reply.finished.connect(self.__tags_list_response_handler)


	# def request_license(self, license_id: str):
	# 	reply = self.api.get(QNetworkRequest(f"license/{license_id}"))
	# 	reply.finished.connect(self.__got_license)


	def request_files(self, metadata_id: str):
		reply = self.api.get(QNetworkRequest(f"metadata/{metadata_id}/files"))
		reply.finished.connect(self.__get_files)


	Slot(dict)
	def __component_response_handler(self, json_data: dict[str, Any]):
		page: PageState = self.state.PageManager.load_page(json_data, DTypes.COMPONENT)
		self.state.QueryManager.set_page(page.page_no)
		self.state.QueryManager.set_page_size(page.size)
		self.component_loaded.emit()


	Slot(dict)
	def __tags_list_response_handler(self, json_data: dict):
		word_list: list[str] = [tag.get("label") for tag in json_data.get("items", [])]
		self.tags_loaded.emit(word_list)


	Slot(dict)
	def __got_license(self, json_data: dict):
		self.license_loaded.emit(json_data.get("fullname", "None"))


	Slot(dict)
	def __get_files(self, json_data: dict):
		self.files_loaded.emit(json_data)
