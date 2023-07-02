from os import path

from PySide6.QtCore import QObject, QUrl
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest

from ..network_manager import network_access_manager, sslConfig
from .replies import ApiReply


class ApiManager(QObject):

	def __init__(self, base_url: str) -> None:
		super().__init__()
		self.manager: QNetworkAccessManager = network_access_manager
		self.base_url: str = path.join(base_url, "api")

	def prepare_api_request(self, request: QNetworkRequest):
		absolute_path: str = path.join(self.base_url, request.url().toString())
		absolute_url: QUrl = QUrl.fromUserInput(absolute_path)
		request.setUrl(absolute_url)
		request.setSslConfiguration(sslConfig)

	def get(self, request: QNetworkRequest) -> ApiReply:
		self.prepare_api_request(request)
		return ApiReply(self.manager.get(request), self)

	def post(self, request: QNetworkRequest, data: bytes) -> ApiReply:
		self.prepare_api_request(request)
		return ApiReply(self.manager.post(request, data), self)

	def put(self, request: QNetworkRequest, data: bytes) -> ApiReply:
		self.prepare_api_request(request)
		return ApiReply(self.manager.put(request, data), self)


component_management_api = ApiManager("http://127.0.0.1:5000")
