import json
from functools import cache

from ...config import Config
from ...data import Component, DataFactory, FileTypes
from ..base_api import ApiInterface
from .storage_adapter import LocalData, LocalDataComp


class LocalApi(ApiInterface):

	def create(self, component: Component, filetype: FileTypes):

		comp_name = component.metadata.name

		with LocalData(Config.LOCAL_COMPONENT_PATH) as data:

			data["components"].add(comp_name)

			old_filetype = data["filetypes"].get(filetype.value, LocalDataComp())
			old_filetype.add(comp_name)
			data["filetypes"].update({filetype.value: old_filetype})

			for tag in component.tags:
				old_tags = data["tags"].get(tag.label, LocalDataComp())
				old_tags.add(comp_name)
				data["tags"].update({tag.label : old_tags})

		with self.metadata_path(comp_name).open('+w') as file:
			metadata = DataFactory.serialize(component.metadata)
			metadata.pop("thumbnail")
			json.dump(metadata, file, indent=4)


	def read(self):...

	def update(self):...

	def delete(self):...

	@classmethod
	def component_path(cls, component_name: str):
		return Config.LOCAL_COMPONENT_PATH/component_name

	@classmethod
	def metadata_path(cls, component_name: str):
		return cls.component_path(component_name)/"metadata.json"


@cache
def getApi() -> LocalApi:
	return LocalApi()
	# TODO apply singleton with
	# _instance = None
    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance
