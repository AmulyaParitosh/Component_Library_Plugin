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

		raw_data: str = self.reply.readAll().data().decode("utf-8")

		self.data = self.parse_json(raw_data)

		if isinstance(self.data, list):
			self.data = {item.get("id"): item for item in self.data}

		self.finished.emit(self.data)
		self.reply.deleteLater()

	@staticmethod
	def parse_json(data: str):
		try:
			parsed_json: dict = json.loads(data)
		except json.decoder.JSONDecodeError:
			parsed_json = dict()
		return parsed_json
