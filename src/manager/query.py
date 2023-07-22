from abc import ABC, abstractproperty
from typing import Any, Union

QueryParam = Union[Any, str]

class ComponentQueryInterface(ABC):
	# TODO introduce abstraction here
	@abstractproperty
	def page(self) -> QueryParam:...

	@abstractproperty
	def page_size(self) -> QueryParam:...

	@abstractproperty
	def search_key(self) -> QueryParam:...

	@abstractproperty
	def sort_by(self) -> QueryParam:...

	@abstractproperty
	def sort_ord(self) -> QueryParam:...

	@abstractproperty
	def file_types(self) -> QueryParam:...

	@abstractproperty
	def tags(self) -> QueryParam:...

	@abstractproperty
	def columns(self) -> QueryParam:...



class RepoComponentQuery(ComponentQueryInterface):

	def __init__(self) -> None:
		self.__page: int | None = 1
		self.__page_size: int | None = 18
		self.__search_key: str | None = None
		self.__sort_by: str | None = "name"
		self.__sort_ord: str  | None = "asc"
		self.__file_types: list[str] | None = None
		self.__tags: list[str] | None = None
		self.__columns: list[str] | None = None

	@property
	def page(self) -> str:
		return '' if self.__page is None else f"page={self.__page}"

	@page.setter
	def page(self, value: int|None) -> None:
		self.__page = value

	@property
	def page_size(self) -> str:
		return "" if self.__page_size is None else f"page_size={self.__page_size}"

	@page_size.setter
	def page_size(self, value: int|None) -> None:
		self.__page_size = value

	@property
	def search_key(self) -> str:
		return "" if self.__search_key is None else f"search_key={self.__search_key}"

	@search_key.setter
	def search_key(self, value: str|None) -> None:
		self.__search_key = value

	@property
	def sort_by(self) -> str:
		return "" if self.__sort_by is None else f"sort_by={self.__sort_by}"

	@sort_by.setter
	def sort_by(self, value: str|None) -> None:
		if value in ("Name", "Rating"):
			value = value.lower()
		elif value == "Created":
			value = "created_at"
		elif value == "Updated":
			value = "updated_at"
		else:
			raise ValueError()

		self.__sort_by = value

	@property
	def sort_ord(self) -> str:
		return "" if self.__sort_ord is None else f"sort_ord={self.__sort_ord}"

	@sort_ord.setter
	def sort_ord(self, value: str|None) -> None:
		if value is None:
			pass
		elif value.lower() == "ascending":
			value = "asc"
		elif value.lower() == "descending":
			value = "desc"
		else:
			raise ValueError()

		self.__sort_ord = value

	@property
	def file_types(self) -> str:
		if self.__file_types is None or len(self.__file_types) == 0:
			return ""

		return "&".join(f"file_types%5B%5D={ft.replace(' ', '%20')}" for ft in self.__file_types)

	@file_types.setter
	def file_types(self, value: list[str]|None) -> None:
		if value != None:
			value = [v.strip() for v in value if v]
		self.__file_types = value

	@property
	def tags(self):
		if self.__tags is None or len(self.__tags) == 0:
			return ""

		return "&".join(f"tags%5B%5D={t.replace(' ', '%20')}" for t in self.__tags)

	@tags.setter
	def tags(self, value: list[str]|None) -> None:
		if value != None:
			value = [v.strip() for v in value if v]
		self.__tags = value

	@property
	def columns(self) -> str:
		if self.__columns is None or len(self.__columns) == 0:
			return ""

		return "&".join(f"columns%5B%5D={t.replace(' ', '%20')}" for t in self.__columns)

	@columns.setter
	def columns(self, value: list[str]|None) -> None:
		if value != None:
			value = [v.strip() for v in value if v]
		self.__columns = value


class LocalComponentQuery(ComponentQueryInterface):...
