import json
from typing import Optional

import dotenv
from PySide2.QtCore import QObject, Signal
from PySide2.QtNetwork import QNetworkRequest


from ..config import Config
from ..data import User
from ..logging import logger
from ..interface.dialogs.authentication import Authentication_Dialog
from .network_manager import get_network_access_manager


class Authentication_Manager(QObject):
    user: Optional[User] = None
    session_update = Signal()

    network_manager, sslConfig = get_network_access_manager()

    def __init__(self) -> None:
        super().__init__()
        if not Config.GITHUB_ACCESS_TOKEN:
            return

        self.api_login()

    def api_login(self):
        request: QNetworkRequest = QNetworkRequest(
            f"{Config.API_URL}/login/app/authorize"
        )
        request.setRawHeader(
            "access_token".encode("utf-8"),
            str(Config.GITHUB_ACCESS_TOKEN).encode("utf-8"),
        )
        self.jwt_auth_reply = self.network_manager.get(request)
        self.jwt_auth_reply.finished.connect(self.handle_jwt_auth_response)

        self.get_user_data(Config.GITHUB_ACCESS_TOKEN)

    def handle_jwt_auth_response(self):
        raw_json_str = self.jwt_auth_reply.readAll().data().decode("utf-8")
        jwt_token = json.loads(raw_json_str)["jwt"]
        Config.JWT_TOKEN = jwt_token

        logger.debug(f"{jwt_token=}")

    def login(self) -> None:
        dialog = Authentication_Dialog()
        dialog.auth_complete.connect(self.get_user_data)
        dialog.exec()

    def logout(self) -> None:
        self.user = None
        dotenv.unset_key(".env", "GITHUB_ACCESS_TOKEN")
        Config.GITHUB_ACCESS_TOKEN = None
        self.session_update.emit(self.session_update)

    def is_authentic(self) -> bool:
        return self.user is not None

    def get_user_data(self, access_token: str):
        if not access_token:
            raise ValueError("The request token has to be supplied!")

        # url = QUrl("https://api.github.com/user")
        # user_data_request = QNetworkRequest(url)
        user_data_request = QNetworkRequest("https://api.github.com/user")
        user_data_request.setRawHeader(
            b"Authorization", f"token {access_token}".encode()
        )
        self.user_data_reply = self.network_manager.get(user_data_request)
        self.user_data_reply.finished.connect(self.handle_user_data_response)

    def handle_user_data_response(self):
        raw_json_str = self.user_data_reply.readAll().data().decode("utf-8")
        user_data = json.loads(raw_json_str)

        self.user = User(
            username=user_data["login"],
            name=user_data["name"],
            email=user_data["email"],
            avatar_url=user_data["avatar_url"],
            components=[],
        )
        self.session_update.emit()

        logger.debug(f"{self.user=}")
