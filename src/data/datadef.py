from dataclasses import InitVar, dataclass, field

from .data_types import DTypes, FileTypes
from .factory import DataFactory


@dataclass(kw_only=True)
class _Data(DataFactory, dtype=None):
	dtype : InitVar[DTypes|None] = None
	id: str
	created_at: str
	updated_at: str

	def __post_init__(self, *args, **kwargs):...


class GenericData(DataFactory, dtype=DTypes.GENERIC):
	def __init__(self, **kwargs):
		kwargs.pop("dtype", None)
		for k, v in kwargs.items():
			setattr(self, k, v)


@dataclass(kw_only=True)
class File(_Data, dtype=DTypes.FILE):
	metadata_id: str
	updated_at: str
	size: int
	url: str
	type : FileTypes = field(default=None) # type: ignore

	def __post_init__(self, *args, **kwargs):
		self.type = FileTypes(self.type.get("name")) # type: ignore


@dataclass(kw_only=True)
class License(_Data, dtype=DTypes.LICENSE):
    identifier: str
    fullname: str
    license_page: str
    fsf_free: bool
    osi_approved: bool


@dataclass(kw_only=True)
class Metadata(_Data, dtype=DTypes.METADATA):
	license_id: str
	name: str
	author: str
	maintainer: str
	description: str
	rating: float
	thumbnail: str
	version: str


@dataclass(kw_only=True)
class Tag(_Data, dtype=DTypes.TAG):
	label: str = ""


@dataclass(kw_only=True)
class Component(DataFactory, dtype=DTypes.COMPONENT):
	dtype : InitVar[DTypes|None] = None
	id: str
	metadata: Metadata
	files: dict[FileTypes, File]
	license: License
	tags: list[Tag]

	def __post_init__(self, *args, **kwargs):
		self.metadata = DataFactory(dtype=DTypes.METADATA, **self.metadata) # type: ignore
		self.files = {file.type : file for file in # type: ignore
			DataFactory.load_many(data_list=self.files, dtype=DTypes.FILE) # type: ignore
		}
		self.license = DataFactory(dtype=DTypes.LICENSE, **self.license) # type: ignore
		self.tags = DataFactory.load_many(data_list=self.tags, dtype=DTypes.TAG) # type: ignore
