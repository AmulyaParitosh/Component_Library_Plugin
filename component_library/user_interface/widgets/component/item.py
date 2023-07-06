from PySide6.QtWidgets import QWidget

from .Ui_item_view import Ui_ComponentItemView


class ComponentItem(QWidget):

	def __init__(self, parent: QWidget, data: dict) -> None:

		super().__init__(parent)

		self.ui = Ui_ComponentItemView()
		self.ui.setupUi(self)

		self.data: dict[str, str] = data

		self.setupItem()


	def setupItem(self):
		self.ui.componentLabel.setText(self.data.get("name", "").capitalize())
		self.ui.thumbnail.setupThumbnail(self.data.get("thumbnail", ""))


	def mouseReleaseEvent(self, event) -> None:
		detailed_view = self.topLevelWidget().ui.componentDetail # type: ignore
		detailed_view.updateContent(self.data)
		self.topLevelWidget().ui.stackedWidget.setCurrentWidget(detailed_view) # type: ignore

		return super().mouseReleaseEvent(event)
