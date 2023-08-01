from PySide6.QtWidgets import QWidget

# Import the necessary components from the application.
from ....data import Component
from .Ui_item_view import Ui_ComponentItemView


class ComponentItem(QWidget):
    # Custom QWidget representing an item in a component view.

    def __init__(self, parent: QWidget, component: Component) -> None:
        # Constructor to initialize the ComponentItem.

        super().__init__(parent)

        # Initialize the user interface from the Ui_ComponentItemView.
        self.ui = Ui_ComponentItemView()
        self.ui.setupUi(self)

        # Store the component data associated with this item.
        self.component: Component = component

        # Set up the item's content.
        self.setupItem()

    def setupItem(self):
        # Method to set up the item's content.

        # Set the component name as the label text.
        self.ui.componentLabel.setText(self.component.metadata.name)

        # Set up the thumbnail using the Thumbnail widget.
        self.ui.thumbnail.setupThumbnail(self.component.metadata.thumbnail)

    def mouseReleaseEvent(self, event) -> None:
        # Override the mouseReleaseEvent to display the detail view of the component.

        # Call the top-level widget's display_detail_view method with this item.
        self.topLevelWidget().display_detail_view(self)

        # Call the base class's mouseReleaseEvent.
        return super().mouseReleaseEvent(event)
