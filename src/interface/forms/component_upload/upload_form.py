from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QPushButton

from ....data import DTypes
from ....manager import OnlineRepoManager
from ..Ui_component_form import Ui_ComponentCreationForm


class ComponetUploadDialog(QDialog):
	def __init__(self, parent, manager: OnlineRepoManager) -> None:
		super().__init__(parent)
		self.ui = Ui_ComponentCreationForm()
		self.manager = manager

		self.setupUi()


	def setupUi(self):
		self.ui.setupUi(self)

		self.create_button = QPushButton("Create")
		self.create_button.clicked.connect(self.on_create_button_clicked)
		self.discard_button = QPushButton("Discard")
		self.discard_button.clicked.connect(self.close)

		self.ui.bottomWidget.layout().addWidget(self.create_button)
		self.ui.bottomWidget.layout().addWidget(self.discard_button)

		self.ui.tagsWidget.set_suggestions(self.manager.load_from_db(DTypes.TAG)) # type: ignore
		self.ui.licenseInput.addItems((license.fullname for license in self.manager.load_from_db(DTypes.LICENSE))) # type: ignore


	def pack_data(self):
		return {
			"author" : self.ui.authorInput.text(),
			"description" : self.ui.descriptionInput.toPlainText(),
			"license_id" : next((
								lis.id for # type: ignore
								lis in self.manager.load_from_db(DTypes.LICENSE)
								if lis.fullname == self.ui.licenseInput.currentText() # type: ignore
							)),
			"maintainer" : self.ui.maintainerInput.text(),
			"name" : self.ui.componentNameInput.text(),
			"tags" : self.ui.tagsWidget.tags,
			"version" : "0",
			"repository" : "test-repo",
			"branch" : "main",
			"files" : {
				"component_files" : self.ui.componentFiles.filepaths,
				"thumbnail_image" : self.ui.thumbnailFile.filepath,
			}
		}


	@Slot()
	def on_create_button_clicked(self):
		self.manager.create_component(self.pack_data())


	@classmethod
	def create_component(cls, parent, manager: OnlineRepoManager):
		instance = cls(parent, manager)
		return instance.exec()
