from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from ...manager.component.api import BrowserManager
from ...manager.states import BrowserQueryStateManager, PageStateManager
from ..widgets import Overlay
from .ui import Ui_itemsView


class ItemsView(QWidget, Ui_itemsView):

	def __init__(self, manager: BrowserManager) -> None:
		super().__init__()

		# self.component_api_manager: Api = component_management_api
		# self.query_states = ComponentRequestState()
		# self.page_manager = PageStateManager(self)
		self.manager: BrowserManager = manager
		self.query_manager: BrowserQueryStateManager = self.manager.state.QueryManager
		self.page_manager: PageStateManager = self.manager.state.PageManager

		self.setupUi()
		self.setupSignals()

		self.show()
		self.initial_loads()


	def setupUi(self):
		super().setupUi(self)

		self.overlay = Overlay(self.scrollArea)
		self.fileTypeComboBox.make_pre_checked()


	def setupSignals(self):
		self.manager.component_loaded.connect(self.component_response_handler)
		self.manager.tags_loaded.connect(self.tags_list_response_handler)
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
		self.manager.get_tags()
		# reply: ApiReply = self.component_api_manager.get(QNetworkRequest("tag"))
		# reply.finished.connect(self.tags_list_response_handler)


	def get_request(self):
		self.overlay.show()
		# reply: ApiReply = self.component_api_manager.get(ComponentRequest(self.query_states))
		# reply.finished.connect(self.component_response_handler)
		self.manager.get_components()


	Slot()
	def component_response_handler(self):
		self.scrollAreaContentItemsWidget.repopulate(self.page_manager.page.data)
		self.pageLable.setText(f"{self.page_manager.page.page_no} / {self.page_manager.page.total_pages}")
		self.overlay.hide()


	Slot(list)
	def tags_list_response_handler(self, word_list: dict):
		# word_list: list[str] = [tag.get("label") for tag in json_data.get("items", [])]
		self.tagBar.set_suggestions(word_list)


	Slot()
	def search_enter_pressed(self):
		# self.query_states.search_key = self.searchLineEdit.text()
		# self.query_states.page = 1
		self.query_manager.set_search_key(self.searchLineEdit.text())
		self.get_request()


	Slot(str)
	def on_sortComboBox_change(self, value: str):
		# self.query_states.sort_by = value
		# self.query_states.page = 1
		self.query_manager.set_sort_by(value)
		self.get_request()


	Slot(str)
	def on_ordCombBox_change(self, value: str):
		# self.query_states.sort_ord = value
		# self.query_states.page = 1
		self.query_manager.set_sort_ord(value)
		self.get_request()


	Slot()
	def on_nextButton_clicked(self):
		# self.query_states.page = self.page_manager.next_page
		self.query_manager.set_page(self.page_manager.page.next_page)
		self.get_request()


	Slot()
	def on_prevButton_clicked(self):
		# self.query_states.page = self.page_manager.prev_page/
		self.query_manager.set_page(self.page_manager.page.prev_page)
		self.get_request()


	Slot(list)
	def on_fileTypeComboBox_change(self, checked_items: list[str]):
		# self.query_states.file_types = checked_items
		# self.query_states.page = 1
		self.query_manager.set_file_types(checked_items)
		self.get_request()

	Slot()
	def on_tagBar_tag_added(self, tags: list[str]):
		# self.query_states.tags = tags
		# self.query_states.page = 1
		self.query_manager.set_tags(tags)
		self.get_request()
