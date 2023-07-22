from PySide6.QtWidgets import QWidget

from ....data import Component
from .Ui_item_view import Ui_ComponentItemView


class ComponentItem(QWidget):

	def __init__(self, parent: QWidget, component: Component) -> None:

		super().__init__(parent)

		self.ui = Ui_ComponentItemView()
		self.ui.setupUi(self)
		self.component: Component = component

		self.setupItem()


	def setupItem(self):
		self.ui.componentLabel.setText(self.component.metadata.name)
		self.ui.thumbnail.setupThumbnail(self.component.metadata.thumbnail)


	def mouseReleaseEvent(self, event) -> None:
		self.topLevelWidget().display_detail_view(self)
		return super().mouseReleaseEvent(event)
