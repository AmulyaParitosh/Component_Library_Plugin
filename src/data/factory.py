from dataclasses import asdict, is_dataclass
from functools import lru_cache
from typing import TYPE_CHECKING, Any, Callable

from PySide6.QtCore import QEventLoop
from PySide6.QtNetwork import QNetworkRequest

from ..api import getApi
from ..config import API_URL
from .data_types import DTypes

if TYPE_CHECKING:
	from ..api import CMSReply


class DataFactory:
	_registry: dict[DTypes, type] = {}

	@classmethod
	def __init_subclass__(cls, /, dtype: DTypes|None, **kwargs):
		super().__init_subclass__(**kwargs)
		if dtype:
			cls._registry[dtype] = cls

	def __new__(cls, dtype: DTypes = DTypes.GENERIC, **kwargs: dict[str, Any]):
		subclass: type = cls._registry.get(dtype, DataFactory)
		return super().__new__(subclass) # type: ignore

	def __is_field(self, attr):
		return not any((
			attr.startswith("_"),
			isinstance(getattr(self, attr), Callable),
		))


	def serialize(self, base_info: bool = False):
		if not is_dataclass(self):
			return {attr: getattr(self, attr) for attr in dir(self) if self.__is_field(attr)}
		data = asdict(self)
		if not base_info:
			for key in ("id", "created_at", "updated_at"):
				data.pop(key)
		return data

	@staticmethod
	def load_many(data_list: list, dtype: DTypes = DTypes.GENERIC):
		return [DataFactory(dtype=dtype, **data) for data in data_list]

	@classmethod
	@lru_cache
	def load_from_db(cls, dtype: DTypes):
		return cls.load_many(DbDataLoader(dtype).data, dtype)


class DbDataLoader:
	def __init__(self, dtype: DTypes) -> None:
		reply: CMSReply = getApi(API_URL).read(QNetworkRequest(self.get_route(dtype)))
		loop = QEventLoop()
		reply.finished.connect(loop.quit)
		loop.exec()
		self.data: list = reply.data.get("items", [])

	@staticmethod
	def get_route(dtype: DTypes) -> str:
		match dtype:
			case DTypes.TAG:
				return "tag"
			case DTypes.LICENSE:
				return "license/all"
			case _:
				return ""
