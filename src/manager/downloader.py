from PySide6.QtCore import QFile, QIODevice, QObject, QUrl, Signal, Slot
from PySide6.QtGui import QImage
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

from ..network.network_manager import network_access_manager


class FileDownloader(QObject):

	finished = Signal(str)
	error = Signal(QNetworkReply.NetworkError)

	def __init__(self, url: str, save_path: str, filename: str) -> None:
		super().__init__()

		self.url = QUrl(url)
		self.path: str = save_path
		self.filename: str = filename
		self.filepath: str = f"{self.path}/{self.filename}"

		request = QNetworkRequest(self.url)
		self.reply: QNetworkReply = network_access_manager.get(request)
		self.reply.finished.connect(lambda : self.__downloaded(self.reply))
		self.downloadProgress = self.reply.downloadProgress


	Slot(QNetworkReply)
	def __downloaded(self, reply: QNetworkReply):

		if reply.error() != QNetworkReply.NetworkError.NoError:
			print(f"Error : {reply.error()}")
			self.error.emit(reply.error())

		file = QFile(self.filepath)

		if file.open(QIODevice.OpenModeFlag.WriteOnly):
			file.write(reply.readAll())

		file.close()
		self.finished.emit(self.filepath)
		reply.deleteLater()
		self.deleteLater()


class ImageDownloader(QObject):
	LOADING_THUMBNAIL_PATH = "src/interface/resources/loading.jpeg"
	DEFAULT_THUMBNAIL_PATH = "src/interface/resources/default.png"

	finished = Signal(QImage)

	def __init__(self, parent=None):
		super().__init__(parent)


	def start_download(self, url: QUrl):
		reply: QNetworkReply = network_access_manager.get(QNetworkRequest(url))
		reply.finished.connect(lambda : self.handle_finished(reply))

	def handle_finished(self, reply: QNetworkReply):

		image = QImage()

		if reply.error() == QNetworkReply.NetworkError.ProtocolUnknownError:

			file = QFile(self.DEFAULT_THUMBNAIL_PATH)

			if file.open(QIODevice.OpenModeFlag.ReadOnly):
				content = file.readAll()
				image.loadFromData(content)
				self.finished.emit(image)

			file.close()

		elif reply.error() == QNetworkReply.NetworkError.NoError:
			image.loadFromData(reply.readAll())
			self.finished.emit(image)

		else:
			print("error: ", reply.errorString())

		reply.deleteLater()
