from PySide6.QtCore import QObject, QUrl, Signal, Slot
from PySide6.QtGui import QImage
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

from .network_manager import network_access_manager


class ComponentDownloader(QObject):
	# TODO dev incomplete

	finished = Signal(str)
	error = Signal(QNetworkReply.NetworkError)

	def __init__(self, url: str, save_path: str) -> None:
		super().__init__()

		self.url = QUrl(url)
		self.path = save_path

		request = QNetworkRequest(self.url)
		self.reply = network_access_manager.get(request)
		self.reply.finished.connect(self.downloaded)


	Slot(QNetworkReply)
	def downloaded(self, reply: QNetworkReply):

		if reply.error() != QNetworkReply.NetworkError.NoError:
			self.error.emit(reply.error())
			print(f"Error : {reply.error()}")

		with open(self.path, 'wb') as file:
			file.write(reply.readAll())
			print("Download successful")

		self.finished.emit(self.path)
		reply.deleteLater()



class ImageDownloader(QObject):
	LOADING_THUMBNAIL_PATH = "component_library/user_interface/resources/loading.jpeg"
	DEFAULT_THUMBNAIL_PATH = "component_library/user_interface/resources/default.png"


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
			with open(self.DEFAULT_THUMBNAIL_PATH, 'rb') as file:
				content = file.read()
			image.loadFromData(content)
			self.finished.emit(image)

		elif reply.error() == QNetworkReply.NetworkError.NoError:
			image.loadFromData(reply.readAll())
			self.finished.emit(image)

		else:
			print("error: ", reply.errorString())

		reply.deleteLater()
