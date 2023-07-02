from PySide6.QtCore import Slot
from PySide6.QtNetwork import QNetworkRequest
from PySide6.QtWidgets import QWidget

from ..components import Overlay
from ..network import (ApiManager, ApiReply, ComponentRequest,
                       ComponentRequestState, component_management_api)
from .page import PageManager
from .ui import Ui_itemsView


class ItemsView(QWidget, Ui_itemsView):

	def __init__(self) -> None:
		super().__init__()

		self.component_api_manager: ApiManager = component_management_api
		self.query_states = ComponentRequestState()
		self.page_manager = PageManager(self)

		self.setupUi()
		self.setupSignals()

		self.show()

		self.initial_loads()


	def setupUi(self):
		super().setupUi(self)

		self.overlay = Overlay(self.scrollArea)
		self.fileTypeComboBox.make_pre_checked()


	def setupSignals(self):
		self.page_manager.enable_next.connect(self.nextButton.setEnabled)
		self.page_manager.enable_prev.connect(self.prevButton.setEnabled)
		self.searchLineEdit.returnPressed.connect(self.search_enter_pressed)
		self.nextButton.clicked.connect(self.on_nextButton_clicked)
		self.prevButton.clicked.connect(self.on_prevButton_clicked)
		self.sortComboBox.currentTextChanged.connect(self.on_sortComboBox_change)
		self.orderComboBox.currentTextChanged.connect(self.on_ordCombBox_change)
		self.fileTypeComboBox.itemChecked.connect(self.on_fileTypeComboBox_change)
		self.tagBar.tag_added.connect(self.on_tagBar_tag_added)


	def initial_loads(self):
		self.get_request()
		reply: ApiReply = self.component_api_manager.get(QNetworkRequest("tag"))
		reply.finished.connect(self.tags_list_response_handler)


	def get_request(self):
		self.overlay.show()
		reply: ApiReply = self.component_api_manager.get(ComponentRequest(self.query_states))
		reply.finished.connect(self.component_response_handler)


	Slot(dict)
	def component_response_handler(self, json_data: dict):
		self.page_manager.load_page(json_data)
		self.query_states.page = self.page_manager.page
		self.query_states.page_size = self.page_manager.size
		self.scrollAreaContentItemsWidget.repopulate(self.page_manager.data)
		self.pageLable.setText(f"{self.page_manager.page} / {self.page_manager.total_pages}")
		self.overlay.hide()


	Slot(dict)
	def tags_list_response_handler(self, json_data: dict):
		word_list: list[str] = [tag.get("label") for tag in json_data.get("items", [])]
		self.tagBar.set_suggestions(word_list)


	Slot()
	def search_enter_pressed(self):
		self.query_states.search_key = self.searchLineEdit.text()
		self.query_states.page = 1
		self.get_request()


	Slot(str)
	def on_sortComboBox_change(self, value: str):
		self.query_states.sort_by = value
		self.query_states.page = 1
		self.get_request()


	Slot(str)
	def on_ordCombBox_change(self, value: str):
		self.query_states.sort_ord = value
		self.query_states.page = 1
		self.get_request()


	Slot()
	def on_nextButton_clicked(self):
		self.query_states.page = self.page_manager.next_page
		self.get_request()


	Slot()
	def on_prevButton_clicked(self):
		self.query_states.page = self.page_manager.prev_page
		self.get_request()


	Slot(list)
	def on_fileTypeComboBox_change(self, checked_items: list[str]):
		self.query_states.file_types = checked_items
		self.query_states.page = 1
		self.get_request()

	Slot()
	def on_tagBar_tag_added(self, tags: list[str]):
		self.query_states.tags = tags
		self.query_states.page = 1
		self.get_request()
