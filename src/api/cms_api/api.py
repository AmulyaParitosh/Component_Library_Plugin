from functools import cache
from os import path

from PySide6.QtCore import QObject, QUrl
from PySide6.QtNetwork import QNetworkRequest

from ...network import get_network_access_manager
from .replies import CMSReply


class CMSApi(QObject):
	network_access_manager, sslConfig = get_network_access_manager()

	def __init__(self, base_url: str) -> None:
		super().__init__()
		self.base_url: str = path.join(base_url, "api")

	def prepare_api_request(self, request: QNetworkRequest):
		absolute_path: str = path.join(self.base_url, request.url().toString())
		absolute_url: QUrl = QUrl.fromUserInput(absolute_path)
		request.setUrl(absolute_url)
		request.setSslConfiguration(self.sslConfig)

	def get(self, request: QNetworkRequest) -> CMSReply:
		self.prepare_api_request(request)
		return CMSReply(self.network_access_manager.get(request), self)

	def post(self, request: QNetworkRequest, data: bytes) -> CMSReply:
		self.prepare_api_request(request)
		return CMSReply(self.network_access_manager.post(request, data), self)

	def put(self, request: QNetworkRequest, data: bytes) -> CMSReply:
		self.prepare_api_request(request)
		return CMSReply(self.network_access_manager.put(request, data), self)

@cache
def getApi(api_url: str) -> CMSApi:
	return CMSApi(api_url)
