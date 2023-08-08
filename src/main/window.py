from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QWidget

from ..interface.forms import ComponetUploadDialog
from ..interface.views import GridView, OnlineDetailedView
from ..interface.widgets import ComponentItem
from ..manager import LocalStorageManager, OnlineRepoManager
from .Ui_window import Ui_MainWindow


# Main application window class
class Window(QMainWindow):

    # Constructor for the Window class
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        # Initialize the OnlineRepoManager
        self.repo_manager = OnlineRepoManager()
        # self.local_manager = LocalStorageManager()

        # Show the main window
        self.show()

        # Create an instance of the Ui_MainWindow class and assign it to the 'ui' attribute
        self.ui = Ui_MainWindow()
        self.setupUi()
        self.setupSignals()
        self.setupManagers()

    # Method to set up the user interface (UI) for the main window
    def setupUi(self):
        self.ui.setupUi(self)

        # TODO add self.localDetailView once it's defined

        # Create an instance of the onlineGridView class and insert it into the stacked widget
        self.onlineGridView = GridView(self)
        self.ui.stackedWidget.insertWidget(0, self.onlineGridView)

        # self.localGridView = GridView(self)
        # self.ui.stackedWidget.insertWidget(1, self.localGridView)

        # Create an instance of the OnlineDetailedView class and insert it into the stacked widget
        self.onlineDetailView = OnlineDetailedView(self)
        self.ui.stackedWidget.insertWidget(2, self.onlineDetailView)

    # Method to set up signal-slot connections for UI elements
    def setupSignals(self):
        # Connect the 'clicked' signal of the browseButton to the 'display_grid_view' method
        self.ui.browseButton.clicked.connect(self.display_grid_view)
        self.ui.uploadButton.clicked.connect(self.uploadButton_clicked)

    def setupManagers(self):
        # Set up the manager for the onlineGridView and the OnlineDetailedView
        self.onlineGridView.setupManager(self.repo_manager)
        self.onlineDetailView.setupManager(self.repo_manager)

        # self.localGridView.setupManager(self.local_manager)

    # Method to display the detailed view of a selected item in the grid view
    def display_detail_view(self, item: ComponentItem):
        # Update the content of the OnlineDetailedView with the selected item
        self.onlineDetailView.updateContent(item)
        # Switch to the OnlineDetailedView by setting it as the current widget in the stacked widget
        self.ui.stackedWidget.setCurrentWidget(self.onlineDetailView)

    # Slot method to switch to the grid view
    @Slot()
    def display_grid_view(self):
        # TODO make it a partial funcation with the main function accepting a view
        # Set the onlineGridView as the current widget in the stacked widget
        self.ui.stackedWidget.setCurrentWidget(self.onlineGridView)

    # Slot method to handle the uploadButton click
    @Slot()
    def uploadButton_clicked(self):
        # Create a component using the ComponetUploadDialog and the OnlineRepoManager
        data = ComponetUploadDialog.create_component(self, self.repo_manager)
        print(data)

    # Method to add a notification widget to the notification area in the main window
    def add_notification_widget(self, notification: QWidget):
        self.ui.notificationArea.addWidget(notification)
