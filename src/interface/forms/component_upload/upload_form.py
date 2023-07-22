from PySide6.QtWidgets import QPushButton, QWidget

from ....data import DataFactory, DTypes
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

		self.ui.tagsWidget.set_suggestions(DataFactory.load_from_db(DTypes.TAG)) # type: ignore
		# print(DataFactory.load_from_db(DTypes.LICENSE))
		self.ui.licenseInput.addItems((license.fullname for license in DataFactory.load_from_db(DTypes.LICENSE))) # type: ignore

	def pack_data(self):
		...
