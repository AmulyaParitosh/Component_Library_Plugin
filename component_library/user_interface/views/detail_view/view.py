from PySide6.QtCore import Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget

from ....manager import BrowserManager
from ...widgets.thumbnail import Thumbnail
from .Ui_detailed_view import Ui_detailedView


class DetailedView(QWidget):
	def __init__(self) -> None:
		super().__init__()

		self.ui = Ui_detailedView()

		self.thumbnail = None
		self.license = "None"

		self.setupUi()

	def setupUi(self):
		self.ui.setupUi(self)
		self.ui.backPushButton.clicked.connect(self.on_backPushButton_click)
		self.ui.contentLabel.setFont(QFont('Arial', 28))
		font_14 = QFont('Arial', 14)
		self.ui.descriptionTextBrowser.setFont(font_14)
		self.ui.authorValue.setFont(font_14)
		self.ui.licenseValue.setFont(font_14)
		self.ui.maintainerValue.setFont(font_14)
		self.ui.createdValue.setFont(font_14)
		self.ui.updatedValue.setFont(font_14)


	def setup_network(self, manager: BrowserManager):
		self.manager: BrowserManager = manager
		self.manager.license_loaded.connect(self.__got_license)


	def updateContent(self, data: dict):
		self.ui.contentLabel.setText(data.get("name", "default"))

		if self.thumbnail != None:
			self.ui.thumbnailAreaHorizontalLayout.removeWidget(self.thumbnail)

		self.thumbnail = Thumbnail(self)

		self.thumbnail.setupThumbnail(data.get("thumbnail", ""))
		self.ui.thumbnailAreaHorizontalLayout.addWidget(self.thumbnail)

		self.ui.descriptionTextBrowser.setText(data.get("description", "None"))
		self.ui.authorValue.setText(data.get("author", "None"))
		self.ui.maintainerValue.setText(data.get("maintainer", "None"))
		self.ui.createdValue.setText(data.get("created_at", "None"))
		self.ui.updatedValue.setText(data.get("updated_at", "None"))
		self.ui.ratingwidget.setRating(data.get("rating", 0))


	def on_backPushButton_click(self):
		self.topLevelWidget().ui.stackedWidget.setCurrentWidget(self.topLevelWidget().ui.repoBrowser) # type: ignore


	Slot(str)
	def __got_license(self, license_name: str):
		self.ui.licenseValue.setText(license_name)
