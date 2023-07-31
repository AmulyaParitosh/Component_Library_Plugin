from pathlib import Path

from PySide6.QtCore import QFile, QIODevice, QObject, QUrl, Signal, Slot
from PySide6.QtGui import QImage
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

from ..network.network_manager import get_network_access_manager


class FileDownloader(QObject):

	finished = Signal(Path)
	error = Signal(QNetworkReply.NetworkError)

	network_access_manager, sslConfig = get_network_access_manager()


	def __init__(self, url: str, save_path: Path, filename: str) -> None:
		super().__init__()

		self.url = QUrl(url)
		save_path.mkdir(exist_ok=True)
		self.filename: str = filename
		self.filepath = save_path/self.filename

		request = QNetworkRequest(self.url)
		self.reply: QNetworkReply = self.network_access_manager.get(request)
		self.reply.finished.connect(lambda : self.__downloaded(self.reply))
		self.downloadProgress = self.reply.downloadProgress


	@Slot(QNetworkReply)
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


class ImageLoader(QObject):
	LOADING_THUMBNAIL_PATH = "src/interface/resources/loading.jpeg"
	DEFAULT_THUMBNAIL_PATH = "src/interface/resources/default.png"

	finished = Signal(QImage)

	network_access_manager, sslConfig = get_network_access_manager()

	def __init__(self, parent=None):
		super().__init__(parent)


	def start_download(self, url: QUrl):
		reply: QNetworkReply = self.network_access_manager.get(QNetworkRequest(url))
		reply.finished.connect(lambda : self.handle_finished(reply))

	def handle_finished(self, reply: QNetworkReply):
		image = self.load_image_from_reply(reply)

		if image.isNull():
			print("Error: Unable to load image from the reply.")
			return

		self.finished.emit(image)
		reply.deleteLater()

	def load_image_from_reply(self, reply: QNetworkReply) -> QImage:
		image = QImage()

		if reply.error() == QNetworkReply.NetworkError.ProtocolUnknownError:
			default_thumbnail_file = QFile(self.DEFAULT_THUMBNAIL_PATH)

			if default_thumbnail_file.open(QIODevice.OpenModeFlag.ReadOnly):
				content = default_thumbnail_file.readAll()
				default_thumbnail_file.close()
				image.loadFromData(content)

		elif reply.error() == QNetworkReply.NetworkError.NoError:
			image.loadFromData(reply.readAll())

		return image
