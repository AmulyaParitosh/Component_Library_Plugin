import contextlib
from copy import deepcopy
import json
from pathlib import Path
from typing import Iterable
import shutil

from ...config import Config
from ...data import Component, FileTypes
from ...utils import singleton
from ..base_api import ApiInterface
from .storage_adapter import LocalData, LocalDataComp, ComponentData, ComponentDataDict


@singleton
class LocalApi(ApiInterface):
    # A class representing a local API interface for CRUD operations on components.

    def create(self, component: Component, filetype: FileTypes):
        # Create a new component in the local storage.
        self._handle_component_data_creation(component, filetype)
        self._handle_local_data_creation(component, filetype)


    def _handle_component_data_creation(self, component: Component, filetype: FileTypes):
        comp_name = component.metadata.name

        with ComponentData(self.metadata_path(comp_name)) as existing_data:

            if existing_data.id == "":
                existing_data.id = component.id
                existing_data.metadata = deepcopy(component.metadata)
                existing_data.license = component.license
                existing_data.tags = component.tags

            existing_data.files[filetype] = deepcopy(component.files[filetype])
            existing_data.files[filetype].url = (self.component_path(comp_name)/f"{comp_name}.{filetype.value}").absolute().as_uri()

            if component.metadata.thumbnail is not None:
                existing_data.metadata.thumbnail = (self.component_path(comp_name)/f"thumbnail{Path(component.metadata.thumbnail).suffix}").absolute().as_uri()

    def _handle_local_data_creation(self, component: Component, filetype: FileTypes):
        comp_name = component.metadata.name  # Extract the name of the component.

        with LocalData(Config.LOCAL_COMPONENT_PATH) as local_data:
            # Open the LocalData storage adapter with the LOCAL_COMPONENT_PATH as the root path.

            local_data["components"].add(comp_name)
            local_data["filetypes"].setdefault(filetype.value, LocalDataComp()).add(comp_name)

            for tag in component.tags:
                local_data["tags"].setdefault(tag.label, LocalDataComp()).add(comp_name)


    def read(self):
        # TODO need list of component json with paginated data
        data = {
            "items" : [],
            "page": 0,
            "per_page": 18,
            "total": 0,
        }
        for path in Config.LOCAL_COMPONENT_PATH.iterdir():
            if not path.is_dir():
                continue
            with open(path/"metadata.json", 'r') as metadata:
                data["items"].append(json.load(metadata))
            data["total"] += 1
            data["page"] = data["total"] // data["per_page"] +1

        return data

    def update(self):...


    def delete(self, component: Component, filetypes: Iterable[FileTypes]|FileTypes):
        comp_name = component.metadata.name
        component_path = self.component_path(comp_name)
        remove_component = False

        with ComponentData(self.metadata_path(comp_name)) as comp_data, LocalData(Config.LOCAL_COMPONENT_PATH) as local_data:
            if isinstance(filetypes, FileTypes): filetypes = [filetypes]
            for filetype in filetypes:
                comp_data.files.pop(filetype)
                local_data["filetypes"][filetype.value].remove(comp_name)
                (component_path/f"{comp_name}.{filetype.value}").unlink()

            if not any(comp_data.files.values()): #checking if there are no files present
                remove_component = True
                local_data["components"].remove(comp_name)
                for comp_list in local_data["tags"].values():
                    with contextlib.suppress(KeyError):
                        comp_list.remove(comp_name)

        if remove_component:
            shutil.rmtree(component_path)


    @classmethod
    def component_path(cls, component_name: str):
        return Config.LOCAL_COMPONENT_PATH/component_name


    @classmethod
    def metadata_path(cls, component_name: str):
        return cls.component_path(component_name)/"metadata.json"


    def get_tags(self):
        with LocalData(Config.LOCAL_COMPONENT_PATH) as local_data:
            return [{"label" : tag} for tag in local_data["tags"].keys()]
