from PySide6.QtWidgets import QMainWindow

from ...controller import RepoManager
from .Ui_plugin import Ui_MainWindow


class Window(QMainWindow):
	def __init__(self, api_url: str, parent=None) -> None:
		super().__init__(parent=parent)

		self.repo_manager = RepoManager(api_url)

		self.show()

		self.ui = Ui_MainWindow()
		self.setupUi()
		self.setup_network()

	def setupUi(self):
		self.ui.setupUi(self)

	def setup_network(self):
		self.ui.repoBrowser.setupManager(self.repo_manager)
		# self.ui.componentDetail.setupManager(self.browser_manager)
