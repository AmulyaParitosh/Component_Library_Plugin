# Copyright (c) 2023 Amulya Paritosh
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


import FreeCAD
import FreeCADGui

from app import module_setup

module_setup()


class ComponentLibraryWorkbench(Workbench):

    def __init__(self):
        self.__class__.MenuText = "ComponentLibrary"
        self.__class__.ToolTip = "ComponentLibrary workbench"

    def Initialize(self) -> None:
        from src import Window

        plugin = Window()

    def Activated(self):
        ...

    def GetClassName(self):
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(ComponentLibraryWorkbench())
