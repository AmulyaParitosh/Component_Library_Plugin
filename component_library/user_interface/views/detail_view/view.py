from PySide6.QtCore import Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QProgressBar, QWidget

from component_library.manager.downloader import FileDownloader

from ....data import Component
from ...widgets import Thumbnail, ComponentItem
from .Ui_detailed_view import Ui_detailedView


class DetailedView(QWidget):
	def __init__(self) -> None:
		super().__init__()

		self.ui = Ui_detailedView()

		self.thumbnail: Thumbnail = None # type: ignore
		self.data: Component = None # type: ignore
		self.files_on_download = {}

		self.setupUi()

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

		self.ui.downloadPushButton.clicked.connect(self.on_downloadButton_click)


	def update_content(self, comp_item: ComponentItem):
		self.data = comp_item.data

		self.ui.contentLabel.setText(self.data.name)

		if self.thumbnail != None:
			self.ui.thumbnailAreaHorizontalLayout.removeWidget(self.thumbnail)

		self.thumbnail = Thumbnail.from_existing(self, comp_item.ui.thumbnail)
		self.ui.thumbnailAreaHorizontalLayout.addWidget(self.thumbnail)

		self.ui.descriptionTextBrowser.setText(self.data.description)
		self.ui.authorValue.setText(self.data.author)
		self.ui.maintainerValue.setText(self.data.maintainer)
		self.ui.createdValue.setText(self.data.created_at)
		self.ui.updatedValue.setText(self.data.updated_at)
		self.ui.ratingwidget.setRating(self.data.rating)
		self.ui.licenseValue.setText(self.data.license.fullname)

		self.ui.filetypeComboBox.clear()
		for file in self.data.files:
			self.ui.filetypeComboBox.addItem(file.type.value)
		self.ui.filetypeComboBox.setCurrentIndex(0)


		if self.data.id in self.files_on_download:
			self.ui.downloadPushButton.setText("Downloading...")
			self.ui.downloadPushButton.setEnabled(False)
		else:
			self.ui.downloadPushButton.setText("Download")
			self.ui.downloadPushButton.setEnabled(True)


	Slot()
	def on_backPushButton_click(self):
		self.topLevelWidget().ui.stackedWidget.setCurrentWidget(self.topLevelWidget().ui.repoBrowser) # type: ignore


	Slot()
	def on_downloadButton_click(self):

		self.ui.downloadPushButton.setText("Downloading...")
		self.ui.downloadPushButton.setEnabled(False)

		for file in self.data.files:
			if file.type == self.ui.filetypeComboBox.currentText():
				downloader = FileDownloader(file.url, "/home/encryptedbee/tesla/projects/GSOC/Component_Library_Plugin/test/downloads", f"{self.data.name}.{file.type}")
				downloader.reply.downloadProgress.connect(self.__update_download_progress)
				downloader.finished.connect(self.on_component_downloaded)
				print("Download started...")

		self.files_on_download[self.data.id] = QProgressBar()
		self.topLevelWidget().ui.notificationAreaLayout.addWidget(self.files_on_download[self.data["id"]]) # type: ignore


	Slot(int, int)
	def __update_download_progress(self, bytes_received, total_bytes):
		self.files_on_download[self.data.id].setMaximum(total_bytes)
		self.files_on_download[self.data.id].setValue(bytes_received)


	Slot(str)
	def on_component_downloaded(self, filepath: str):
		self.ui.downloadPushButton.setText("Remove")
		self.ui.downloadPushButton.setEnabled(True)
		print("Download Successful!")
		print("file at", filepath)
