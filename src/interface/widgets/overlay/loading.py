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

from .overlay import Overlay


class LoadingOverlay(Overlay):
    """
    Custom subclass of the Overlay class representing a loading overlay.
    """

    overlay_text = "loading..."

    @property
    def loading(self) -> bool:
        """
        Get the visibility status of the loading overlay.

        Returns
        -------
        bool
            True if the loading overlay is currently visible, False otherwise.
        """
        return self.isVisible()

    @loading.setter
    def loading(self, load: bool):
        """
        Set the visibility of the loading overlay.

        Parameters
        ----------
        load : bool
            True to show the loading overlay, False to hide it.
        """
        if load:
            self.show()
        else:
            self.hide()
