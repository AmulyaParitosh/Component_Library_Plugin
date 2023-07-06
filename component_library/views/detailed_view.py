from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QFont
from PySide6.QtNetwork import QNetworkRequest
from PySide6.QtWidgets import QWidget

from ..components.thumbnail import Thumbnail
from ..network import component_management_api
from .ui import Ui_detailedView


class DetailedView(QWidget, Ui_detailedView):
	def __init__(self) -> None:
		super().__init__()
		self.setupUi()
		self.thumbnail = None
		self.license = "None"

	def setupUi(self):
		super().setupUi(self)
		self.backPushButton.clicked.connect(self.on_backPushButton_click)
		self.contentLabel.setFont(QFont('Arial', 28))
		font_14 = QFont('Arial', 14)
		self.descriptionTextBrowser.setFont(font_14)
		self.authorValue.setFont(font_14)
		self.licenseValue.setFont(font_14)
		self.maintainerValue.setFont(font_14)
		self.createdValue.setFont(font_14)
		self.updatedValue.setFont(font_14)

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

		self.descriptionTextBrowser.setText(data.get("description", "None"))
		self.authorValue.setText(data.get("author", "None"))
		self.maintainerValue.setText(data.get("maintainer", "None"))
		license_id = data.get("license_id")
		reply = component_management_api.get(QNetworkRequest(f"license/{license_id}"))
		reply.finished.connect(self.__got_license)
		self.createdValue.setText(data.get("created_at", "None"))
		self.updatedValue.setText(data.get("updated_at", "None"))
		self.ratingwidget.setRating(data.get("rating", 0))

	def on_backPushButton_click(self):
		self.topLevelWidget().stackedWidget.setCurrentWidget(self.topLevelWidget().repoBrowser) # type: ignore

	def __got_license(self, json_data: dict):
		self.licenseValue.setText(json_data.get("fullname", "None"))
