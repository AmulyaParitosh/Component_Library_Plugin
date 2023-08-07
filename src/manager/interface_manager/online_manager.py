from functools import cache
from pathlib import Path
from typing import Any

from PySide6.QtCore import QEventLoop, Signal, Slot
from PySide6.QtNetwork import QNetworkRequest

from ...api.cms_api import (CMSApi, CMSReply, ComponentRequest,
                            RepoComponentQuery, construct_multipart)
from ...api.local_api import LocalApi
from ...config import Config
from ...data import Component, DataFactory, DTypes, FileTypes
from ..download_manager import FileDownloader
from ..page_manager import PageStates
from .base import ManagerInterface


class OnlineRepoManager(ManagerInterface):
    # A manager class for an online repository.

    component_loaded = Signal()
    api : CMSApi

    query: RepoComponentQuery = RepoComponentQuery()
    page_states = PageStates()

    def __init__(self) -> None:
        super().__init__()
        self.api = CMSApi()
        self.local = LocalApi()

    def request_components(self) -> CMSReply:
        """Method to request components from the API using the current query."""
        reply: CMSReply = self.api.read(ComponentRequest(self.query))
        reply.finished.connect(self.__component_response_handler)
        return reply

    def reload_page(self) -> CMSReply:
        """Method to reload the current page of components."""
        self.query.page = 1
        return self.request_components()

    def next_page(self) -> CMSReply:
        """Method to load the next page of components."""
        self.query.page = self.page_states.next_page
        return self.request_components()

    def prev_page(self) -> CMSReply:
        """Method to load the previous page of components."""
        self.query.page = self.page_states.prev_page
        return self.request_components()

    def search(self, search_key: str) -> CMSReply:
        """Method to search for components using the given search_key."""
        self.query.search_key = search_key
        return self.reload_page()

    def sort(self, /, by: str, order: str) -> CMSReply:
        """Method to sort components based on the given criteria."""
        self.query.sort_by = by
        self.query.sort_ord = order
        return self.reload_page()

    def filter(self, /, filetypes: list[str], tags: list[str]) -> CMSReply:
        """Method to filter components based on filetypes and tags."""
        self.query.file_types = filetypes
        self.query.tags = tags
        return self.reload_page()

    def download_component(self, component: Component, filetype: FileTypes) -> FileDownloader:
        """Method to download a component file from the repository."""
        file = component.files.get(filetype)
        if file is None:
            raise FileNotFoundError()

        # Get the path for saving the downloaded component and its thumbnail (if available)
        component_path = self.local.component_path(component.metadata.name)

        # Create a FileDownloader to download the main component file
        component_downloader = FileDownloader(
            file.url,
            component_path,
            f"{component.metadata.name}.{file.type.value}",
        )

        # If the component has a thumbnail and it is not already present in the component directory,
        # download the thumbnail file as well
        if component.metadata.thumbnail and not any(
            path.match("thumbnail.*") for path in component_path.glob("thumbnail.*")
        ):
            FileDownloader(
                component.metadata.thumbnail,
                component_path,
                f"thumbnail{Path(component.metadata.thumbnail).suffix}",
            )

        # Create a local record for the downloaded component
        self.local.create(component, filetype)

        return component_downloader

    def create_component(self, data: dict):
        """Method to create a new component using the provided data."""
        # Create a multipart request using the provided data
        multi_part = construct_multipart(data)

        # If the multipart request is empty, return immediately
        if not multi_part:
            return

        # Create a ComponentRequest with the necessary headers and send the multipart request to the API
        request = ComponentRequest()
        request.setRawHeader("X-Access-Token".encode(), Config.GITHUB_ACCESS_TOKEN.encode())
        reply = self.api.create(request, multi_part)
        multi_part.setParent(reply)
        return reply

    @cache
    def load_from_db(self, dtype: DTypes):
        """Method to load data from the local database for the specified dtype."""
        # Create a DbDataLoader instance to fetch data from the API
        return DataFactory.load_many(DbDataLoader(dtype).data, dtype)

    @Slot(dict)
    def __component_response_handler(self, json_data: dict[str, Any]):
        """Slot to handle the response from the API when components are loaded."""
        # Load the received JSON data into the PageStates object to update the page information
        page: PageStates = self.page_states.load_page(json_data)

        # Update the query's page and page_size based on the received page information
        self.query.page = page.page_no
        self.query.page_size = page.size

        # Emit the component_loaded signal to notify other parts of the application that components are loaded
        self.component_loaded.emit()


class DbDataLoader:
    # A class to load data from the database.

    def __init__(self, dtype: DTypes) -> None:
        reply: CMSReply = CMSApi().read(QNetworkRequest(self.get_route(dtype)))
        loop = QEventLoop(parent=reply)
        reply.finished.connect(loop.quit)
        loop.exec()
        self.data: list = reply.data.get("items", [])

    @staticmethod
    def get_route(dtype: DTypes) -> str:
        """Method to get the API route based on the dtype."""
        match dtype:
            case DTypes.TAG:
                return "tag"
            case DTypes.LICENSE:
                return "license"
            case _:
                return ""
