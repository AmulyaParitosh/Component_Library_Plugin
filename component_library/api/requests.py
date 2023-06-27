from copy import copy
import queue
from PySide6.QtCore import QUrl, QUrlQuery
from PySide6.QtNetwork import QNetworkRequest

from .utils import PageManager

class ComponentRequest(QNetworkRequest):

	def __init__(self, url: QUrl, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setUrl(url)


class ComponentRequestManager:
	url = QUrl("component")
	query = QUrlQuery()

	@classmethod
	def request(cls) -> ComponentRequest:
		cls.url.setQuery(copy(cls.query))
		cls.query.clear()
		return ComponentRequest(cls.url)

	@classmethod
	def set_search_key(cls, search_key: str):
		cls.query.addQueryItem("search_key", search_key)

	@classmethod
	def set_pagination(cls, page_manager: PageManager):
		cls.query.addQueryItem("page", str(page_manager.page))
		cls.query.addQueryItem("page_size", str(page_manager.size))

	@classmethod
	def set_next_page_pagination(cls, page_manager: PageManager):
		cls.query.addQueryItem("page", str(page_manager.next_page))
		cls.query.addQueryItem("page_size", str(page_manager.size))

	@classmethod
	def set_prev_page_pagination(cls, page_manager: PageManager):
		cls.query.addQueryItem("page", str(page_manager.prev_page))
		cls.query.addQueryItem("page_size", str(page_manager.size))
