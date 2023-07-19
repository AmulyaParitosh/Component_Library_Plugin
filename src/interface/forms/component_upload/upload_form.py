from PySide6.QtWidgets import QPushButton, QWidget

from ..Ui_component_form import Ui_componentCreationForm


class ComponetUploadForm(QWidget):
	def __init__(self, parent: QWidget) -> None:
		super().__init__(parent)
		self.ui = Ui_componentCreationForm()

		self.setupUi()

	def setupUi(self):
		self.ui.setupUi(self)
		self.create_button = QPushButton("Create")
		self.discard_button = QPushButton("Discard")
		self.ui.bottomWidget.layout().addWidget(self.create_button)
		self.ui.bottomWidget.layout().addWidget(self.discard_button)

	def pack_data(self):
		...
