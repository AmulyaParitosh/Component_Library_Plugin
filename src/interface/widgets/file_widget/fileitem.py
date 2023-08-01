from pathlib import Path

from PySide6.QtWidgets import (QFileDialog, QFrame, QHBoxLayout, QLabel,
                               QListWidget, QListWidgetItem, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)


class FileItem(QFrame):
    # Custom QFrame class to represent an item for a file in the list.

    def __init__(self, parent=None) -> None:
        # Constructor to initialize the FileItem.

        super().__init__(parent)

        # Initialize the filepath to an empty string.
        self.filepath = ""

        # Create a horizontal layout for the FileItem.
        layout = QHBoxLayout()

        # Create a "Choose File" button and connect it to the open_file_dialog method.
        self.choose_file_btn = QPushButton("Choose File")
        self.choose_file_btn.clicked.connect(self.open_file_dialog)

        # Create a QLabel to display the filename of the chosen file.
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        # Add the buttons and label to the layout.
        layout.addWidget(self.choose_file_btn)
        layout.addWidget(self.label)

        # Set the layout for the FileItem.
        self.setLayout(layout)

    def open_file_dialog(self):
        # Method to open a file dialog and set the filepath.

        self.filepath, _ = QFileDialog.getOpenFileName(
            self,
            "Select Files",
        )
        if self.filepath:
            # Display the filename (without the path) in the label.
            self.label.setText(Path(self.filepath).name)


class FileList(QWidget):
    # Custom QWidget class to represent a list of files.

    def __init__(self, parent=None) -> None:
        # Constructor to initialize the FileList.

        super().__init__(parent)

        # Create a vertical layout for the FileList.
        layout = QVBoxLayout()

        # Create a QListWidget to display the list of files.
        self.list_widget = QListWidget()

        # Create an "Add File" button and connect it to the add_file method.
        self.add_file_btn = QPushButton("Add File")
        self.add_file_btn.clicked.connect(self.add_file)

        # Add the QListWidget and "Add File" button to the layout.
        layout.addWidget(self.list_widget)
        layout.addWidget(self.add_file_btn)

        # Set the layout for the FileList.
        self.setLayout(layout)

    def add_file(self):
        # Method to add a new file to the list.

        # Create a new FileItem widget representing the file.
        file_widget = FileItem()

        # Create a "Remove" button (denoted by "X") to remove the file from the list.
        cb = QPushButton("X")
        cb.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        file_widget.layout().addWidget(cb)

        # Create a QListWidgetItem to hold the FileItem widget.
        itemN = QListWidgetItem()

        # Set the size hint for the QListWidgetItem to match the size of the FileItem.
        itemN.setSizeHint(file_widget.sizeHint())

        # Simulate a click on the "Choose File" button to open the file dialog.
        file_widget.choose_file_btn.click()

        # Connect the "Remove" button's click event to the remove_item method.
        cb.clicked.connect(lambda: self.remove_item(itemN))

        # Add the QListWidgetItem to the QListWidget and set the FileItem widget as its associated widget.
        self.list_widget.addItem(itemN)
        self.list_widget.setItemWidget(itemN, file_widget)

    def remove_item(self, item: QListWidgetItem):
        # Method to remove a file from the list.

        # Take the QListWidgetItem (and its associated widget) from the QListWidget.
        self.list_widget.takeItem(self.list_widget.row(item))

    @property
    def filepaths(self) -> list[str]:
        # Property to get the list of filepaths currently in the list.
        return [self.list_widget.itemWidget(self.list_widget.item(i)).filepath for i in range(self.list_widget.count())]  # type: ignore
