from .overlay import Overlay


class LoadingOverlay(Overlay):
    overlay_text = "loading..."

    @property
    def loading(self) -> bool:
        return self.isVisible()

    @loading.setter
    def loading(self, load: bool):
        if load:
            self.show()
        else:
            self.hide()
