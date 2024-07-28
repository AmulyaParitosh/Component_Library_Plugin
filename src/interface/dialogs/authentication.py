import json
from urllib.parse import parse_qs, urlparse

import dotenv
from PySide2.QtCore import QUrl, Signal
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QDialog, QVBoxLayout

from ...config import config


class Authentication_Dialog(QDialog):
    auth_complete = Signal(str)
    auth_scope: str = "public_repo"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("GitHub OAuth Login")
        self.setGeometry(100, 100, 800, 600)

        self.web_view = QWebEngineView()
        self.web_view.loadFinished.connect(self.handleLoadFinished)

        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        self.setLayout(layout)

        self.load_html = False

        self.start_github_oauth()

    def start_github_oauth(self):
        self.web_view.setUrl(
            QUrl(
                f"https://github.com/login/oauth/authorize?client_id={config.GITHUB_OAUTH_CLIENT_ID}&scope={self.auth_scope}"
            )
        )

    def handleLoadFinished(self, ok):
        curr_url = self.web_view.page().url()
        query = parse_qs(urlparse(curr_url.toString()).query)

        if ok and (curr_url.hasQuery()) and ("code" in query):
            self.web_view.page().runJavaScript(
                "document.documentElement.outerHTML", 0, self.handleHtml
            )

    def handleHtml(self, html: str):
        json_str = html.removeprefix(
            '<html><head><meta name="color-scheme" content="light dark"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">'
        ).removesuffix("</pre></body></html>")

        response_data: dict = json.loads(json_str)

        config.GITHUB_ACCESS_TOKEN = response_data.get("auth_token", "")
        dotenv.set_key(".env", "GITHUB_ACCESS_TOKEN", config.GITHUB_ACCESS_TOKEN)

        config.JWT_TOKEN = response_data.get("jwt", "")

        self.auth_complete.emit(config.GITHUB_ACCESS_TOKEN)

        self.web_view.deleteLater()
        self.deleteLater()
