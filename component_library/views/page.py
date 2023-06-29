from typing import Any
from PySide6.QtCore import QObject, Signal


class PageManager(QObject):


	enable_next = Signal(bool)
	enable_prev = Signal(bool)

	def __init__(self, parent: QObject | None = ...) -> None:
		super().__init__(parent)
		self.data: list = []
		self.total_items: int = 0
		self.page: int = 0
		self.total_pages = 0
		self.size: int = 18
		self.next_page: int | None = None
		self.prev_page: int | None = None

	def load_page(self, json_response: dict[str, Any]):
		self.data = json_response.get("items", [])
		self.total_items = json_response.get("total", 0)
		self.page = json_response.get("page", 1)
		self.size = json_response.get("per_page", 18)

		self.total_pages = (self.total_items + self.size -1) // self.size

		if self.page==1:
			self.prev_page = None
			self.enable_prev.emit(False)
		else:
			self.prev_page = self.page - 1
			self.enable_prev.emit(True)

		if (self.total_items - (self.page * self.size)) < self.size:
			self.next_page = None
			self.enable_next.emit(False)
		else:
			self.next_page = self.page + 1
			self.enable_next.emit(True)


	def to_begining(self):
		self.page = 1
