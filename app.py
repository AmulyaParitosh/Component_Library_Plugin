#!.venv/bin/python
import sys

from PySide6.QtWidgets import QApplication

from src import Window

app = QApplication(sys.argv)
plugin = Window()
sys.exit(app.exec_())
