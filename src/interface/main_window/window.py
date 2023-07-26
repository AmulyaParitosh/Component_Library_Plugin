from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QWidget

from ...config import API_URL
from ...manager import OnlineRepoManager
from ..forms import ComponetUploadDialog
from ..views import GridView, OnlineDetailedView
from ..widgets import ComponentItem
from .Ui_window import Ui_MainWindow


class Window(QMainWindow):

	def __init__(self, parent=None) -> None:
		super().__init__(parent=parent)

		self.repo_manager = OnlineRepoManager(API_URL)

		self.show()

		self.ui = Ui_MainWindow()
		self.setupUi()
		self.setupSignals()
		self.setupNetwork()

	def setupUi(self):
		self.ui.setupUi(self)

		# TODO add self.localDetailView once its defined

		self.gridView = GridView(self)
		self.ui.stackedWidget.insertWidget(0, self.gridView)

		self.onlineDetailView = OnlineDetailedView(self)
		self.ui.stackedWidget.insertWidget(1, self.onlineDetailView)


	def setupSignals(self):
		self.ui.browseButton.clicked.connect(self.switch_to_grid_view)
		# ~ self.ui.uploadButton.clicked.connect(self.on_uploadButton_clicked)
		# * no need to connect manually as in setupUi() method at the end QMetaObject.connectSlotsByName(ComponentCreationForm) is used
		# * which will automaticaly connect the on_uploadButton_clicked with the uploadButton

	def setupNetwork(self):
		self.gridView.setupManager(self.repo_manager)
		self.onlineDetailView.setupManager(self.repo_manager)

	def display_detail_view(self, item: ComponentItem):
		self.onlineDetailView.updateContent(item)
		self.ui.stackedWidget.setCurrentWidget(self.onlineDetailView)

	@Slot()
	def switch_to_grid_view(self):
		self.ui.stackedWidget.setCurrentWidget(self.gridView)

	@Slot()
	def on_uploadButton_clicked(self):
		data = ComponetUploadDialog.create_component(self, self.repo_manager)
		print(data)

	def add_notification(self, notification: QWidget):
		self.ui.notificationArea.addWidget(notification)
