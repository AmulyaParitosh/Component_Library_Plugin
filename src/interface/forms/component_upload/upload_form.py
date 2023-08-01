from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QPushButton

# Import the necessary components from the application.
from ....data import DTypes
from ....manager import OnlineRepoManager
from ..Ui_component_form import Ui_ComponentCreationForm


class ComponetUploadDialog(QDialog):
    # Custom QDialog for creating and uploading new components.

    def __init__(self, parent, manager: OnlineRepoManager) -> None:
        # Constructor to initialize the ComponentUploadDialog.

        super().__init__(parent)

        # Initialize the user interface from the Ui_ComponentCreationForm.
        self.ui = Ui_ComponentCreationForm()
        self.manager = manager

        # Set up the dialog.
        self.setupUi()

    def setupUi(self):
        # Method to set up the user interface of the dialog.

        self.ui.setupUi(self)

        # Create "Create" and "Discard" buttons and connect their click events.
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.on_create_button_clicked)
        self.discard_button = QPushButton("Discard")
        self.discard_button.clicked.connect(self.close)

        # Add the buttons to the bottom widget layout.
        self.ui.bottomWidget.layout().addWidget(self.create_button)
        self.ui.bottomWidget.layout().addWidget(self.discard_button)

        # Set suggestions for tags and licenses using the OnlineRepoManager.
        self.ui.tagsWidget.set_suggestions(self.manager.load_from_db(DTypes.TAG)) # type: ignore
        self.ui.licenseInput.addItems((license.fullname for license in self.manager.load_from_db(DTypes.LICENSE))) # type: ignore

    def pack_data(self):
        # Method to pack the data entered in the form.

        return {
            "author": self.ui.authorInput.text(),
            "description": self.ui.descriptionInput.toPlainText(),
            "license_id": next((
                lis.id for # type: ignore
                lis in self.manager.load_from_db(DTypes.LICENSE)
                if lis.fullname == self.ui.licenseInput.currentText() # type: ignore
            )),
            "maintainer": self.ui.maintainerInput.text(),
            "name": self.ui.componentNameInput.text(),
            "tags": self.ui.tagsWidget.tags,
            "version": "0",
            "repository": "test-repo",
            "branch": "main",
            "files": {
                "component_files": self.ui.componentFiles.filepaths,
                "thumbnail_image": self.ui.thumbnailFile.filepath,
            }
        }

    @Slot()
    def on_create_button_clicked(self):
        # Slot to handle the "Create" button click event.

        # Pack the data and create the component using the OnlineRepoManager.
        self.manager.create_component(self.pack_data())

    @classmethod
    def create_component(cls, parent, manager: OnlineRepoManager):
        # Class method to create and execute the ComponentUploadDialog.

        instance = cls(parent, manager)
        return instance.exec()
