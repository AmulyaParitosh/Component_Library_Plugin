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
