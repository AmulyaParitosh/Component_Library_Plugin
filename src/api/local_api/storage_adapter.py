import json
from functools import cache
from pathlib import Path


# ~ from ...config import Config

class LocalData:
	def __init__(self, components, tags, filetypes) -> None:
		self.components = components
		self.tags = tags
		self.filetypes = filetypes



class LocalDataManager:

	storage_path: Path = Path("test/local_storage")
	# ~ storage_path: Path = Config.LOCAL_COMPONENT_PATH

	with (storage_path/"data.json").open('r') as file:
		comp_data = json.load(file)

	x = storage_path/"data.json"
	print(str(x))

	@classmethod
	def get_compoent(cls, component_path: str):...
