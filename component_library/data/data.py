from dataclasses import InitVar, asdict, dataclass, is_dataclass, field
from enum import Enum
from typing import Any, Callable


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


class GenericData(DataFactory, d_type=DTypes.GENERIC):
	def __init__(self, **kwargs):
		kwargs.pop("d_type", None)
		for k, v in kwargs.items():
			setattr(self, k, v)


@dataclass
class _Data(DataFactory, d_type=None):
	d_type : InitVar[DTypes|None] = None
	id: str = field(default="")
	created_at: str = field(default="")
	updated_at: str = field(default="")

	def __post_init__(self, *args, **kwargs):...


class FileTypes(Enum):
	STL = "stl"
	FCSTD = "fcstd"
	FCSTD1 = "fcstd1"
	STEP = "step"
	STP = "stp"


@dataclass
class File(_Data, d_type=DTypes.FILE):
	metadata_id: str = field(default="")
	updated_at: str = field(default="")
	size: int = field(default=0)
	url: str = field(default="")
	type : FileTypes|None = field(default=None)

	def __post_init__(self, *args, **kwargs):
		self.type = FileTypes(self.type.get("name")) # type: ignore


@dataclass
class License(_Data, d_type=DTypes.LICENSE):
    identifier: str = field(default="")
    fullname: str = field(default="")
    license_page: str = field(default="")
    fsf_free: bool = field(default=False)
    osi_approved: bool = field(default=True)


@dataclass
class Metadata(_Data, d_type=DTypes.METADATA):
	license_id: str = field(default="")
	name: str = field(default="")
	author: str = field(default="")
	maintainer: str = field(default="")
	description: str = field(default="")
	rating: float = field(default=0)
	thumbnail: str = field(default="")
	version: str = field(default="")


@dataclass
class Tag(_Data, d_type=DTypes.TAG):
	label: str = ""


@dataclass
class Component(Metadata, d_type=DTypes.COMPONENT):
	files: list[File] = field(default_factory=list)
	license : list[License] = field(default_factory=list)
	tags: list[Tag] = field(default_factory=list)
