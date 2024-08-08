import os
from pathlib import Path

from .utils import module_setup, setup_config
from .config import Config


class ComponentLibraryAddon:

    @staticmethod
    def independent_local_dev_app():
        module_setup()
        config = Config()
        config.API_URL = "http://127.0.0.1:5000"
        config.LOCAL_COMPONENT_PATH = Path("local_storage")
        config.GITHUB_OAUTH_CLIENT_ID = os.environ.get("GITHUB_OAUTH_CLIENT_ID", "")
        config.GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", "")
        config.JWT_TOKEN = ""

        setup_config(config)

        from .addon_window import AddonWindow

        return AddonWindow()

    @staticmethod
    def freecad_local_dev_app():
        import FreeCAD

        config = Config()
        config.API_URL = "http://127.0.0.1:5000"
        config.LOCAL_COMPONENT_PATH = (
            Path(FreeCAD.ConfigGet("UserAppData")) / "ComponentLibrary"
        )
        config.LOCAL_COMPONENT_PATH.mkdir(exist_ok=True)
        config.GITHUB_OAUTH_CLIENT_ID = os.environ.get("GITHUB_OAUTH_CLIENT_ID", "")
        config.GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", "")
        config.JWT_TOKEN = ""

        setup_config(config)

        from .addon_window import AddonWindow

        return AddonWindow()
