# SPDX-License-Identifier: MIT
# --------------------------------------------------------------
# |																|
# |             Copyright 2023 - 2023, Amulya Paritosh			|
# |																|
# |  This file is part of Component Library Plugin for FreeCAD.	|
# |																|
# |               This file was created as a part of				|
# |              Google Summer Of Code Program - 2023			|
# |																|
# --------------------------------------------------------------

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file in the current working directory (if present)


class Config:
    """
    Class to store all the configurations.
    """

    API_URL: str
    LOCAL_COMPONENT_PATH: Path

    GITHUB_OAUTH_CLIENT_ID: str
    GITHUB_ACCESS_TOKEN: str
    JWT_TOKEN: str


config = None
