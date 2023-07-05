from PySide6.QtWidgets import QMainWindow

from .ui.Ui_plugin import Ui_MainWindow


class Plugin(QMainWindow, Ui_MainWindow):
	def __init__(self) -> None:
		super().__init__()
		self.show()
		self.setupUi()

	def setupUi(self):
		super().setupUi(self)
