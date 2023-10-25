# Copyright (c) 2023 Amulya Paritosh
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
import FreeCAD
import FreeCADGui

class ComponetLibraryWorkbench(Workbench):
	def __init__(self):
		self.__class__.Icon = FreeCAD.getResourceDir() + ""
		self.__class__.MenuText = "ComponentLibrary"
		self.__class__.ToolTip = "ComponentLibrary workbench"

    def Initialize(self):
		from src import Window
		plugin = Window()

    def Activated(self):...

    def GetClassName(self):...

FreeCADGui.addWorkbench(ComponetLibraryWorkbench())

# FreeCAD.addImportType()
# FreeCAD.addExportType()
