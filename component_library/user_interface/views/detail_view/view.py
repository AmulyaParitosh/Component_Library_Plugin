from PySide6.QtCore import Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QProgressBar

from component_library.manager.downloader import FileDownloader

from ....manager import BrowserManager
from ...widgets.thumbnail import Thumbnail
from .Ui_detailed_view import Ui_detailedView


class DetailedView(QWidget):
	def __init__(self) -> None:
		super().__init__()

		self.ui = Ui_detailedView()

		self.thumbnail = None
		self.license = "None"
		self.data = dict()
		self.files = []

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


	def setup_network(self, manager: BrowserManager):
		self.manager: BrowserManager = manager
		self.manager.license_loaded.connect(self.__got_license)
		self.manager.files_loaded.connect(self.__got_files)


	def updateContent(self, data: dict):

		self.data = data

		self.ui.contentLabel.setText(data.get("name", "default"))

		if self.thumbnail != None:
			self.ui.thumbnailAreaHorizontalLayout.removeWidget(self.thumbnail)

		self.thumbnail = Thumbnail(self)

		self.thumbnail.setupThumbnail(data.get("thumbnail", ""))
		self.ui.thumbnailAreaHorizontalLayout.addWidget(self.thumbnail)

		self.ui.descriptionTextBrowser.setText(data.get("description", "None"))
		self.ui.authorValue.setText(data.get("author", "None"))
		self.ui.maintainerValue.setText(data.get("maintainer", "None"))
		self.ui.createdValue.setText(data.get("created_at", "None"))
		self.ui.updatedValue.setText(data.get("updated_at", "None"))
		self.ui.ratingwidget.setRating(data.get("rating", 0))

		if data.get("id") in self.files_on_download:
			self.ui.downloadPushButton.setText("Downloading...")
			self.ui.downloadPushButton.setEnabled(False)
		else:
			self.ui.downloadPushButton.setText("Download")
			self.ui.downloadPushButton.setEnabled(True)

		self.manager.get_files(data.get("id", "None"))


	Slot()
	def on_backPushButton_click(self):
		self.topLevelWidget().ui.stackedWidget.setCurrentWidget(self.topLevelWidget().ui.repoBrowser) # type: ignore


	Slot()
	def on_downloadButton_click(self):

		self.ui.downloadPushButton.setText("Downloading...")
		self.ui.downloadPushButton.setEnabled(False)

		for file in self.files:
			if file["type"]["name"] == self.ui.filetypeComboBox.currentText():
				downloader = FileDownloader(file["url"], "/home/encryptedbee/tesla/projects/GSOC/Component_Library_Plugin/test/downloads", f"{self.data['name']}.{file['type']['name']}")
				downloader.reply.downloadProgress.connect(self.__update_download_progress)
				downloader.finished.connect(self.on_component_downloaded)
				print("Download started...")

		self.files_on_download[self.data["id"]] = QProgressBar()
		self.topLevelWidget().ui.notificationAreaLayout.addWidget(self.files_on_download[self.data["id"]]) # type: ignore


	Slot(str)
	def __got_license(self, license_name: str):
		self.ui.licenseValue.setText(license_name)


	Slot(int, int)
	def __update_download_progress(self, bytes_received, total_bytes):
		self.files_on_download[self.data["id"]].setMaximum(total_bytes)
		self.files_on_download[self.data["id"]].setValue(bytes_received)

	Slot(dict)
	def __got_files(self, files: dict):
		self.files = files.values()
		self.ui.filetypeComboBox.clear()
		for file in files.values():
			self.ui.filetypeComboBox.addItem(file["type"]["name"])
		self.ui.filetypeComboBox.setCurrentIndex(0)

	Slot(str)
	def on_component_downloaded(self, filepath: str):
		self.ui.downloadPushButton.setText("Remove")
		self.ui.downloadPushButton.setEnabled(True)
		print("Download Successful!")
		print("file at", filepath)
