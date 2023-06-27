import sys

from PySide6.QtWidgets import QApplication

from component_library.views import ItemsView

app = QApplication(sys.argv)
window = ItemsView()
sys.exit(app.exec())
