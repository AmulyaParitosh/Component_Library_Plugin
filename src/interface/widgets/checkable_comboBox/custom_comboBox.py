from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QComboBox


class CheckableComboBox(QComboBox):
    # Custom QComboBox that supports checkable items.

    selectionUpdated = Signal(list)

    def __init__(self, parent=None):
        # Constructor to initialize the CheckableComboBox.

        super().__init__(parent)

        # Connect the pressed signal of the view to handleItemPressed method.
        self.view().pressed.connect(self.handleItemPressed)

        # A flag to track if the combobox items have been changed.
        self._changed = False

        # A list to store the last checked items.
        self._last_checked_items = []

    def handleItemPressed(self, index):
        # Method to handle item presses and toggle the check state.

        item = self.model().itemFromIndex(index)  # Get the model item from index.

        # Toggle the check state when an item is pressed.
        if item.checkState() == Qt.CheckState.Checked:
            item.setCheckState(Qt.CheckState.Unchecked)
        else:
            item.setCheckState(Qt.CheckState.Checked)

        # Set the changed flag to True.
        self._changed = True

    def hidePopup(self):
        # Override the hidePopup method to emit the selectionUpdated signal.

        if not self._changed:
            # Call the original hidePopup if there were no changes.
            super().hidePopup()

            # Emit the selectionUpdated signal if the checked items have changed.
            if self._last_checked_items != self.checked_items():
                self._last_checked_items = self.checked_items()
                self.selectionUpdated.emit(self.checked_items())

        # Reset the changed flag to False.
        self._changed = False

    def itemChecked(self, index):
        # Method to check if a specific item is checked.

        item = self.model().item(index, self.modelColumn())
        return item.checkState() == Qt.CheckState.Checked

    def setItemChecked(self, index, checked=True):
        # Method to set the check state of a specific item.

        item = self.model().item(index, self.modelColumn())
        if checked:
            item.setCheckState(Qt.CheckState.Checked)
        else:
            item.setCheckState(Qt.CheckState.Unchecked)

    def checked_items(self):
        # Method to get a list of checked item texts.

        checkedItems: list[str] = []

        for i in range(self.count()):
            item = self.model().item(i, 0)
            if item.checkState() == Qt.CheckState.Checked:
                checkedItems.append(item.text())

        return checkedItems

    def index_is_checked(self, index):
        # Method to check if a specific index is checked.

        item = self.model().item(index, 0)
        return item.checkState() == Qt.CheckState.Checked

    def make_pre_checked(self):
        # Method to set all items as checked initially.

        for i in range(self.count()):
            item = self.model().item(i, 0)
            if item.checkState() == Qt.CheckState.Checked:
                continue
            item.setCheckState(Qt.CheckState.Checked)

        # Store the checked items in _last_checked_items.
        self._last_checked_items = self.checked_items()
