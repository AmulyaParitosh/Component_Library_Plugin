from PySide6.QtWidgets import QWidget

from ....data import Component
from .Ui_item_view import Ui_ComponentItemView


class ComponentItem(QWidget):

	def __init__(self, parent: QWidget, data: Component) -> None:

		super().__init__(parent)

		self.ui = Ui_ComponentItemView()
		self.ui.setupUi(self)

		self.data: Component = data

		self.setupItem()


	def setupItem(self):
		self.ui.componentLabel.setText(self.data.name)
		self.ui.thumbnail.setupThumbnail(self.data.thumbnail)


	def mouseReleaseEvent(self, event) -> None:
		detailed_view = self.topLevelWidget().ui.componentDetail # type: ignore
		detailed_view.update_content(self)
		self.topLevelWidget().ui.stackedWidget.setCurrentWidget(detailed_view) # type: ignore

		return super().mouseReleaseEvent(event)
