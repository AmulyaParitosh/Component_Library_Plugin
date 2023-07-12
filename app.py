import sys

from PySide6.QtWidgets import QApplication

from component_library import Window

app = QApplication(sys.argv)
plugin = Window()
sys.exit(app.exec())
