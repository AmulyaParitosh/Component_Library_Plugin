from PySide6.QtWidgets import QWidget

from .ui.Ui_items_view import Ui_itemsView


class ItemsView(QWidget, Ui_itemsView):

	def __init__(self, data) -> None:
		super().__init__()
		self.setupUi(self)

		self.scrollAreaContentItemsWidget.populate(data)

		self.show()
