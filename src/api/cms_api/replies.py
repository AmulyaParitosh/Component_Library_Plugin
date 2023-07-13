import json

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtNetwork import QNetworkReply


class CMSReply(QObject):

	finished = Signal(dict)

	def __init__(self, reply: QNetworkReply, parent) -> None:
		super().__init__(parent)
		self.reply: QNetworkReply = reply
		self.reply.finished.connect(self.response_serializer)

	Slot()
	def response_serializer(self) -> None:
		if self.reply.error() != QNetworkReply.NetworkError.NoError:
			print(f"Error : {self.reply.errorString()}")

		data: str = self.reply.readAll().data().decode("utf-8")

		try:
			self.data: dict = json.loads(data)
		except json.decoder.JSONDecodeError:
			self.data = dict()

		if isinstance(self.data, list):
			self.data = {item.get("id"): item for item in self.data}

		self.finished.emit(self.data)
		self.reply.deleteLater()
