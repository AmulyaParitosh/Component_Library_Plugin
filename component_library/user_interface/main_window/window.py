from PySide6.QtWidgets import QMainWindow, QWidget

from ...controller import OnlineRepoManager
from ..widgets import ComponentItem
from .Ui_plugin import Ui_MainWindow


class Window(QMainWindow):
	def __init__(self, parent=None) -> None:
		super().__init__(parent=parent)

		self.repo_manager = OnlineRepoManager("http://127.0.0.1:5000")

		self.show()

		self.ui = Ui_MainWindow()
		self.setupUi()
		self.setup_network()

	def setupUi(self):
		self.ui.setupUi(self)

	def setup_network(self):
		self.ui.repoBrowser.setupManager(self.repo_manager)
		self.ui.componentDetail.setupManager(self.repo_manager)

	def display_detail_view(self, item: ComponentItem):
		self.ui.componentDetail.updateContent(item)
		self.ui.stackedWidget.setCurrentWidget(self.ui.componentDetail)

	def switch_to_grid_view(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.repoBrowser)

	def add_notification(self, notification: QWidget):
		self.ui.notificationAreaLayout.addWidget(notification)
