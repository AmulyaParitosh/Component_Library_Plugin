import json
from pathlib import Path
from typing import TypedDict

LocalDataComp =  set[str]


class LocalDataDict(TypedDict):
	components: LocalDataComp
	tags: dict[str, LocalDataComp]
	filetypes: dict[str, LocalDataComp]


class SetJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


class SetJSONDecoder(json.JSONDecoder):
	def __init__(self):
		json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

	def dict_to_object(self, d: dict):
		f = {}
		for key, value in d.items():
			if isinstance(value, list):
				value = set(value)
			f[key] = value
		return f


class LocalData:
	# TODO make it sindleton

	def __init__(self, storage_path: Path) -> None:
		self.DATA_PATH = storage_path / "data.json"
		if not self.DATA_PATH.exists():
			self.__reset_data()

	def __enter__(self):
		with (self.DATA_PATH).open('r') as file:
			self.data: LocalDataDict = json.load(file, cls=SetJSONDecoder)
			return self.data

	def __exit__(self, exc_type, exc_value, exc_tb):
		with (self.DATA_PATH).open('w') as file:
			json.dump(self.data, file, cls=SetJsonEncoder, indent=4)

	def __reset_data(self):
		with self.DATA_PATH.open("w+") as file:
			json.dump(
				{
					"components" : [],
					"tags" : {},
					"filetypes" : {},
				},
				file, indent=4,
			)
