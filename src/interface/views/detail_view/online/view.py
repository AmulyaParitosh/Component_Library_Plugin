from enum import Enum, auto
from pathlib import Path

from PySide6.QtCore import Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QProgressBar, QWidget

from .....data import File, FileTypes
from .....manager import ManagerInterface, OnlineRepoManager
from ....widgets import ComponentItem, StatefullPushButton, Thumbnail
from ..base_detail_view import BaseDetailedView

# Enum to represent different download states
class DownloadStates(Enum):
    DOWNLOAD = auto()
    IN_PROGRESS = auto()
    FINISHED = auto()

# Class for the online detailed view of a component
class OnlineDetailedView(BaseDetailedView):
    # Declare a class attribute 'manager' of type OnlineRepoManager
    manager: OnlineRepoManager

    # Constructor for the OnlineDetailedView class
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        # Call the setupUi and setupSignals methods
        self.setupUi()
        self.setupSignals()

    # Initialize the user interface elements
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

        self.downloadPushButton = StatefullPushButton(self)
        self.addControlWidget(self.downloadPushButton)

    # Connect signals to their respective slots
    def setupSignals(self):
        self.downloadPushButton.register_state(
            DownloadStates.DOWNLOAD,
            self.downloadButton_click,
            "Download",
            True
        )
        self.downloadPushButton.register_state(
            DownloadStates.IN_PROGRESS,
            None,
            "Downloading...",
            False
        )
        self.downloadPushButton.register_state(
            DownloadStates.FINISHED,
            None,
            "Remove",
            True
        )

        self.ui.filetypeComboBox.currentTextChanged.connect(self.update_download_button_state)

    # Set up the manager for the OnlineDetailedView
    def setupManager(self, manager: ManagerInterface):
        super().setupManager(manager)

    # Update the content based on the given ComponentItem
    def updateContent(self, comp_item: ComponentItem):
        self.component = comp_item.component

        self._update_thumbnail(comp_item.ui.thumbnail)
        self._update_filetype_combobox()
        self.update_download_button_state()

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

    # Slot method to handle backPushButton click
    @Slot()
    def backPushButton_click(self):
        # Switch back to the grid view when the back button is clicked
        self.topLevelWidget().switch_to_grid_view() # type: ignore

    # Slot method to handle downloadButton click
    @Slot()
    def downloadButton_click(self):
        file = self.current_file()
        if file is None:
            return

        # Add a progress bar for the file being downloaded
        self.files_on_download[file.id] = QProgressBar()
        self.topLevelWidget().add_notification(self.files_on_download[file.id]) # type: ignore
        self.downloadPushButton.setState(DownloadStates.IN_PROGRESS)

        # Start the component download process
        downloader = self.manager.download_component(
            self.component,
            file.type,
        )
        downloader.downloadProgress.connect(self.__update_download_progress)
        downloader.finished.connect(self.component_downloaded)
        print("Download started...")

    # Slot method to update the download progress
    @Slot(int, int)
    def __update_download_progress(self, bytes_received, total_bytes):
        file = self.current_file()
        if file is None:
            return
        # Update the progress bar's maximum and current values based on the download progress
        self.files_on_download[file.id].setMaximum(total_bytes)
        self.files_on_download[file.id].setValue(bytes_received)

    # Slot method to handle component download completion
    @Slot(Path)
    def component_downloaded(self, filepath: Path):
        file = self.current_file()
        if file is None:
            return
        self.downloadPushButton.setState(DownloadStates.FINISHED)
        # Mark the file as existing (downloaded successfully)
        file.EXISTS = True
        # Remove the file id and progress bar from the files_on_download dictionary
        self.files_on_download.pop(file.id)
        print("Download Successful!")
        print("file at", filepath)

    # Check if a file is currently being downloaded
    def is_file_on_download(self):
        file = self.current_file()
        # Return True if the file is currently being downloaded (exists in files_on_download)
        return (file is not None) and (file.id in self.files_on_download)

    # Get the current file selected in the filetypeComboBox
    def current_file(self) -> File | None:
		# Return the corresponding File object based on the current file type in the combobox
        txt = self.ui.filetypeComboBox.currentText()
        # TODO Check why txt produces empty string
        if txt and FileTypes(txt):
            return self.component.files.get(FileTypes(txt))
        # ! should not return None. Investigate

    # Slot method to update the download button state based on the selected file type
    @Slot(str)
    def update_download_button_state(self):
        # Check if the selected file is currently being downloaded
        if self.is_file_on_download():
            self.downloadPushButton.setState(DownloadStates.IN_PROGRESS)

        # Check if the current file exists (downloaded successfully)
        elif self.current_file().EXISTS:
            # ! This produces an error when current_file() returns None
            self.downloadPushButton.setState(DownloadStates.FINISHED)
        else:
            # Set the download button state to 'DOWNLOAD' (not downloaded)
            self.downloadPushButton.setState(DownloadStates.DOWNLOAD)
