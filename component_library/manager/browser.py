from typing import Any

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtNetwork import QNetworkRequest

from ..data import DTypes
from ..network import network_access_manager, sslConfig
from ..network.api import Api, ApiReply, ComponentRequest, getApi
from .page import Page
from .queries import ComponenetQueryParameters


class BrowserManager(QObject):
	component_loaded = Signal()

	def __init__(self, api_url: str) -> None:
		super().__init__()
		self.api: Api = getApi(api_url, network_access_manager, sslConfig)
		self.query = ComponenetQueryParameters()
		self.page = Page()

	def reload_page(self):
		return self.request_components()

	def next_page(self):
		self.query.page = self.page.next_page
		return self.request_components()

	def prev_page(self):
		self.query.page = self.page.prev_page
		return self.request_components()


	def request_components(self):
		reply: ApiReply = self.api.get(ComponentRequest(self.query))
		reply.finished.connect(self.__component_response_handler)
		return reply


	def request_tags(self):
		reply: ApiReply = self.api.get(QNetworkRequest("tag"))
		return reply


	Slot(dict)
	def __component_response_handler(self, json_data: dict[str, Any]):
		page: Page = self.page.load_page(json_data, DTypes.COMPONENT)
		self.query.page = page.page_no
		self.query.page_size = page.size
		self.component_loaded.emit()
