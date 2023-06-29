from os import path

from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtCore import QObject

from .replies import ApiReply

network_access_manager = QNetworkAccessManager()


class ApiManager(QObject):

	def __init__(self, base_url: str) -> None:
		super().__init__()
		self.manager: QNetworkAccessManager = network_access_manager
		self.base_url: str = path.join(base_url, "api")

	def make_absolutepath(self, request: QNetworkRequest):
		absolute_path: str = path.join(self.base_url, request.url().toString())
		print(f"{absolute_path=}")
		request.setUrl(absolute_path)

	def get(self, request: QNetworkRequest) -> ApiReply:
		self.make_absolutepath(request)
		return ApiReply(self.manager.get(request), self)

	def post(self, request: QNetworkRequest, data: bytes) -> ApiReply:
		self.make_absolutepath(request)
		return ApiReply(self.manager.post(request, data), self)

	def put(self, request: QNetworkRequest, data: bytes) -> ApiReply:
		self.make_absolutepath(request)
		return ApiReply(self.manager.put(request, data), self)


component_management_api = ApiManager("http://127.0.0.1:5000")
