import sys
from PySide6.QtWidgets import QApplication,  QFileDialog, QWidget, QGridLayout, QListWidget, QPushButton, QLabel
from pathlib import Path

from PySide6.QtWidgets import QPushButton, QLabel, QHBoxLayout, QFrame, QFileDialog






class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt File Dialog')
        self.setGeometry(100, 100, 400, 100)

        layout = QGridLayout()
        self.setLayout(layout)

        file_browse = QPushButton('Browse')
        file_browse.clicked.connect(self.open_file_dialog)

        self.file_list = QListWidget(self)

        layout.addWidget(QLabel('Selected Files:'), 0, 0)
        layout.addWidget(self.file_list, 1, 0)
        layout.addWidget(file_browse, 2, 0)

        self.show()

    def open_file_dialog(self):
        filenames, _ = QFileDialog.getOpenFileNames(
            self,
            "Select Files",
        )
        if filenames:
            self.file_list.addItems([str(Path(filename))
                                     for filename in filenames])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
