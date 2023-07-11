from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QComboBox


class CheckableComboBox(QComboBox):

	selectionUpdated = Signal(list)

	def __init__(self, parent=None):
		super().__init__(parent)
		self.view().pressed.connect(self.handleItemPressed)
		self._changed = False
		self._last_checked_items = []

	def handleItemPressed(self, index):
		item = self.model().itemFromIndex(index) # type: ignore
		if item.checkState() == Qt.CheckState.Checked:
			item.setCheckState(Qt.CheckState.Unchecked)
		else:
			item.setCheckState(Qt.CheckState.Checked)
		self._changed = True

	def hidePopup(self):
		if not self._changed:
			super().hidePopup()

			if self._last_checked_items != self.checked_items():
				self._last_checked_items = self.checked_items()

				self.selectionUpdated.emit(self.checked_items())
		self._changed = False

	def itemChecked(self, index):
		item = self.model().item(index, self.modelColumn()) # type: ignore
		return item.checkState() == Qt.CheckState.Checked

	def setItemChecked(self, index, checked=True):
		item = self.model().item(index, self.modelColumn()) # type: ignore
		if checked:
			item.setCheckState(Qt.CheckState.Checked)
		else:
			item.setCheckState(Qt.CheckState.Unchecked)

	def checked_items(self):
		checkedItems: list[str] = []

		for i in range(self.count()):
			item = self.model().item(i, 0) # type: ignore
			if item.checkState() == Qt.CheckState.Checked:
				checkedItems.append(item.text())

		return checkedItems

	def index_is_checked(self, index):
		item = self.model().item(index, 0) # type: ignore
		return item.checkState() == Qt.CheckState.Checked

	def make_pre_checked(self):

		for i in range(self.count()):
			item = self.model().item(i, 0) # type: ignore
			if item.checkState() == Qt.CheckState.Checked:
				continue
			item.setCheckState(Qt.CheckState.Checked)
		self._last_checked_items = self.checked_items()
