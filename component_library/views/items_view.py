import json

from PySide6.QtCore import Slot
from PySide6.QtNetwork import QNetworkReply
from PySide6.QtWidgets import QWidget

from ..api import (ComponentRequestManager, PageManager,
                   component_management_api)
from .ui import Ui_itemsView


class ItemsView(QWidget, Ui_itemsView):

	def __init__(self) -> None:
		super().__init__()
		self.setupUi()

		self.api_manager = component_management_api
		self.api_manager.finished.connect(self.response_handler)

		self.pagemanager = PageManager(self)
		self.pagemanager.enable_next.connect(self.nextButton.setEnabled)
		self.pagemanager.enable_prev.connect(self.prevButton.setEnabled)

		ComponentRequestManager.set_pagination(self.pagemanager)
		self.api_manager.get(ComponentRequestManager.request())

		self.show()

	def setupUi(self):
		super().setupUi(self)
		self.searchLineEdit.returnPressed.connect(self.search_enter_pressed)
		self.nextButton.clicked.connect(self.nextButton_clicked)
		self.prevButton.clicked.connect(self.prevButton_clicked)


	def response_handler(self, reply: QNetworkReply):
		if reply.error() != QNetworkReply.NetworkError.NoError:
			print(f"Error : {reply.errorString()}")

		data = reply.readAll().data().decode("utf-8")

		try:
			json_data: dict = json.loads(data)
		except json.decoder.JSONDecodeError:
			json_data = dict()

		self.pagemanager.load_page(json_data)
		self.scrollAreaContentItemsWidget.repopulate(self.pagemanager.data)

	Slot()
	def search_enter_pressed(self):
		ComponentRequestManager.set_search_key(self.searchLineEdit.text())
		self.pagemanager.to_begining()
		ComponentRequestManager.set_pagination(self.pagemanager)
		self.api_manager.get(ComponentRequestManager.request())


	Slot()
	def nextButton_clicked(self):
		ComponentRequestManager.set_next_page_pagination(self.pagemanager)
		self.api_manager.get(ComponentRequestManager.request())

	Slot()
	def prevButton_clicked(self):
		ComponentRequestManager.set_prev_page_pagination(self.pagemanager)
		self.api_manager.get(ComponentRequestManager.request())
