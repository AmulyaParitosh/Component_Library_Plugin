from enum import Enum


class DTypes(Enum):
	# An Enum representing different data types.

	COMPONENT = "component"
	FILE = "file"
	LICENSE = "license"
	METADATA = "metadata"
	TAG = "tag"
	GENERIC = "generic"


class FileTypes(Enum):
	# An Enum representing different file types.

	STL = "stl"
	FCSTD = "fcstd"
	FCSTD1 = "fcstd1"
	STEP = "step"
	STP = "stp"
