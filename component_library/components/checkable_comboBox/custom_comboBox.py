from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import QComboBox


class CheckableComboBox(QComboBox):

	itemChecked = Signal(list)

	def __init__(self, parent):
		super().__init__()
		self.setParent(parent) # type: ignore
		self.view().pressed.connect(self.handle_item_pressed)
		self.setModel(QStandardItemModel(self))


	def handle_item_pressed(self, index):

		item = self.model().itemFromIndex(index) # type: ignore

		if item.checkState() == Qt.CheckState.Checked:
			item.setCheckState(Qt.CheckState.Unchecked)
		else:
			item.setCheckState(Qt.CheckState.Checked)

		checked_items = self.checked_items()
		self.itemChecked.emit(checked_items)

	def index_is_checked(self, index):
		item = self.model().item(index, 0) # type: ignore
		return item.checkState() == Qt.CheckState.Checked


	def checked_items(self):
		checkedItems: list[str] = []

		for i in range(self.count()):
			item = self.model().item(i, 0) # type: ignore
			if item.checkState() == Qt.CheckState.Checked:
				checkedItems.append(item.text())

		return checkedItems

	def make_pre_checked(self):

		for i in range(self.count()):
			item = self.model().item(i, 0) # type: ignore
			if item.checkState() == Qt.CheckState.Checked:
				continue
			item.setCheckState(Qt.CheckState.Checked)
