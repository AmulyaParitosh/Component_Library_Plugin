
# SPDX-License-Identifier: MIT
# --------------------------------------------------------------
#|																|
#|             Copyright 2023 - 2023, Amulya Paritosh			|
#|																|
#|  This file is part of Component Library Plugin for FreeCAD.	|
#|																|
#|               This file was created as a part of				|
#|              Google Summer Of Code Program - 2023			|
#|																|
# --------------------------------------------------------------

import json
from dataclasses import InitVar, dataclass, field

from .data_types import DTypes, FileTypes
from .factory import DataFactory


@dataclass(kw_only=True)
class _Data(DataFactory, dtype=None):
    # A base dataclass representing generic data objects.

    dtype: InitVar[DTypes|None] = None
    id: str = None
    created_at: str = None
    updated_at: str = None

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

    metadata_id: str = None
    updated_at: str = None
    size: int = 0
    url: str = None
    type: FileTypes = field(default=None)
    exists: bool = False

    def __post_init__(self, *args, **kwargs):
        # the data from api has type as dict but in local it is string
        try:
            self.type = FileTypes(self.type.get("name"))
        except AttributeError:
            self.type = FileTypes(self.type)


@dataclass(kw_only=True)
class License(_Data, dtype=DTypes.LICENSE):
    # A dataclass representing License data objects.

    identifier: str = None
    fullname: str = None
    license_page: str = None
    fsf_free: bool = False
    osi_approved: bool = False


@dataclass(kw_only=True)
class Metadata(_Data, dtype=DTypes.METADATA):
    # A dataclass representing Metadata data objects.

    license_id: str = None
    name: str = None
    author: str = None
    maintainer: str = None
    description: str = None
    rating: float = 0
    thumbnail: str = None
    version: str = None


@dataclass(kw_only=True)
class Tag(_Data, dtype=DTypes.TAG):
    # A dataclass representing Tag data objects.
    label: str = ""


@dataclass(kw_only=True)
class Component(DataFactory, dtype=DTypes.COMPONENT):
    # A dataclass representing Component data objects.

    dtype: InitVar[DTypes|None] = None
    id: str = ''
    metadata: Metadata = None
    files: dict[FileTypes, File] = field(default_factory=dict)
    license: License = None
    tags: list[Tag] = field(default_factory=list)

    def __post_init__(self, *args, **kwargs):
        # Post-initialization method for Component objects.

        self.metadata = DataFactory.create(dtype=DTypes.METADATA, **self.metadata)

        # files object from api is a list and in local it is a dict
        if isinstance(self.files, list):
            self.files = {file.type: file for file in
                        DataFactory.load_many(data_list=self.files, dtype=DTypes.FILE)}
        elif isinstance(self.files, dict):
            self.files = {file.type: file for file in
                        DataFactory.load_many(data_list=list(self.files.values()), dtype=DTypes.FILE)}
        self.license = DataFactory.create(dtype=DTypes.LICENSE, **self.license)
        self.tags = DataFactory.load_many(data_list=self.tags, dtype=DTypes.TAG)

    def serialize(self, base_info: bool = False):
        original_files = self.files
        self.files = {key.value: value for key, value in self.files.items()}
        data = super().serialize()
        self.files = original_files
        return data


class DataJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Component, Metadata, File, License, Tag)):
            return obj.serialize()
        if isinstance(obj, FileTypes):
            return obj.value
        return json.JSONEncoder.default(self, obj)
