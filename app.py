#!/usr/bin/python3

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


import sys

from src.config import Settings
from src.utils import module_setup, setup_config

if __name__ == "__main__":
    module_setup()
    config = Settings()
    setup_config(config)

    from PySide2.QtWidgets import QApplication

    from src.main import Window

    app = QApplication(sys.argv)

    plugin = Window()

    sys.exit(app.exec_())
