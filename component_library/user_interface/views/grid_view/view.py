from PySide6.QtCore import Slot

from ....manager import BrowserManager, Page
from ...widgets.overlay import LoadingOverlay
from ..base_view import BaseView
from .Ui_grid_view import Ui_gridView


class GridView(BaseView):

	def __init__(self) -> None:
		super().__init__()

		self.ui = Ui_gridView()

		self.setupUi()
		self.setupSignals()


	def setupUi(self):
		self.ui.setupUi(self)

		self.overlay = LoadingOverlay(self.ui.scrollArea)
		self.ui.fileTypeComboBox.make_pre_checked()


	def setupSignals(self):
		self.ui.searchLineEdit.returnPressed.connect(self.search_enter_pressed)
		self.ui.nextButton.clicked.connect(self.on_nextButton_clicked)
		self.ui.prevButton.clicked.connect(self.on_prevButton_clicked)
		self.ui.sortComboBox.currentTextChanged.connect(self.on_sortComboBox_change)
		self.ui.orderComboBox.currentTextChanged.connect(self.on_ordCombBox_change)
		self.ui.fileTypeComboBox.selectionUpdated.connect(self.on_fileTypeComboBox_change)
		self.ui.tagBar.tags_edited.connect(self.on_tagBar_tag_edited)


	def setupManager(self, manager: BrowserManager):
		self.manager: BrowserManager = manager

		self.manager.component_loaded.connect(self.components_response_handler)
		self.manager.tags_loaded.connect(self.tags_list_response_handler)
		self.manager.page_manager.enable_next.connect(self.ui.nextButton.setEnabled)
		self.manager.page_manager.enable_prev.connect(self.ui.prevButton.setEnabled)

		self.initial_load()


	def updateContent(self, page: Page):
		self.ui.scrollAreaContentItemsWidget.repopulate(page.data)
		self.ui.pageLable.setText(f"{page.page_no} / {page.total_pages}")
		self.loading = False


	@property
	def loading(self) -> bool:
		return self.overlay.isVisible()

	@loading.setter
	def loading(self, load: bool):
		if load:
			self.overlay.show()
		else:
			self.overlay.hide()

	Slot()
	def components_response_handler(self):
		self.updateContent(self.manager.page_manager.page)


	def initial_load(self):
		self.get_request()
		self.manager.request_tags()


	def get_request(self):
		self.overlay.show()
		self.manager.request_components()


	Slot(list)
	def tags_list_response_handler(self, word_list: list):
		self.ui.tagBar.set_suggestions(word_list)


	Slot()
	def on_nextButton_clicked(self):
		self.loading = True
		self.manager.next_page()


	Slot()
	def on_prevButton_clicked(self):
		self.loading = True
		self.manager.prev_page()


	Slot()
	def search_enter_pressed(self):
		self.manager.query_manager.set_search_key(self.ui.searchLineEdit.text())
		self.get_request()


	Slot(str)
	def on_sortComboBox_change(self, value: str):
		self.manager.query_manager.set_sort_by(value)
		self.get_request()


	Slot(str)
	def on_ordCombBox_change(self, value: str):
		self.manager.query_manager.set_sort_ord(value)
		self.get_request()


	Slot(list)
	def on_fileTypeComboBox_change(self, checked_items: list[str]):
		self.manager.query_manager.set_file_types(checked_items)
		self.get_request()

	Slot()
	def on_tagBar_tag_edited(self, tags: list[str]):
		self.manager.query_manager.set_tags(tags)
		self.get_request()
