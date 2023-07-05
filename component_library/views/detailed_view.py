from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget

from ..components.thumbnail import Thumbnail
from .ui import Ui_detailedView


class DetailedView(QWidget, Ui_detailedView):
	def __init__(self) -> None:
		super().__init__()
		self.setupUi()
		self.contentLabel.setFont(QFont('Arial', 28))
		self.thumbnail = None

	def setupUi(self):
		super().setupUi(self)
		self.backPushButton.clicked.connect(self.on_backPushButton_click)


	def updateContent(self, data: dict):
		self.contentLabel.setText(data.get("name", "default"))

		if self.thumbnail != None:
			self.thumbnailAreaHorizontalLayout.removeWidget(self.thumbnail)

		self.thumbnail = Thumbnail(self)

		url_str: str = data.get("thumbnail", "")
		url: QUrl = QUrl.fromUserInput(url_str)
		self.thumbnail.setupThumbnail(url)
		self.thumbnail.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
		self.thumbnailAreaHorizontalLayout.addWidget(self.thumbnail)

	def on_backPushButton_click(self):
		self.topLevelWidget().stackedWidget.setCurrentWidget(self.topLevelWidget().repoBrowser) # type: ignore
