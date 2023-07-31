import contextlib
from enum import Enum

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton


class StatefullPushButton(QPushButton):

	def __init__(self, parent=None):
		super().__init__(parent)
		self.states = {}
		self.button = QPushButton()

	def register_state(self, state: Enum, slot: Slot|None, text: str, enable: bool):
		self.states[state] = {
			"slot" : slot,
			"text" : text,
			"enable" : enable,
		}

	def setState(self, state: Enum):
		if state not in self.states:
			raise ValueError(f"{state} not registered!")

		state_data = self.states[state]

		self.setText(state_data["text"])

		for key, value in self.states.items():
			if key == state:
				continue
			with contextlib.suppress(Exception):
				self.clicked.disconnect(value["slot"])
		if state_data["slot"]:
			self.clicked.connect(state_data["slot"])

		self.setEnabled(state_data["enable"])
