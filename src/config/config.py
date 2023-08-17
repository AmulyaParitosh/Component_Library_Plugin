
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

# Load environment variables from a .env file in the current working directory (if present)
load_dotenv()

# Define a configuration class to hold various settings and constants
class Config:
    # Define the API_URL constant with the value "http://127.0.0.1:5000"
    API_URL = "http://127.0.0.1:5000"

    # Retrieve the GITHUB_ACCESS_TOKEN from the environment variables
    # If the "ACCESS_TOKEN" environment variable is not set, it will default to an empty string
    GITHUB_ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")

    # Define the LOCAL_COMPONENT_PATH constant as a Path object representing the "test/local_storage" path
    LOCAL_COMPONENT_PATH = Path("local_storage")
