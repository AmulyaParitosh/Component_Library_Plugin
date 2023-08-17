#!.venv/bin/python
import sys

from PySide6.QtWidgets import QApplication

from src import Window

app = QApplication(sys.argv)

# TODO: Instantiate the Window class from the 'src' module
plugin = Window()

sys.exit(app.exec())
