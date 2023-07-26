from functools import cache
from os import path
from typing import Any

from PySide6.QtCore import QUrl
from PySide6.QtNetwork import QNetworkRequest

from ...network import get_network_access_manager
from ..base_api import ApiInterface
from .replies import CMSReply


class CMSApi(ApiInterface):
	network_access_manager, sslConfig = get_network_access_manager()

	def __init__(self, base_url: str) -> None:
		super().__init__()
		self.base_url: str = path.join(base_url, "api")

	def prepare_api_request(self, request: QNetworkRequest):
		absolute_path: str = path.join(self.base_url, request.url().toString())
		request.setUrl(QUrl.fromUserInput(absolute_path))
		request.setSslConfiguration(self.sslConfig)

	def read(self, request: QNetworkRequest) -> CMSReply:
		self.prepare_api_request(request)
		return CMSReply(self.network_access_manager.get(request), self)

	def create(self, request: QNetworkRequest, data: Any) -> CMSReply:
		self.prepare_api_request(request)
		return CMSReply(self.network_access_manager.post(request, data), self)

	def update(self, request: QNetworkRequest, data: bytes) -> CMSReply:
		self.prepare_api_request(request)
		return CMSReply(self.network_access_manager.put(request, data), self)

	def delete(self, request: QNetworkRequest) -> CMSReply:
		self.prepare_api_request(request)
		return CMSReply(self.network_access_manager.deleteResource(request), self)


@cache
def getApi(api_url: str) -> CMSApi:
	return CMSApi(api_url)
