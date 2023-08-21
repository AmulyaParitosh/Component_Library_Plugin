
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

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv() # Load environment variables from a .env file in the current working directory (if present)

class Config:
    """
    Class to store all the configurations.
    """
    API_URL = "http://127.0.0.1:5000"
    GITHUB_ACCESS_TOKEN: str = os.getenv("ACCESS_TOKEN", "")
    LOCAL_COMPONENT_PATH = Path("local_storage")
