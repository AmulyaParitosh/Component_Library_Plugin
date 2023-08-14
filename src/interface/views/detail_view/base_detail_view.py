from abc import abstractmethod

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget

from ....data import Component, File, FileTypes
from ...widgets import DetailedWidget, Thumbnail
from ..base_view import BaseView
from ...widgets import ComponentItem, Thumbnail


# Base class for detailed views of components
class BaseDetailedView(BaseView):

    # Class attribute to store files being downloaded with their corresponding progress bars
    files_on_download = {}
    # Class attribute to store the thumbnail widget
    thumbnail: Thumbnail = None
    # Class attribute to store the component being displayed in the detailed view
    component: Component = None

    # Constructor for the BaseDetailedView class
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        # Create an instance of DetailedWidget and assign it to the 'ui' attribute
        self.ui = DetailedWidget()

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.backPushButton.clicked.connect(self.backPushButton_click)
        self.ui.contentLabel.setFont(QFont('Arial', 28))
        font_14 = QFont('Arial', 14)
        self.ui.descriptionTextBrowser.setFont(font_14)
        self.ui.authorValue.setFont(font_14)
        self.ui.licenseValue.setFont(font_14)
        self.ui.maintainerValue.setFont(font_14)
        self.ui.createdValue.setFont(font_14)
        self.ui.updatedValue.setFont(font_14)

    # Abstract method that must be implemented in derived classes
    # @abstractmethod
    def backPushButton_click(self):
        self.manager.reload_page()
        self.topLevelWidget().toLastWidget()

    # Method to add a control widget to the control area in the detailed view
    def addControlWidget(self, widget: QWidget):
        self.ui.controlArea.addWidget(widget)

    # Method to remove a control widget from the control area in the detailed view
    def removeControlWidget(self, widget: QWidget):
        self.ui.controlArea.removeWidget(widget)

    # Method to add a progress widget to the processes area in the detailed view
    def addProgressWidget(self, widget: QWidget):
        self.ui.processesArea.addWidget(widget)

    def current_file(self) -> File | None:
		# Return the corresponding File object based on the current file type in the combobox
        txt = self.ui.filetypeComboBox.currentText()
        # TODO Check why txt produces empty string
        if txt and FileTypes(txt):
            return self.component.files.get(FileTypes(txt))
        # ! should not return None. Investigate

    def updateContent(self, comp_item: ComponentItem):
        self.component = comp_item.component

        self._update_thumbnail(comp_item.ui.thumbnail)
        self._update_filetype_combobox()

        self.ui.contentLabel.setText(self.component.metadata.name)
        self.ui.descriptionTextBrowser.setText(self.component.metadata.description)
        self.ui.authorValue.setText(self.component.metadata.author)
        self.ui.maintainerValue.setText(self.component.metadata.maintainer)
        self.ui.createdValue.setText(self.component.metadata.created_at)
        self.ui.updatedValue.setText(self.component.metadata.updated_at)
        self.ui.ratingwidget.setRating(self.component.metadata.rating)
        self.ui.licenseValue.setText(self.component.license.fullname)

    # Update the thumbnail widget
    def _update_thumbnail(self, thumbnail_widget):
        if self.thumbnail is not None:
            self.ui.thumbnailAreaHorizontalLayout.removeWidget(self.thumbnail)

        self.thumbnail = Thumbnail.from_existing(self, thumbnail_widget)
        self.ui.thumbnailAreaHorizontalLayout.addWidget(self.thumbnail)

    # Update the filetype combobox based on the component files
    def _update_filetype_combobox(self):
        self.ui.filetypeComboBox.clear()
        for file in self.component.files:
            self.ui.filetypeComboBox.addItem(file.value)
        self.ui.filetypeComboBox.setCurrentIndex(0)
