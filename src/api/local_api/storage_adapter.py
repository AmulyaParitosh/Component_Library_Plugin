import json
from pathlib import Path
from typing import TypedDict

# Type alias for a set of strings representing components in local data
LocalDataComp = set[str]

# TypedDict representing the structure of the local data JSON
class LocalDataDict(TypedDict):
    components: LocalDataComp
    tags: dict[str, LocalDataComp]
    filetypes: dict[str, LocalDataComp]

# Custom JSONEncoder for encoding sets as lists in JSON serialization
class SetJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

# Custom JSONDecoder for decoding lists back to sets in JSON deserialization
class SetJSONDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

    def dict_to_object(self, d: dict):
        f = {}
        for key, value in d.items():
            if isinstance(value, list):
                # Convert lists back to sets for keys that should be sets
                value = set(value)
            f[key] = value
        return f

# Class for managing and interacting with local data stored in a JSON file
class LocalData:
    # TODO make it singleton

    def __init__(self, storage_path: Path) -> None:
        # If the folder does not exixt, create it.
        storage_path.mkdir(exist_ok=True)
        self.DATA_PATH = storage_path / "data.json"
        if not self.DATA_PATH.exists():
            # If data file does not exist, create it with default values
            self.__reset_data()

    # Context manager: used to enter the context and read data from the JSON file
    def __enter__(self):
		# Load data from the JSON file using SetJSONDecoder for loading lists as set
        with self.DATA_PATH.open('r') as file:
            self.data: LocalDataDict = json.load(file, cls=SetJSONDecoder)
            return self.data

    # Context manager: used to exit the context and write data to the JSON file
    def __exit__(self, exc_type, exc_value, exc_tb):
		# Write data back to the JSON file using SetJsonEncoder for loading lists as set
        with self.DATA_PATH.open('w') as file:
            json.dump(self.data, file, cls=SetJsonEncoder, indent=4)

    # Private method to reset the data file with default values
    def __reset_data(self):
        with self.DATA_PATH.open("w") as file:
            # Initialize the data file with default empty lists and dictionaries
            json.dump(
                {
                    "components": [],
                    "tags": {},
                    "filetypes": {},
                },
                file, indent=4,
            )