import sys

from PySide6.QtWidgets import QApplication

from component_library import Plugin

app = QApplication(sys.argv)
window = Plugin()
sys.exit(app.exec())
