from __future__ import annotations

from PySide6.QtCore import QObject, QUrl, Signal
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest
from PySide6.QtWidgets import QLabel, QWidget

from ...network import network_access_manager

LOADING_THUMBNAIL_PATH = "component_library/components/thumbnail/loading.jpeg"
DEFAULT_THUMBNAIL_PATH = "component_library/components/thumbnail/default.png"


class ImageDownloader(QObject):
	finished = Signal(QImage)

	def __init__(self, parent=None):
		super().__init__(parent)
		self.manager = network_access_manager


	def start_download(self, url: QUrl):
		reply = self.manager.get(QNetworkRequest(url))
		reply.finished.connect(lambda : self.handle_finished(reply))

	def handle_finished(self, reply: QNetworkReply):

		image = QImage()

		if reply.error() == QNetworkReply.NetworkError.ProtocolUnknownError:
			with open(DEFAULT_THUMBNAIL_PATH, 'rb') as file:
				content = file.read()
			image.loadFromData(content)
			self.finished.emit(image)

		elif reply.error() == QNetworkReply.NetworkError.NoError:
			image.loadFromData(reply.readAll())
			self.finished.emit(image)

		else:
			print("error: ", reply.errorString())

		reply.deleteLater()


class Thumbnail(QLabel):
	def __init__(self, parent: QWidget) -> None:
		super().__init__(parent)
		self.setScaledContents(True)
		self.setPixmap(QPixmap(LOADING_THUMBNAIL_PATH))

		self.downloader = ImageDownloader()
		self.downloader.finished.connect(self.loadImage)

	def setupThumbnail(self, image_url: QUrl):
		self.downloader.start_download(image_url)

	def loadImage(self, image: QImage):
		pixmap = QPixmap(image)
		self.setPixmap(pixmap)
