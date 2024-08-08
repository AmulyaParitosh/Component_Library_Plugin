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

from PySide2.QtWidgets import QApplication
from src.main import ComponentLibraryAddon

if __name__ == "__main__":

    app = QApplication(sys.argv)

    addon = ComponentLibraryAddon.independent_local_dev_app()

    sys.exit(app.exec_())
