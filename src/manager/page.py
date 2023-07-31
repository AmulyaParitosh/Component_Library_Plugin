from dataclasses import dataclass, field
from typing import Any

from PySide6.QtCore import QObject, Signal
from ..api.local_api.storage_adapter import LocalData, LocalDataComp
from ..data import Component, DataFactory, DTypes
from ..config import Config

@dataclass
class PageStates(QObject):
	enable_next = Signal(bool)
	enable_prev = Signal(bool)

	data: list[Component] = field(default_factory=list)
	total_items: int = 0
	page_no: int = 0
	total_pages = 0
	size: int = 18
	next_page: int | None = None
	prev_page: int | None = None


	def __init__(self, *args, **kwargs):
		super(QObject, self).__init__()
		super().__init__(*args, **kwargs)


	def load_page(self, json_response: dict[str, Any]):
		self.load_page_data(json_response)
		self.calculate_pagination()
		return self

	def load_page_data(self, json_response: dict[str, Any]) -> None:
		self.data: list[Component] = DataFactory.load_many(data_list=json_response.get("items", []), dtype=DTypes.COMPONENT) # type: ignore
		self.update_existing_comps(self.data) # type: ignore

		self.total_items = json_response.get("total", 0)
		self.page_no = json_response.get("page", 1)
		self.size = json_response.get("per_page", 18)

	def update_existing_comps(self, components: list[Component]) -> None:
		with LocalData(Config.LOCAL_COMPONENT_PATH) as local_data:
			for component in components:
				self.update_existing_files_for_component(component, local_data)

	def update_existing_files_for_component(self, component: Component, local_data) -> None:
		for file in component.files:
			existing_comps = local_data["filetypes"].get(file.value, set())
			component.files[file].EXISTS = component.metadata.name in existing_comps


	def calculate_pagination(self) -> None:
		self.total_pages = (self.total_items + self.size - 1) // self.size

		if self.page_no == 1:
			self.prev_page = None
			self.enable_prev.emit(False)
		else:
			self.prev_page = self.page_no - 1
			self.enable_prev.emit(True)

		if (self.total_items - (self.page_no * self.size)) < 0:
			self.next_page = None
			self.enable_next.emit(False)
		else:
			self.next_page = self.page_no + 1
			self.enable_next.emit(True)
