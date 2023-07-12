from PySide6.QtCore import Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QProgressBar

from ....controller.downloader import FileDownloader
from ....controller.manager_interface import (ManagerInterface,
                                              OnlineRepoManager)
from ....data import Component, FileTypes
from ...widgets import ComponentItem, Thumbnail
from ..base_view import BaseView
from .Ui_detailed_view import Ui_detailedView


class DetailedView(BaseView):
	files_on_download = {}

	def __init__(self) -> None:
		super().__init__()

		self.ui = Ui_detailedView()

		self.thumbnail: Thumbnail = None # type: ignore
		self.component: Component = None # type: ignore

		self.setupUi()
		self.setupSignals()

	def setupUi(self):
		self.ui.setupUi(self)
		self.ui.backPushButton.clicked.connect(self.on_backPushButton_click)
		self.ui.contentLabel.setFont(QFont('Arial', 28))
		font_14 = QFont('Arial', 14)
		self.ui.descriptionTextBrowser.setFont(font_14)
		self.ui.authorValue.setFont(font_14)
		self.ui.licenseValue.setFont(font_14)
		self.ui.maintainerValue.setFont(font_14)
		self.ui.createdValue.setFont(font_14)
		self.ui.updatedValue.setFont(font_14)


	def setupSignals(self):
		self.ui.downloadPushButton.clicked.connect(self.on_downloadButton_click)


	def setupManager(self, manager: ManagerInterface):
		self.manage: OnlineRepoManager = manager


	def updateContent(self, comp_item: ComponentItem):
		self.component = comp_item.component

		self.ui.contentLabel.setText(self.component.name)

		if self.thumbnail != None:
			self.ui.thumbnailAreaHorizontalLayout.removeWidget(self.thumbnail)

		self.thumbnail = Thumbnail.from_existing(self, comp_item.ui.thumbnail)
		self.ui.thumbnailAreaHorizontalLayout.addWidget(self.thumbnail)

		self.ui.descriptionTextBrowser.setText(self.component.description)
		self.ui.authorValue.setText(self.component.author)
		self.ui.maintainerValue.setText(self.component.maintainer)
		self.ui.createdValue.setText(self.component.created_at)
		self.ui.updatedValue.setText(self.component.updated_at)
		self.ui.ratingwidget.setRating(self.component.rating)
		self.ui.licenseValue.setText(self.component.license.fullname)

		self.ui.filetypeComboBox.clear()
		for file in self.component.files:
			self.ui.filetypeComboBox.addItem(file.value)
		self.ui.filetypeComboBox.setCurrentIndex(0)


		if self.component.id in self.files_on_download:
			self.ui.downloadPushButton.setText("Downloading...")
			self.ui.downloadPushButton.setEnabled(False)
		else:
			self.ui.downloadPushButton.setText("Download")
			self.ui.downloadPushButton.setEnabled(True)


	Slot()
	def on_backPushButton_click(self):
		self.topLevelWidget().switch_to_grid_view() # type: ignore


	Slot()
	def on_downloadButton_click(self):

		self.ui.downloadPushButton.setText("Downloading...")
		self.ui.downloadPushButton.setEnabled(False)

		downloader: FileDownloader = self.manage.download_component(
			self.component,
			FileTypes(self.ui.filetypeComboBox.currentText()),
		)
		downloader.downloadProgress.connect(self.__update_download_progress)
		downloader.finished.connect(self.on_component_downloaded)
		print("Download started...")

		self.files_on_download[self.component.id] = QProgressBar()
		self.topLevelWidget().add_notification(self.files_on_download[self.component.id]) # type: ignore


	Slot(int, int)
	def __update_download_progress(self, bytes_received, total_bytes):
		self.files_on_download[self.component.id].setMaximum(total_bytes)
		self.files_on_download[self.component.id].setValue(bytes_received)


	Slot(str)
	def on_component_downloaded(self, filepath: str):
		self.ui.downloadPushButton.setText("Remove")
		self.ui.downloadPushButton.setEnabled(True)
		print("Download Successful!")
		print("file at", filepath)
