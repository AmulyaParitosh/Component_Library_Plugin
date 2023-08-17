
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

from .overlay import Overlay


class LoadingOverlay(Overlay):
    # Custom subclass of the Overlay class representing a loading overlay.

    overlay_text = "loading..."  # Text to be displayed on the loading overlay.

    @property
    def loading(self) -> bool:
        # Property getter method to check if the loading overlay is currently visible.
        return self.isVisible()

    @loading.setter
    def loading(self, load: bool):
        # Property setter method to show or hide the loading overlay based on the 'load' parameter.

        if load:
            self.show()  # Show the loading overlay.
        else:
            self.hide()  # Hide the loading overlay.
