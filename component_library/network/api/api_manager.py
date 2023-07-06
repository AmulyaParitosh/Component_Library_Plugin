from os import path

from PySide6.QtCore import QObject, QUrl
from PySide6.QtNetwork import (QNetworkAccessManager, QNetworkRequest,
                               QSslConfiguration)

from .replies import ApiReply


class Api(QObject):

	def __init__(self, base_url: str, manager: QNetworkAccessManager, ssl_config: QSslConfiguration) -> None:
		super().__init__()
		self.manager: QNetworkAccessManager = manager
		self.base_url: str = path.join(base_url, "api")
		self.ssl_config: QSslConfiguration = ssl_config

	def prepare_api_request(self, request: QNetworkRequest):
		absolute_path: str = path.join(self.base_url, request.url().toString())
		absolute_url: QUrl = QUrl.fromUserInput(absolute_path)
		request.setUrl(absolute_url)
		request.setSslConfiguration(self.ssl_config)

	def get(self, request: QNetworkRequest) -> ApiReply:
		self.prepare_api_request(request)
		return ApiReply(self.manager.get(request), self)

	def post(self, request: QNetworkRequest, data: bytes) -> ApiReply:
		self.prepare_api_request(request)
		return ApiReply(self.manager.post(request, data), self)

	def put(self, request: QNetworkRequest, data: bytes) -> ApiReply:
		self.prepare_api_request(request)
		return ApiReply(self.manager.put(request, data), self)


def getApi(api_url: str, manager: QNetworkAccessManager, ssl_config: QSslConfiguration) -> Api:
	return Api(api_url, manager, ssl_config)
