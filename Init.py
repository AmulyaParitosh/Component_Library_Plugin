# Copyright (c) 2023 Amulya Paritosh
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pathlib import Path

import FreeCAD

from src.config import config
from src.utils import setup_config

# config = Settings()
config.LOCAL_COMPONENT_PATH = (
    Path(FreeCAD.ConfigGet("UserAppData")) / "ComponentLibrary"
)
config.LOCAL_COMPONENT_PATH.mkdir(exist_ok=True)
# setup_config(config)

# FreeCAD.__unit_test__ += ["TestComponentLibraryAddon"]
