from __future__ import annotations

from PySide6.QtCore import QUrl
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel, QWidget

from ....manager import ImageDownloader


class Thumbnail(QLabel):
	def __init__(self, parent: QWidget, url: str|None=None) -> None:
		super().__init__(parent)
		self.setScaledContents(True)
		self.setPixmap(QPixmap(ImageDownloader.LOADING_THUMBNAIL_PATH))

		self.downloader = ImageDownloader()
		self.downloader.finished.connect(self.loadImage)

		if url:
			self.setupThumbnail(url)

	def setupThumbnail(self, url_str: str):
		self.downloader.start_download(QUrl.fromUserInput(url_str))

	def loadImage(self, image: QImage):
		pixmap = QPixmap(image)
		self.setPixmap(pixmap)

	@staticmethod
	def from_existing(parent, thumbnail: Thumbnail):
		new_thumbnail = Thumbnail(parent)
		new_thumbnail.setPixmap(thumbnail.pixmap())
		return new_thumbnail
