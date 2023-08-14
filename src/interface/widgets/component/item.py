import PySide6.QtGui
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

    def parentGrigView(self):
        return self.parent().parent().parent().parent()


    def mousePressEvent(self, event) -> None:
        self.topLevelWidget().widgetStack.append(self.parentGrigView())
        return super().mousePressEvent(event)


    def mouseReleaseEvent(self, event) -> None:
        self.topLevelWidget().display_detail_view(self, self.parentGrigView())
        return super().mouseReleaseEvent(event)
