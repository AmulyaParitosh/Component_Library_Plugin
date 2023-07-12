from typing import Callable

from PySide6.QtCore import Slot

from component_library.controller.manager_interface import ManagerInterface

from ....controller import ManagerInterface, Page
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

		self.loading_overlay = LoadingOverlay(self.ui.scrollArea)
		self.ui.fileTypeComboBox.make_pre_checked()


	def setupSignals(self):
		self.ui.searchLineEdit.returnPressed.connect(self.search_enter_pressed)
		self.ui.nextButton.clicked.connect(self.on_nextButton_clicked)
		self.ui.prevButton.clicked.connect(self.on_prevButton_clicked)
		self.ui.sortComboBox.currentTextChanged.connect(self.on_sortComboBox_change)
		self.ui.orderComboBox.currentTextChanged.connect(self.on_ordCombBox_change)
		self.ui.fileTypeComboBox.selectionUpdated.connect(self.on_fileTypeComboBox_change)
		self.ui.tagBar.tags_edited.connect(self.on_tagBar_tag_edited)


	def setupManager(self, manager: ManagerInterface):
		self.manager: ManagerInterface = manager

		self.manager.component_loaded.connect(self.components_response_handler)
		self.manager.page.enable_next.connect(self.ui.nextButton.setEnabled)
		self.manager.page.enable_prev.connect(self.ui.prevButton.setEnabled)

		self.initial_load()


	def updateContent(self, page: Page):
		self.ui.scrollAreaContentItemsWidget.repopulate(page.data)
		self.ui.pageLable.setText(f"{page.page_no} / {page.total_pages}")
		self.loading_overlay.loading = False

	@staticmethod
	def loading(func: Callable):
		def wraper(self, *args, **kwargs):
			self.loading_overlay.loading = True
			self.ui.scrollArea.verticalScrollBar().setValue(0)
			return func(self, *args, **kwargs)
		return wraper

	Slot()
	def components_response_handler(self):
		self.updateContent(self.manager.page)


	@loading
	def initial_load(self):
		self.manager.reload_page()
		reply = self.manager.request_tags()
		reply.finished.connect(self.tags_list_response_handler)


	Slot(dict)
	def tags_list_response_handler(self, json_data: dict):
		word_list: list[str] = [tag.get("label") for tag in json_data.get("items", [])]
		self.ui.tagBar.set_suggestions(word_list)


	Slot()
	@loading
	def on_nextButton_clicked(self):
		self.manager.next_page()


	Slot()
	@loading
	def on_prevButton_clicked(self):
		self.manager.prev_page()


	Slot()
	@loading
	def search_enter_pressed(self):
		self.manager.query.search_key = self.ui.searchLineEdit.text()
		self.manager.reload_page()


	Slot(str)
	@loading
	def on_sortComboBox_change(self, value: str):
		self.manager.query.sort_by = value
		self.manager.reload_page()


	Slot(str)
	@loading
	def on_ordCombBox_change(self, value: str):
		self.manager.query.sort_ord = value
		self.manager.reload_page()


	Slot(list)
	@loading
	def on_fileTypeComboBox_change(self, checked_items: list[str]):
		self.manager.query.file_types = checked_items
		self.manager.reload_page()

	Slot()
	@loading
	def on_tagBar_tag_edited(self, tags: list[str]):
		self.manager.query.tags = tags
		self.manager.reload_page()
