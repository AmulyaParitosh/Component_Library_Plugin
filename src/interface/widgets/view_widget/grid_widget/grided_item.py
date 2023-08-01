from PySide6.QtWidgets import QGridLayout, QWidget

from .....data import Component
from ...component import ComponentItem


class GridItemWidget(QWidget):
    # Custom QWidget class to display a grid of ComponentItem widgets.

    def __init__(self) -> None:
        # Constructor to initialize the GridItemWidget.

        super().__init__()

        # Create a QGridLayout to arrange the widgets in a grid.
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # Set the maximum number of columns and initialize current row and column indices.
        self.__MAX_COL = 3
        self.__cur_row = 0
        self.__cur_col = 0

    def reset(self):
        # Method to reset the grid by removing all widgets and resetting indices.

        # Remove all widgets from the grid layout.
        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().deleteLater()

        # Reset the maximum number of columns and current row and column indices.
        self.__MAX_COL = 3
        self.__cur_row = 0
        self.__cur_col = 0

    def repopulate(self, components: list[Component]):
        # Method to repopulate the grid with a new list of components.

        # Reset the grid first.
        self.reset()

        # Populate the grid with the new list of components.
        self.populate(components)

    def populate(self, components: list[Component]):
        # Method to populate the grid with a list of components.

        # Add each component as a ComponentItem widget to the grid.
        for data in components:
            component = ComponentItem(self, data)
            self.addItem(component)

    def __next_row(self):
        # Method to calculate the next row index for the grid.

        self.__cur_row = self.__cur_col // self.__MAX_COL
        return self.__cur_row

    def __next_col(self):
        # Method to calculate the next column index for the grid.

        self.__cur_col += 1
        return (self.__cur_col - 1) % self.__MAX_COL

    def addItem(self, item: ComponentItem):
        # Method to add a ComponentItem widget to the grid.

        # Add the item to the grid layout at the calculated row and column indices.
        self.grid.addWidget(item, self.__next_row(), self.__next_col())
