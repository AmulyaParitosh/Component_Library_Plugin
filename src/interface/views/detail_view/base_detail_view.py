from abc import abstractmethod

from PySide6.QtWidgets import QWidget

from ....data import Component
from ...widgets import DetailedWidget, Thumbnail
from ..base_view import BaseView


class BaseDetailedView(BaseView):

	files_on_download = {}
	thumbnail: Thumbnail = None # type: ignore
	component: Component = None # type: ignore

	def __init__(self, parent: QWidget | None = None) -> None:
		super().__init__(parent)
		self.ui = DetailedWidget()

	@abstractmethod
	def on_backPushButton_click(self):...

	def addControlWidget(self, widget: QWidget):
		self.ui.controlArea.addWidget(widget)

	def removeControlWidget(self, widget: QWidget):
		self.ui.controlArea.removeWidget(widget)

	def addProgressWidget(self, widget: QWidget):
		self.ui.processesArea.addWidget(widget)
