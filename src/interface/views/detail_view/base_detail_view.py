from abc import abstractmethod

from PySide6.QtWidgets import QWidget

from ....data import Component
from ...widgets import DetailedWidget, Thumbnail
from ..base_view import BaseView


# Base class for detailed views of components
class BaseDetailedView(BaseView):

    # Class attribute to store files being downloaded with their corresponding progress bars
    files_on_download = {}
    # Class attribute to store the thumbnail widget
    thumbnail: Thumbnail = None  # type: ignore
    # Class attribute to store the component being displayed in the detailed view
    component: Component = None  # type: ignore

    # Constructor for the BaseDetailedView class
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        # Create an instance of DetailedWidget and assign it to the 'ui' attribute
        self.ui = DetailedWidget()

    # Abstract method that must be implemented in derived classes
    @abstractmethod
    def backPushButton_click(self):...
        # This method should handle the backPushButton click in the detailed view
        # Its implementation will vary in the derived classes.
        # The 'abstractmethod' decorator makes it mandatory to implement this method in the derived classes.

    # Method to add a control widget to the control area in the detailed view
    def addControlWidget(self, widget: QWidget):
        self.ui.controlArea.addWidget(widget)

    # Method to remove a control widget from the control area in the detailed view
    def removeControlWidget(self, widget: QWidget):
        self.ui.controlArea.removeWidget(widget)

    # Method to add a progress widget to the processes area in the detailed view
    def addProgressWidget(self, widget: QWidget):
        self.ui.processesArea.addWidget(widget)
