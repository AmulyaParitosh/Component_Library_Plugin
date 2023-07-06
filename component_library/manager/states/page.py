from dataclasses import dataclass
from typing import Any

from PySide6.QtCore import QObject, Signal


@dataclass
class PageState(QObject):

	data: list[dict[str, Any]] = []
	total_items: int = 0
	page_no: int = 0
	total_pages = 0
	size: int = 18
	next_page: int | None = None
	prev_page: int | None = None


class PageStateManager(QObject):
	enable_next = Signal(bool)
	enable_prev = Signal(bool)
	page = PageState()

	def load_page(self, json_response: dict[str, Any]) -> PageState:
		self.page.data = json_response.get("items", [])
		self.page.total_items = json_response.get("total", 0)
		self.page.page_no = json_response.get("page_no", 1)
		self.page.size = json_response.get("per_page", 18)

		self.page.total_pages = (self.page.total_items + self.page.size -1) // self.page.size

		if self.page.page_no==1:
			self.page.prev_page = None
			self.enable_prev.emit(False)
		else:
			self.page.prev_page = self.page.page_no - 1
			self.enable_prev.emit(True)

		if (self.page.total_items - (self.page.page_no * self.page.size)) < self.page.size:
			self.page.next_page = None
			self.enable_next.emit(False)
		else:
			self.page.next_page = self.page.page_no + 1
			self.enable_next.emit(True)

		return self.page
