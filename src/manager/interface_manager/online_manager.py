
# SPDX-License-Identifier: MIT
# --------------------------------------------------------------
#|																|
#|             Copyright 2023 - 2023, Amulya Paritosh			|
#|																|
#|  This file is part of Component Library Plugin for FreeCAD.	|
#|																|
#|               This file was created as a part of				|
#|              Google Summer Of Code Program - 2023			|
#|																|
# --------------------------------------------------------------

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
    component_loaded = Signal()
    api: CMSApi

    query: RepoComponentQuery = RepoComponentQuery()
    page_states = PageStates()

    def __init__(self) -> None:
        super().__init__()
        self.api = CMSApi()
        self.local = LocalApi()

    def request_components(self) -> CMSReply:
        reply: CMSReply = self.api.read(ComponentRequest(self.query))
        reply.finished.connect(self.__component_response_handler)
        return reply

    def reload_page(self) -> CMSReply:
        self.query.page = 1
        return self.request_components()

    def next_page(self) -> CMSReply:
        self.query.page = self.page_states.next_page
        return self.request_components()

    def prev_page(self) -> CMSReply:
        self.query.page = self.page_states.prev_page
        return self.request_components()

    def search(self, search_key: str) -> CMSReply:
        self.query.search_key = search_key
        return self.reload_page()

    def sort(self, /, by: str, order: str) -> CMSReply:
        self.query.sort_by = by
        self.query.sort_ord = order
        return self.reload_page()

    def filter(self, /, filetypes: list[str], tags: list[str]) -> CMSReply:
        self.query.file_types = filetypes
        self.query.tags = tags
        return self.reload_page()

    def download_component(self, component: Component, filetype: FileTypes) -> FileDownloader:
        file = component.files.get(filetype)
        if file is None:
            raise FileNotFoundError()

        component_path = self.local.component_path(component.metadata.name)

        component_downloader = FileDownloader(
            file.url,
            component_path,
            f"{component.metadata.name}.{file.type.value}",
        )

        if component.metadata.thumbnail and not any(
            path.match("thumbnail.*") for path in component_path.glob("thumbnail.*")
        ):
            FileDownloader(
                component.metadata.thumbnail,
                component_path,
                f"thumbnail{Path(component.metadata.thumbnail).suffix}",
            )

        self.local.create(component, filetype)

        return component_downloader

    def create_component(self, data: dict):
        multi_part = construct_multipart(data)

        if not multi_part:
            return

        request = ComponentRequest()
        request.setRawHeader("X-Access-Token".encode(), Config.GITHUB_ACCESS_TOKEN.encode())
        reply = self.api.create(request, multi_part)
        multi_part.setParent(reply)
        return reply

    @cache
    def load_from_db(self, dtype: DTypes):
        return DataFactory.load_many(DbDataLoader(dtype).data, dtype)

    @Slot(dict)
    def __component_response_handler(self, json_data: dict[str, Any]):
        self.page_states.load_page(json_data)
        self.query.page = self.page_states.page_no
        self.query.page_size = self.page_states.size
        self.component_loaded.emit()

    def remove_file(self, component: Component, filetype: FileTypes):
        self.local.delete(component, filetype)


class DbDataLoader:
    def __init__(self, dtype: DTypes) -> None:
        reply: CMSReply = CMSApi().read(QNetworkRequest(self.get_route(dtype)))
        loop = QEventLoop(parent=reply)
        reply.finished.connect(loop.quit)
        loop.exec()
        self.data: list = reply.data.get("items", [])

    @staticmethod
    def get_route(dtype: DTypes) -> str:
        match dtype:
            case DTypes.TAG:
                return "tag"
            case DTypes.LICENSE:
                return "license"
            case _:
                return ""
