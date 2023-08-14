from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QWidget

from ..interface.forms import ComponetUploadDialog
from ..interface.views import GridView, LocalDetailedView, OnlineDetailedView
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
        self.local_manager = LocalStorageManager()
        self.widgetStack = []

        # Show the main window
        self.show()

        # Create an instance of the Ui_MainWindow class and assign it to the 'ui' attribute
        self.ui = Ui_MainWindow()
        self.setupUi()
        self.setupSignals()
        self.setupManagers()
        self.display_grid_view()

    # Method to set up the user interface (UI) for the main window
    def setupUi(self):
        self.ui.setupUi(self)

        self.onlineGridView = GridView(self)
        self.ui.stackedWidget.insertWidget(0, self.onlineGridView)

        self.onlineDetailView = OnlineDetailedView(self)
        self.ui.stackedWidget.insertWidget(1, self.onlineDetailView)
        self.onlineGridView.detailView = self.onlineDetailView


        self.localGridView = GridView(self)
        self.ui.stackedWidget.insertWidget(2, self.localGridView)

        self.localDetailView = LocalDetailedView(self)
        self.ui.stackedWidget.insertWidget(3, self.localDetailView)
        self.localGridView.detailView = self.localDetailView


    # Method to set up signal-slot connections for UI elements
    def setupSignals(self):
        # Connect the 'clicked' signal of the browseButton to the 'display_grid_view' method
        self.ui.browseButton.clicked.connect(self.display_grid_view)
        self.ui.uploadButton.clicked.connect(self.uploadButton_clicked)
        self.ui.LocalButton.clicked.connect(self.display_local_components)

    def setupManagers(self):
        # Set up the manager for the onlineGridView and the OnlineDetailedView
        self.onlineGridView.setupManager(self.repo_manager)
        self.onlineDetailView.setupManager(self.repo_manager)

        self.localGridView.setupManager(self.local_manager)
        self.localDetailView.setupManager(self.local_manager)

    # Method to display the detailed view of a selected item in the grid view
    def display_detail_view(self, item: ComponentItem, grid_view: GridView):
        grid_view.detailView.updateContent(item)
        self.ui.stackedWidget.setCurrentWidget(grid_view.detailView)

    def display_local_components(self):
        self.local_manager.request_components()
        self.ui.stackedWidget.setCurrentWidget(self.localGridView)

    # Slot method to switch to the grid view
    @Slot()
    def display_grid_view(self):
        # Set the onlineGridView as the current widget in the stacked widget
        self.ui.stackedWidget.setCurrentWidget(self.onlineGridView)

    @Slot()
    def toLastWidget(self):
        self.ui.stackedWidget.setCurrentWidget(self.widgetStack.pop())

    # Slot method to handle the uploadButton click
    @Slot()
    def uploadButton_clicked(self):
        # Create a component using the ComponetUploadDialog and the OnlineRepoManager
        data = ComponetUploadDialog.create_component(self, self.repo_manager)
        print(data)

    # Method to add a notification widget to the notification area in the main window
    def add_notification_widget(self, notification: QWidget):
        self.ui.notificationArea.addWidget(notification)
