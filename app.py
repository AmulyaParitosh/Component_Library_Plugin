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


def module_setup():
    try:
        import PySide

        sys.modules["PySide6"] = PySide
        print("changed name, using PySide as PySide6")
    except ImportError:
        print("error in importing PySide, using PySide6")


if __name__ == "__main__":
    module_setup()

    from PySide6.QtWidgets import QApplication

    from src import Window

    app = QApplication(sys.argv)

    plugin = Window()

    sys.exit(app.exec())
