from functools import wraps
from typing import Callable

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from ....data import DTypes
from ....manager import ManagerInterface, OnlineRepoManager
from ....manager.page import PageStates
from ...widgets.overlay import LoadingOverlay
from ..base_view import BaseView
from .Ui_grid_view import Ui_gridView


class GridView(BaseView):
    # Declare a class attribute 'manager' of type OnlineRepoManager
    manager: OnlineRepoManager

    # Constructor for the GridView class
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        # Create an instance of the UI class for the GridView
        self.ui = Ui_gridView()

        # Call the setupUi and setupSignals methods
        self.setupUi()
        self.setupSignals()

    # Initialize the user interface elements
    def setupUi(self):
        self.ui.setupUi(self)

        # Create a loading overlay widget for the scroll area
        self.loading_overlay = LoadingOverlay(self.ui.scrollArea)

        # Set the pre-checked items in the fileTypeComboBox
        self.ui.fileTypeComboBox.make_pre_checked()

    # Connect signals to their respective slots
    def setupSignals(self):
        self.ui.searchLineEdit.returnPressed.connect(self.search_enter_pressed)
        self.ui.nextButton.clicked.connect(self.on_nextButton_clicked)
        self.ui.prevButton.clicked.connect(self.on_prevButton_clicked)
        self.ui.sortComboBox.currentTextChanged.connect(self.on_sortComboBox_change)
        self.ui.orderComboBox.currentTextChanged.connect(self.on_ordCombBox_change)
        self.ui.fileTypeComboBox.selectionUpdated.connect(self.on_fileTypeComboBox_change)
        self.ui.tagBar.tags_edited.connect(self.on_tagBar_tag_edited)

    # Set up the manager for the GridView
    def setupManager(self, manager: ManagerInterface):
        super().setupManager(manager)

        # Connect signals for component loading and enabling next/previous buttons
        self.manager.component_loaded.connect(self.components_response_handler)
        self.manager.page_states.enable_next.connect(self.ui.nextButton.setEnabled)
        self.manager.page_states.enable_prev.connect(self.ui.prevButton.setEnabled)

        # Perform initial loading of data
        self.initial_load()

    # Update the content based on the given PageStates object
    def updateContent(self, page: PageStates):
        self.ui.scrollAreaContentItemsWidget.repopulate(page.data)
        self.ui.pageLable.setText(f"{page.page_no} / {page.total_pages}")
        self.loading_overlay.loading = False

    # Decorator function to display loading overlay during method execution
    @staticmethod
    def loading(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Extract 'self' from arguments and set loading_overlay to True
            self, *args = args
            self.loading_overlay.loading = True
            # Set the vertical scrollbar value to 0 to reset the scroll position
            self.ui.scrollArea.verticalScrollBar().setValue(0)
            return func(self, *args, **kwargs)
        return wrapper

    # Slot method to handle components response from the manager
    @Slot()
    def components_response_handler(self):
        self.updateContent(self.manager.page_states)

    @loading
    def initial_load(self):
        # Reload the page data and set tag suggestions for the tagBar from the database
        self.manager.reload_page()
        self.ui.tagBar.set_suggestions(self.manager.load_from_db(DTypes.TAG)) # type: ignore

    @loading
    @Slot()
    def on_nextButton_clicked(self):
        # Request loading the next page of data
        self.manager.next_page()

    @loading
    @Slot()
    def on_prevButton_clicked(self):
        # Request loading the previous page of data
        self.manager.prev_page()

    @loading
    @Slot()
    def search_enter_pressed(self):
        # Perform search with the entered text from searchLineEdit
        self.manager.search(self.ui.searchLineEdit.text())

    @loading
    @Slot(str)
    def on_sortComboBox_change(self, value: str):
        # Perform sorting based on the selected value and the orderComboBox's current text
        self.manager.sort(
            by=value,
            order=self.ui.orderComboBox.currentText(),
        )

    @loading
    @Slot(str)
    def on_ordCombBox_change(self, value: str):
        # Perform sorting based on the sortComboBox's current text and the selected value
        self.manager.sort(
            by=self.ui.sortComboBox.currentText(),
            order=value,
        )

    @loading
    @Slot(list)
    def on_fileTypeComboBox_change(self, checked_items: list[str]):
        # Perform filtering based on checked filetypes and tags from tagBar
        self.manager.filter(
            filetypes=checked_items,
            tags=self.ui.tagBar.tags,
        )

    @loading
    @Slot()
    def on_tagBar_tag_edited(self, tags: list[str]):
        # Update the manager's query tags and perform filtering based on filetypes and tags
        self.manager.query.tags = tags
        self.manager.filter(
            filetypes=self.ui.fileTypeComboBox.checked_items(),
            tags=tags,
        )
