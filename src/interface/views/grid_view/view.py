from typing import Callable

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from ....manager import ManagerInterface, OnlineRepoManager
from ....manager.page import PageStates
from ....data import DataFactory, DTypes
# from ....manager.data_loader import load_tags
from ...widgets.overlay import LoadingOverlay
from ..base_view import BaseView
from .Ui_grid_view import Ui_gridView


class GridView(BaseView):

	manager: OnlineRepoManager

	def __init__(self, parent: QWidget) -> None:
		super().__init__(parent)

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
		super().setupManager(manager)
		self.manager.component_loaded.connect(self.components_response_handler)
		self.manager.page_states.enable_next.connect(self.ui.nextButton.setEnabled)
		self.manager.page_states.enable_prev.connect(self.ui.prevButton.setEnabled)

		self.initial_load()


	def updateContent(self, page: PageStates):
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

	@Slot()
	def components_response_handler(self):
		self.updateContent(self.manager.page_states)


	@loading
	def initial_load(self):
		self.manager.reload_page()
		self.ui.tagBar.set_suggestions(DataFactory.load_from_db(DTypes.TAG))

	@loading
	@Slot()
	def on_nextButton_clicked(self):
		self.manager.next_page()


	@loading
	@Slot()
	def on_prevButton_clicked(self):
		self.manager.prev_page()


	@loading
	@Slot()
	def search_enter_pressed(self):
		self.manager.search(self.ui.searchLineEdit.text())


	@loading
	@Slot(str)
	def on_sortComboBox_change(self, value: str):
		self.manager.sort(
			by = value,
			order = self.ui.orderComboBox.currentText(),
		)


	@loading
	@Slot(str)
	def on_ordCombBox_change(self, value: str):
		self.manager.sort(
			by = self.ui.sortComboBox.currentText(),
			order = value,
		)


	@loading
	@Slot(list)
	def on_fileTypeComboBox_change(self, checked_items: list[str]):
		self.manager.filter(
			filetypes = checked_items,
			tags = self.ui.tagBar.tags,
		)

	@loading
	@Slot()
	def on_tagBar_tag_edited(self, tags: list[str]):
		self.manager.query.tags = tags
		self.manager.filter(
			filetypes = self.ui.fileTypeComboBox.checked_items(),
			tags = tags,
		)
