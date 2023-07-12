from typing import Any, Union

from ..utils import Interface

QueryParam = Union[Any, str]

class ComponentQueryInterface(Interface):
	page: QueryParam
	page_size: QueryParam
	search_key: QueryParam
	sort_by: QueryParam
	sort_ord: QueryParam
	file_types: QueryParam
	tags: QueryParam
	columns: QueryParam


class RepoComponentQuery:

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
		if self.__page == None:
			return ''
		return f"page={self.__page}"

	@page.setter
	def page(self, value: int|None) -> None:
		self.__page = value

	@property
	def page_size(self) -> str:
		if self.__page_size == None:
			return ""
		return f"page_size={self.__page_size}"

	@page_size.setter
	def page_size(self, value: int|None) -> None:
		self.__page_size = value

	@property
	def search_key(self) -> str:
		if self.__search_key == None:
			return ""
		return f"search_key={self.__search_key}"

	@search_key.setter
	def search_key(self, value: str|None) -> None:
		self.__search_key = value

	@property
	def sort_by(self) -> str:
		if self.__sort_by == None:
			return ""
		return f"sort_by={self.__sort_by}"

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
		if self.__sort_ord == None:
			return ""
		return f"sort_ord={self.__sort_ord}"

	@sort_ord.setter
	def sort_ord(self, value: str|None) -> None:
		if value == None:
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
		if self.__file_types == None or len(self.__file_types) == 0:
				return ""

		return "&".join(f"file_types%5B%5D={ft.replace(' ', '%20')}" for ft in self.__file_types)

	@file_types.setter
	def file_types(self, value: list[str]|None) -> None:
		if value == None:
			pass
		else:
			value = [v.strip() for v in value if v]
		self.__file_types = value

	@property
	def tags(self):
		if self.__tags == None or len(self.__tags) == 0:
				return ""

		return "&".join(f"tags%5B%5D={t.replace(' ', '%20')}" for t in self.__tags)

	@tags.setter
	def tags(self, value: list[str]|None) -> None:
		if value == None:
			pass
		else:
			value = [v.strip() for v in value if v]
		self.__tags = value

	@property
	def columns(self) -> str:
		if self.__columns == None or len(self.__columns) == 0:
				return ""

		return "&".join(f"columns%5B%5D={t.replace(' ', '%20')}" for t in self.__columns)

	@columns.setter
	def columns(self, value: list[str]|None) -> None:
		if value == None:
			pass
		else:
			value = [v.strip() for v in value if v]
		self.__columns = value


class LocalComponentQuery:...
