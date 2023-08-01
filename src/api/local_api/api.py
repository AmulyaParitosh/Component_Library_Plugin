import json
from functools import cache

from ...config import Config
from ...data import Component, DataFactory, FileTypes
from ..base_api import ApiInterface
from .storage_adapter import LocalData, LocalDataComp


class LocalApi(ApiInterface):
    # A class representing a local API interface for CRUD operations on components.

    def create(self, component: Component, filetype: FileTypes):
        # Create a new component in the local storage.

        comp_name = component.metadata.name  # Extract the name of the component.

        with LocalData(Config.LOCAL_COMPONENT_PATH) as data:
            # Open the LocalData storage adapter with the LOCAL_COMPONENT_PATH as the root path.

            data["components"].add(comp_name)  # Add the component name to the list of components.

            data["filetypes"].setdefault(filetype.value, LocalDataComp()).add(comp_name)
            # Add the component name to the corresponding filetype set in the data.

            for tag in component.tags:
                data["tags"].setdefault(tag.label, LocalDataComp()).add(comp_name)
                # Add the component name to the corresponding tag set in the data.

        with self.metadata_path(comp_name).open('w') as file:
            metadata = DataFactory.serialize(component.metadata)
            metadata.pop("thumbnail")  # Remove the 'thumbnail' field from the metadata.
            json.dump(metadata, file, indent=4)
            # Write the serialized metadata to the metadata file in JSON format with indentation.


    def read(self):...


    def update(self):...


    def delete(self):...


    @classmethod
    def component_path(cls, component_name: str):
        # Get the path of a component based on its name.
        return Config.LOCAL_COMPONENT_PATH/component_name


    @classmethod
    def metadata_path(cls, component_name: str):
        # Get the path of the metadata file for a component based on its name.
        return cls.component_path(component_name)/"metadata.json"


@cache
def getApi() -> LocalApi:
    # Function to get a singleton instance of LocalApi.

    return LocalApi()
    # Return an instance of LocalApi class (the same instance if it already exists).

    # TODO apply singleton with
    # _instance = None
    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance
