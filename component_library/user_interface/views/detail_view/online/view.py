from PySide6.QtCore import Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QProgressBar, QPushButton

from .....controller.downloader import FileDownloader
from .....controller.manager_interface import (ManagerInterface,
                                               OnlineRepoManager)
from .....data import FileTypes
from ....widgets import ComponentItem, Thumbnail
from ..base_detail_view import BaseDetailedView


class OnlineDetailedView(BaseDetailedView):
	manager: OnlineRepoManager

	def __init__(self) -> None:
		super().__init__()

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

		self.downloadPushButton = QPushButton("Download")
		self.addControlWidget(self.downloadPushButton)


	def setupSignals(self):
		self.downloadPushButton.clicked.connect(self.on_downloadButton_click)


	def setupManager(self, manager: ManagerInterface):
		super().setupManager(manager)


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
			self.downloadPushButton.setText("Downloading...")
			self.downloadPushButton.setEnabled(False)
		else:
			self.downloadPushButton.setText("Download")
			self.downloadPushButton.setEnabled(True)


	Slot()
	def on_backPushButton_click(self):
		self.topLevelWidget().switch_to_grid_view() # type: ignore


	Slot()
	def on_downloadButton_click(self):

		self.downloadPushButton.setText("Downloading...")
		self.downloadPushButton.setEnabled(False)

		downloader: FileDownloader = self.manager.download_component(
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
		self.downloadPushButton.setText("Remove")
		self.downloadPushButton.setEnabled(True)
		print("Download Successful!")
		print("file at", filepath)
