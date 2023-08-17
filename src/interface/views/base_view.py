
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

from abc import abstractmethod
from typing import Any

from ...manager import ManagerInterface
from ...utils import ABCQWidget


# Abstract base class for view classes displaying content in a user interface
class BaseView(ABCQWidget):

    # Abstract method to set up the user interface (UI)
    @abstractmethod
    def setupUi(self):...
        # This method must be implemented in the derived classes.
        # It should define and initialize the UI elements (widgets) of the view.

    # Abstract method to set up signal-slot connections
    @abstractmethod
    def setupSignals(self):...
        # This method must be implemented in the derived classes.
        # It should connect signals emitted by the UI elements to their respective slot methods.

    # Abstract method to set up the manager for the view
    @abstractmethod
    def setupManager(self, manager: ManagerInterface):
        # This method must be implemented in the derived classes.
        # It should store the given ManagerInterface instance in the 'manager' attribute of the view.
        self.manager: ManagerInterface = manager
        # The ManagerInterface is used to interact with data and signals for the view.
        # The 'abstractmethod' decorator makes it mandatory to implement this method in the derived classes.

    # Abstract method to update the content displayed in the view
    @abstractmethod
    def updateContent(self, content: Any):...
        # This method must be implemented in the derived classes.
        # It should update the view's UI elements with the given 'content' data.
        # The 'Any' type here means the 'content' parameter can be of any type.
        # The 'abstractmethod' decorator makes it mandatory to implement this method in the derived classes.
