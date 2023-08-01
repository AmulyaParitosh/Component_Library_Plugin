from enum import Enum, auto
from pathlib import Path

from PySide6.QtCore import Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QProgressBar, QWidget

from .....data import File, FileTypes
from .....manager import ManagerInterface, OnlineRepoManager
from ....widgets import ComponentItem, StatefullPushButton, Thumbnail
from ..base_detail_view import BaseDetailedView


class DownloadStates(Enum):
	DOWNLOAD = auto()
	IN_PROGRESS = auto()
	FINISHED = auto()


class OnlineDetailedView(BaseDetailedView):
	manager: OnlineRepoManager

	def __init__(self, parent: QWidget) -> None:
		super().__init__(parent)

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

		self.downloadPushButton = StatefullPushButton(self)
		self.addControlWidget(self.downloadPushButton)


	def setupSignals(self):
		self.downloadPushButton.register_state(
			DownloadStates.DOWNLOAD,
			self.on_downloadButton_click,
			"Download",
			True
		)
		self.downloadPushButton.register_state(
			DownloadStates.IN_PROGRESS,
			None,
			"Downloading...",
			False
		)
		self.downloadPushButton.register_state(
			DownloadStates.FINISHED,
			None,
			"Remove",
			True
		)

		self.ui.filetypeComboBox.currentTextChanged.connect(self.update_download_button_state)


	def setupManager(self, manager: ManagerInterface):
		super().setupManager(manager)


	def updateContent(self, comp_item: ComponentItem):
		self.component = comp_item.component

		self._update_thumbnail(comp_item.ui.thumbnail)
		self._update_filetype_combobox()
		self.update_download_button_state()

		self.ui.contentLabel.setText(self.component.metadata.name)
		self.ui.descriptionTextBrowser.setText(self.component.metadata.description)
		self.ui.authorValue.setText(self.component.metadata.author)
		self.ui.maintainerValue.setText(self.component.metadata.maintainer)
		self.ui.createdValue.setText(self.component.metadata.created_at)
		self.ui.updatedValue.setText(self.component.metadata.updated_at)
		self.ui.ratingwidget.setRating(self.component.metadata.rating)
		self.ui.licenseValue.setText(self.component.license.fullname)


	def _update_thumbnail(self, thumbnail_widget):
		if self.thumbnail is not None:
			self.ui.thumbnailAreaHorizontalLayout.removeWidget(self.thumbnail)

		self.thumbnail = Thumbnail.from_existing(self, thumbnail_widget)
		self.ui.thumbnailAreaHorizontalLayout.addWidget(self.thumbnail)

	def _update_filetype_combobox(self):
		self.ui.filetypeComboBox.clear()
		for file in self.component.files:
			self.ui.filetypeComboBox.addItem(file.value)
		self.ui.filetypeComboBox.setCurrentIndex(0)


	@Slot()
	def on_backPushButton_click(self):
		self.topLevelWidget().switch_to_grid_view() # type: ignore


	@Slot()
	def on_downloadButton_click(self):
		file = self.current_file()
		if file is None:
			return
		self.files_on_download[file.id] = QProgressBar()
		self.topLevelWidget().add_notification(self.files_on_download[file.id]) # type: ignore

		self.downloadPushButton.setState(DownloadStates.IN_PROGRESS)

		downloader = self.manager.download_component(
			self.component,
			file.type,
		)
		downloader.downloadProgress.connect(self.__update_download_progress)
		downloader.finished.connect(self.on_component_downloaded)
		print("Download started...")


	@Slot(int, int)
	def __update_download_progress(self, bytes_received, total_bytes):
		file = self.current_file()
		if file is None:
			return
		self.files_on_download[file.id].setMaximum(total_bytes)
		self.files_on_download[file.id].setValue(bytes_received)


	@Slot(Path)
	def on_component_downloaded(self, filepath: Path):
		file = self.current_file()
		if file is None:
			return
		self.downloadPushButton.setState(DownloadStates.FINISHED)
		file.EXISTS = True
		self.files_on_download.pop(file.id)
		print("Download Successful!")
		print("file at", filepath)


	def is_file_on_download(self):
		file = self.current_file()
		return (file is not None) and (file.id in self.files_on_download)


	def current_file(self) -> File | None:
		txt = self.ui.filetypeComboBox.currentText()
		if txt and FileTypes(txt):
			return self.component.files.get(FileTypes(txt))

	@Slot(str)
	def update_download_button_state(self):
		if self.is_file_on_download():
			self.downloadPushButton.setState(DownloadStates.IN_PROGRESS)
		elif file := self.current_file():
			if file is not None and file.EXISTS:
				self.downloadPushButton.setState(DownloadStates.FINISHED)
		else:
			self.downloadPushButton.setState(DownloadStates.DOWNLOAD)
