from PySide6.QtCore import QObject, QUrl, Signal, Slot
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
