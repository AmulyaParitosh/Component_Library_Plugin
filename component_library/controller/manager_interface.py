from typing import Any

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtNetwork import QNetworkRequest

from ..data import DTypes
from ..network import network_access_manager, sslConfig
from ..network.api import Api, ApiReply, ComponentRequest, getApi
from ..utils import Interface
from .page import PageStates
from .query import ComponentQueryInterface, RepoComponentQuery


class ManagerInterface(Interface):
	component_loaded: Signal

	api: Any # TODO change type of api to APIInterface
	page_states: PageStates
	query: ComponentQueryInterface

	def reload_page(self):
		raise NotImplementedError

	def next_page(self):
		raise NotImplementedError

	def prev_page(self):
		raise NotImplementedError

	def search(self, search_key: str):
		raise NotImplementedError

	def sort(self, /, by: str, order: str):
		# TODO make ENums for by and order
		raise NotImplementedError

	def filter(self,/ , filetypes: list[str], tags: list[str]):
		# TODO replace typehint of filetypes & tags with enum
		raise NotImplementedError



class OnlineRepoManager(QObject):
	component_loaded = Signal()

	query = RepoComponentQuery()
	page_states = PageStates()

	def __init__(self, api_url: str) -> None:
		super().__init__()
		self.api: Api = getApi(api_url, network_access_manager, sslConfig)

	def reload_page(self):
		self.query.page = 1
		return self.request_components()

	def next_page(self):
		self.query.page = self.page_states.next_page
		return self.request_components()

	def prev_page(self):
		self.query.page = self.page_states.prev_page
		return self.request_components()

	def search(self, search_key: str):
		self.query.search_key = search_key
		return self.reload_page()

	def sort(self, /, by: str, order: str):
		self.query.sort_by = by
		self.query.sort_ord = order
		return self.reload_page()

	def filter(self,/ , filetypes: list[str], tags: list[str]):
		self.query.file_types = filetypes
		self.query.tags = tags
		return self.reload_page()


	def request_components(self):
		reply: ApiReply = self.api.get(ComponentRequest(self.query))
		reply.finished.connect(self.__component_response_handler)
		return reply


	def request_tags(self):
		reply: ApiReply = self.api.get(QNetworkRequest("tag"))
		return reply


	Slot(dict)
	def __component_response_handler(self, json_data: dict[str, Any]):
		page: PageStates = self.page_states.load_page(json_data, DTypes.COMPONENT)
		self.query.page = page.page_no
		self.query.page_size = page.size
		self.component_loaded.emit()


class LocalStorageManager(QObject):...
