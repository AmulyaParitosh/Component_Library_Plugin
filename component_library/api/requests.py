from os import path

from PySide6.QtNetwork import QNetworkRequest

from .component_management_system import Api


class ComponentQueryState:...



class ComponentRequest(QNetworkRequest):

	def __init__(self, api: Api, *args, **kwargs):
		self._api = api
		self._api.setUrl(path.join(self._api.url(), "component"))
		super().__init__(*args, **kwargs)

	def add_search_key(self, search_key: str):
		self._api.addQueryParameter("search_key", search_key)

	def request(self):
		self.setUrl(self._api.url())
		return self
