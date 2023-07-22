from enum import Enum


class DTypes(Enum):
	COMPONENT = "component"
	FILE = "file"
	LICENSE = "license"
	METADATA = "metadata"
	TAG = "tag"
	GENERIC = "generic"


class FileTypes(Enum):
	STL = "stl"
	FCSTD = "fcstd"
	FCSTD1 = "fcstd1"
	STEP = "step"
	STP = "stp"
