from dataclasses import InitVar, asdict, dataclass, field, is_dataclass
from enum import Enum
from functools import lru_cache
from typing import Any, Callable

from PySide6.QtCore import QEventLoop, QObject, Signal
from PySide6.QtNetwork import QNetworkRequest

from ..api import CMSReply, getApi
from ..config import API_URL


class DTypes(Enum):
	COMPONENT = "component"
	FILE = "file"
	LICENSE = "license"
	METADATA = "metadata"
	TAG = "tag"
	GENERIC = "generic"


class DataFactory:
	_registry: dict[DTypes, type] = {}

	@classmethod
	def __init_subclass__(cls, /, d_type: DTypes|None, **kwargs):
		super().__init_subclass__(**kwargs)
		if d_type:
			cls._registry[d_type] = cls

	def __new__(cls, d_type: DTypes = DTypes.GENERIC, **kwargs: dict[str, Any]):
		subclass: type | type[GenericData] = cls._registry.get(d_type, GenericData)
		return super().__new__(subclass) # type: ignore

	def __is_field(self, attr):
		if any((
			attr.startswith("_"),
			isinstance(getattr(self, attr), Callable),
		)):
			return False
		return True


	def serialize(self, base_info: bool = False):
		if is_dataclass(self):
			data = asdict(self) # type: ignore
			if not base_info:
				for key in ("id", "created_at", "updated_at"):
					data.pop(key)
			return data
		else:
			return {attr: getattr(self, attr) for attr in dir(self) if self.__is_field(attr)}

	@staticmethod
	def load_many(data_list: list, d_type: DTypes = DTypes.GENERIC):
		many = []
		for data in data_list:
			many.append(DataFactory(d_type=d_type, **data))
		return many

	@classmethod
	@lru_cache
	def load_from_db(cls, d_type: DTypes):
		data = DbDataLoader(d_type).data.get("items", [])
		return cls.load_many(data, d_type)


class DbDataLoader(QObject):
	data_loaded = Signal(DTypes, list)

	def __init__(self, d_type: DTypes) -> None:
		super().__init__()
		reply: CMSReply = getApi(API_URL).read(QNetworkRequest(d_type.value))
		loop = QEventLoop()
		reply.finished.connect(loop.quit)
		loop.exec()
		self.data = reply.data


class GenericData(DataFactory, d_type=DTypes.GENERIC):
	def __init__(self, **kwargs):
		kwargs.pop("d_type", None)
		for k, v in kwargs.items():
			setattr(self, k, v)


@dataclass(kw_only=True)
class _Data(DataFactory, d_type=None):
	d_type : InitVar[DTypes|None] = None
	id: str
	created_at: str
	updated_at: str

	def __post_init__(self, *args, **kwargs):...


class FileTypes(Enum):
	STL = "stl"
	FCSTD = "fcstd"
	FCSTD1 = "fcstd1"
	STEP = "step"
	STP = "stp"


@dataclass(kw_only=True)
class File(_Data, d_type=DTypes.FILE):
	metadata_id: str
	updated_at: str
	size: int
	url: str
	type : FileTypes = field(default=None) # type: ignore

	def __post_init__(self, *args, **kwargs):
		self.type = FileTypes(self.type.get("name")) # type: ignore


@dataclass(kw_only=True)
class License(_Data, d_type=DTypes.LICENSE):
    identifier: str
    fullname: str
    license_page: str
    fsf_free: bool
    osi_approved: bool


@dataclass(kw_only=True)
class Metadata(_Data, d_type=DTypes.METADATA):
	license_id: str
	name: str
	author: str
	maintainer: str
	description: str
	rating: float
	thumbnail: str
	version: str


@dataclass(kw_only=True)
class Tag(_Data, d_type=DTypes.TAG):
	label: str = ""


@dataclass(kw_only=True)
class Component(Metadata, d_type=DTypes.COMPONENT):
	files: dict[FileTypes, File]
	license: License
	tags: list[Tag]

	def __post_init__(self, *args, **kwargs):
		self.files = {file.type : file for file in
			DataFactory.load_many(data_list=self.files, d_type=DTypes.FILE) # type: ignore
		}
		self.license = DataFactory(d_type=DTypes.LICENSE, **self.license) # type: ignore
		self.tags = DataFactory.load_many(data_list=self.tags, d_type=DTypes.TAG)
		return super().__post_init__(*args, **kwargs)
