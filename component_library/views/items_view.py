import json

from PySide6.QtCore import Slot
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkReply
from PySide6.QtWidgets import QWidget

from ..api import ComponentRequest, component_management_api
from .ui import Ui_itemsView


class ItemsView(QWidget, Ui_itemsView):

	def __init__(self) -> None:
		super().__init__()
		self.setupUi(self)
		self.setupView()

		self.network_manager = QNetworkAccessManager()
		self.network_manager.finished.connect(self.response_handler)

		self.api = component_management_api

		initial_request = ComponentRequest(self.api)
		self.network_manager.get(initial_request.request())

		self.current_page_data = []

		self.show()

	def response_handler(self, reply: QNetworkReply):
		if reply.error() != QNetworkReply.NetworkError.NoError:
			print(f"Error : {reply.errorString()}")

		data = reply.readAll().data().decode("utf-8")

		try:
			json_data: dict = json.loads(data)
		except json.decoder.JSONDecodeError:
			json_data = dict()

		self.current_page_data = json_data.get("items", [])
		self.scrollAreaContentItemsWidget.repopulate(self.current_page_data)

	def setupView(self):
		self.searchLineEdit.returnPressed.connect(self.search_enter_pressed)
		pass


	Slot()
	def search_enter_pressed(self):
		request = ComponentRequest(self.api)
		request.add_search_key(self.searchLineEdit.text())
		self.network_manager.get(request.request())
