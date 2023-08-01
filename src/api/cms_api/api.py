from functools import cache
from typing import Any

from PySide6.QtCore import QUrl
from PySide6.QtNetwork import QNetworkRequest

from src.config.config import Config

from ...network import get_network_access_manager
from ..base_api import ApiInterface
from .replies import CMSReply


# API interface class that implements CRUD operations using QNetworkAccessManager
class CMSApi(ApiInterface):
    network_access_manager, sslConfig = get_network_access_manager()

    BASEURL: str = Config.API_URL + '/api'

    def __init__(self) -> None:
        super().__init__()

    # Method to prepare the API request by setting the absolute path and SSL configuration
    def prepare_api_request(self, request: QNetworkRequest):
        absolute_path: str = f'{self.BASEURL}/{request.url().toString()}'
        request.setUrl(QUrl.fromUserInput(absolute_path))
        request.setSslConfiguration(self.sslConfig)

    # Method to perform a read operation on the API
    def read(self, request: QNetworkRequest) -> CMSReply:
        self.prepare_api_request(request)
        return CMSReply(self.network_access_manager.get(request), self)

    # Method to perform a create operation on the API
    def create(self, request: QNetworkRequest, data: Any) -> CMSReply:
        self.prepare_api_request(request)
        return CMSReply(self.network_access_manager.post(request, data), self)

    # Method to perform an update operation on the API
    def update(self, request: QNetworkRequest, data: bytes) -> CMSReply:
        self.prepare_api_request(request)
        return CMSReply(self.network_access_manager.put(request, data), self)

    # Method to perform a delete operation on the API
    def delete(self, request: QNetworkRequest) -> CMSReply:
        self.prepare_api_request(request)
        return CMSReply(self.network_access_manager.deleteResource(request), self)


# Cache decorator ensures that the function result is cached for subsequent calls with the same arguments
@cache
def getApi() -> CMSApi:
    # This function returns an instance of CMSApi, using caching to store the result
    return CMSApi()
    # TODO apply singleton with
    # _instance = None
    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance
