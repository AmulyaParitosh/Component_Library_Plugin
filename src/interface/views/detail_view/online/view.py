
# SPDX-License-Identifier: MIT
# --------------------------------------------------------------
#|																|
#|             Copyright 2023 - 2023, Amulya Paritosh			|
#|																|
#|  This file is part of Component Library Plugin for FreeCAD.	|
#|																|
#|               This file was created as a part of				|
#|              Google Summer Of Code Program - 2023			|
#|																|
# --------------------------------------------------------------

from enum import Enum, auto
from pathlib import Path

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QProgressBar, QWidget

from .....manager import ManagerInterface, OnlineRepoManager
from ....widgets import ComponentItem, StatefullPushButton
from ..base_detail_view import BaseDetailedView


# Enum to represent different download states
class DownloadStates(Enum):
    AVAILABLE = auto()
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
        super().setupUi()

        self.downloadPushButton = StatefullPushButton(self)
        self.addControlWidget(self.downloadPushButton)

    # Connect signals to their respective slots
    def setupSignals(self):
        self.downloadPushButton.register_state(
            DownloadStates.AVAILABLE,
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
            self.removeButton_click,
            "Remove",
            True
        )

        self.ui.filetypeComboBox.currentTextChanged.connect(self.update_download_button_state)

    # Set up the manager for the OnlineDetailedView
    def setupManager(self, manager: ManagerInterface):
        super().setupManager(manager)

    # Update the content based on the given ComponentItem
    def updateContent(self, comp_item: ComponentItem):
        super().updateContent(comp_item)
        self.update_download_button_state()


    # Slot method to handle downloadButton click
    @Slot()
    def downloadButton_click(self):
        file = self.current_file()
        if file is None:
            return

        # Add a progress bar for the file being downloaded
        self.files_on_download[file.id] = QProgressBar()
        self.topLevelWidget().add_notification_widget(self.files_on_download[file.id])
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
        file.exists = True
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


    # Slot method to update the download button state based on the selected file type
    @Slot(str)
    def update_download_button_state(self):
        # Check if the selected file is currently being downloaded
        if self.is_file_on_download():
            self.downloadPushButton.setState(DownloadStates.IN_PROGRESS)

        # Check if the current file exists (downloaded successfully)
        elif self.current_file().exists:
            # ! This produces an error when current_file() returns None
            self.downloadPushButton.setState(DownloadStates.FINISHED)
        else:
            # Set the download button state to 'AVAILABLE' (not downloaded)
            self.downloadPushButton.setState(DownloadStates.AVAILABLE)

    @Slot()
    def removeButton_click(self):
        self.manager.remove_file(self.component, self.current_file().type)
        self.downloadPushButton.setState(DownloadStates.AVAILABLE)
        # ! SOME errors are occuring
