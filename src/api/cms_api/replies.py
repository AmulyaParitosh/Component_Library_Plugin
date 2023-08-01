import json

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtNetwork import QNetworkReply


# Custom QObject class to handle network replies and emit signals with parsed data
class CMSReply(QObject):
    # Signal to be emitted when the reply is finished, with the parsed data as an argument
    finished = Signal(dict)

    def __init__(self, reply: QNetworkReply, parent) -> None:
        super().__init__(parent)
        self.reply: QNetworkReply = reply
        self.reply.finished.connect(self.response_serializer)

    # Slot method to handle the network reply and parse the JSON data
    @Slot()
    def response_serializer(self) -> None:
        # Check if there was an error in the network reply
        if self.reply.error() != QNetworkReply.NetworkError.NoError:
            print(f"Error: {self.reply.errorString()}")

        # Read the raw data from the network reply and decode it as UTF-8 as parse as JSON
        raw_data: str = self.reply.readAll().data().decode("utf-8")
        self.data = self.parse_json(raw_data)

        # If the parsed data is a list, convert it to a dictionary using the 'id' field as the key
        if isinstance(self.data, list):
            self.data = {item.get("id"): item for item in self.data}

        self.finished.emit(self.data)
        self.reply.deleteLater()

    # Static method to parse JSON data, handling potential JSONDecodeError
    @staticmethod
    def parse_json(data: str):
        try:
            parsed_json: dict = json.loads(data)
        except json.decoder.JSONDecodeError:
            parsed_json = dict()
        return parsed_json
