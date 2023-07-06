import sys

from PySide6.QtWidgets import QApplication

from component_library import Window

app = QApplication(sys.argv)
plugin = Window("http://127.0.0.1:5000")
sys.exit(app.exec())
