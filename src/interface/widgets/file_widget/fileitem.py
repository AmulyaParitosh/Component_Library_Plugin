import sys
from pathlib import Path

from PySide6.QtWidgets import (QApplication, QFileDialog, QFrame, QHBoxLayout,
                               QLabel, QListWidget, QListWidgetItem,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)


class FileItem(QFrame):
	def __init__(self, parent=None) -> None:
		super().__init__(parent)
		layout = QHBoxLayout()
		self.choose_file_btn = QPushButton("Choose File")
		self.choose_file_btn.clicked.connect(self.open_file_dialog)
		self.label = QLabel()
		self.label.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
		layout.addWidget(self.choose_file_btn)
		layout.addWidget(self.label)
		self.setLayout(layout)

	def open_file_dialog(self):
		filename, _ = QFileDialog.getOpenFileName(
			self,
			"Select Files",
		)
		if filename:
			self.label.setText(Path(filename).name)


class FileList(QWidget):
	def __init__(self, parent=None) -> None:
		super().__init__(parent)
		layout = QVBoxLayout()

		self.list_widget = QListWidget()
		self.add_file_btn = QPushButton("Add File")
		self.add_file_btn.clicked.connect(self.add_file)

		layout.addWidget(self.list_widget)
		layout.addWidget(self.add_file_btn)

		self.setLayout(layout)

	def add_file(self):
		file_widget = FileItem()

		cb = QPushButton("X")
		cb.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
		file_widget.layout().addWidget(cb)

		itemN = QListWidgetItem()
		itemN.setSizeHint(file_widget.sizeHint())
		file_widget.choose_file_btn.click()

		cb.clicked.connect(lambda: self.remove_item(itemN))

		self.list_widget.addItem(itemN)
		self.list_widget.setItemWidget(itemN, file_widget)

	def remove_item(self, item: QListWidgetItem):
		self.list_widget.takeItem(self.list_widget.row(item))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = FileList()
	window.show()
	sys.exit(app.exec())
