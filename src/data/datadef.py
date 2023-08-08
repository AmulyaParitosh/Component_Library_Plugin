from dataclasses import InitVar, dataclass, field

from .data_types import DTypes, FileTypes
from .factory import DataFactory


@dataclass(kw_only=True)
class _Data(DataFactory, dtype=None):
    # A base dataclass representing generic data objects.

    dtype: InitVar[DTypes|None] = None
    id: str
    created_at: str
    updated_at: str

    def __post_init__(self, *args, **kwargs):...
        # Placeholder for any post-initialization logic.
        # The implementation for this method is not provided in the code.


class GenericData(DataFactory, dtype=DTypes.GENERIC):
    # A dataclass representing generic data objects with no specific dtype.

    def __init__(self, **kwargs):
        # Initialize a GenericData object.

        kwargs.pop("dtype", None)  # Remove the dtype from the kwargs, if provided.

        for k, v in kwargs.items():
            setattr(self, k, v)
            # Set the attributes of the object based on the provided kwargs.


@dataclass(kw_only=True)
class File(_Data, dtype=DTypes.FILE):
    # A dataclass representing File data objects.

    metadata_id: str
    updated_at: str
    size: int
    url: str
    type: FileTypes = field(default=None)
    EXISTS: bool = False

    def __post_init__(self, *args, **kwargs):
        # Post-initialization method for File objects.

        self.type = FileTypes(self.type.get("name"))  # Convert the type to a FileTypes enum.


@dataclass(kw_only=True)
class License(_Data, dtype=DTypes.LICENSE):
    # A dataclass representing License data objects.

    identifier: str
    fullname: str
    license_page: str
    fsf_free: bool
    osi_approved: bool


@dataclass(kw_only=True)
class Metadata(_Data, dtype=DTypes.METADATA):
    # A dataclass representing Metadata data objects.

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
    # A dataclass representing Tag data objects.

    label: str = ""


@dataclass(kw_only=True)
class Component(DataFactory, dtype=DTypes.COMPONENT):
    # A dataclass representing Component data objects.

    dtype: InitVar[DTypes|None] = None
    id: str
    metadata: Metadata
    files: dict[FileTypes, File]
    license: License
    tags: list[Tag]

    def __post_init__(self, *args, **kwargs):
        # Post-initialization method for Component objects.

        self.metadata = DataFactory(dtype=DTypes.METADATA, **self.metadata)  # Create a Metadata object.
        self.files = {file.type: file for file in
                      DataFactory.load_many(data_list=self.files, dtype=DTypes.FILE)}  # Create File objects.
        self.license = DataFactory(dtype=DTypes.LICENSE, **self.license)  # Create a License object.
        self.tags = DataFactory.load_many(data_list=self.tags, dtype=DTypes.TAG)  # Create Tag objects.

    def serialize(self, base_info: bool = False):
        data = super().serialize(base_info)
        # return {filetype.value : value for filetype, value in data["files"].items()}
        new_dict = {}
        for key, value in data["files"].items():
            value["type"] = value["type"].value
            new_dict[key.value] = value

        data["files"] = new_dict

        return data
