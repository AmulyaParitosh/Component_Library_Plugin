from typing import Any

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtNetwork import QNetworkRequest

from ..data import DTypes
from ..network import network_access_manager, sslConfig
from ..network.api import Api, ApiReply, ComponentRequest, getApi
from .page import Page, PageManager
from .query import ComponentQueryManager


class BrowserManager(QObject):
	component_loaded = Signal()
	tags_loaded = Signal(list)
	license_loaded = Signal(str)
	files_loaded = Signal(dict)


	def __init__(self, api_url: str) -> None:
		super().__init__()
		self.api: Api = getApi(api_url, network_access_manager, sslConfig)
		# self.state: StateManager = state_manager
		self.query_manager = ComponentQueryManager()
		self.page_manager = PageManager()

	def next_page(self):
		self.query_manager.set_next_page(self.page_manager.page)
		self.request_components()

	def prev_page(self):
		self.query_manager.set_prev_page(self.page_manager.page)
		self.request_components()


	def request_components(self):
		reply: ApiReply = self.api.get(ComponentRequest(self.query_manager.query_states))
		reply.finished.connect(self.__component_response_handler)
		# TODO custom signals are beinf user, try returning thjre reply and search if multiple slots can be added to a signal


	def request_tags(self):
		reply: ApiReply = self.api.get(QNetworkRequest("tag"))
		reply.finished.connect(self.__tags_list_response_handler)


	def request_files(self, metadata_id: str):
		reply = self.api.get(QNetworkRequest(f"metadata/{metadata_id}/files"))
		reply.finished.connect(self.__get_files)


	Slot(dict)
	def __component_response_handler(self, json_data: dict[str, Any]):
		page: Page = self.page_manager.load_page(json_data, DTypes.COMPONENT)
		self.query_manager.set_page(page.page_no)
		self.query_manager.set_page_size(page.size)
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
