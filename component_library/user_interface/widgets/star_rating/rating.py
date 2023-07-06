from __future__ import annotations

from enum import Enum

from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget


class Star(QLabel):

	class State(Enum):
		Empty = "component_library/user_interface/resources/emptystar.png"
		Filled = "component_library/user_interface/resources/filledstar.png"


	def __init__(self, parent):
		super().__init__(parent)
		self.setFixedSize(QSize(25, 25))
		self.setScaledContents(True)

		self.state = None

		self.setState(self.State.Empty)


	def setState(self, state: Star.State):

		if self.state == state:
			return

		self.state = state
		self.setPixmap(QPixmap(state.value))


class StarRating(QWidget):

	def __init__(self, parent: QWidget | None=None, default_value: float=0, max_value: int=5) -> None:
		super().__init__(parent)

		self.value: float = default_value
		self.max_value: int = max_value
		self.setupUi()


	def setupUi(self):
		self.hbox_layout = QHBoxLayout()
		self.setLayout(self.hbox_layout)

		self.value_label = QLabel()
		self.value_label.setFont(QFont('Arial', 14))
		self.hbox_layout.addWidget(self.value_label)

		for i in range(1, self.max_value+1):
			star = Star(self)
			if i <= self.value:
				star.setState(Star.State.Filled)
			self.hbox_layout.addWidget(star)


	def setRating(self, rating: float):
		self.value = rating
		self.value_label.setNum(self.value)

		for i in range(1, self.hbox_layout.count()):
			star: Star = self.hbox_layout.itemAt(i).widget() # type: ignore

			if i <= self.value:
				star.setState(Star.State.Filled)
			else:
				star.setState(Star.State.Empty)
