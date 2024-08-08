import logging

from FreeCAD import Console


class Logger(logging.Logger):

    def __init__(self, name, level=logging.DEBUG):
        super().__init__(name, level)

        self.setLevel(level)
        self.formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        self.console_handler = logging.StreamHandler()
        self.console_handler.setFormatter(self.formatter)
        self.addHandler(self.console_handler)
        self.file_handler = logging.FileHandler("log.log")
        self.file_handler.setFormatter(self.formatter)
        self.addHandler(self.file_handler)
        self.info("Logger initialized")

    def debug(self, msg: str) -> None:
        if self.isEnabledFor(logging.DEBUG):
            Console.PrintLog(msg)
        return super().debug(msg)

    def info(self, msg: str) -> None:
        if self.isEnabledFor(logging.INFO):
            Console.PrintMessage(msg)
        return super().info(msg)

    def warning(self, msg: str) -> None:
        if self.isEnabledFor(logging.WARNING):
            Console.PrintWarning(msg)
        return super().warning(msg)

    def exception(self, msg: str) -> None:
        if self.isEnabledFor(logging.ERROR):
            Console.PrintError(msg)
        return super().exception(msg)

    def critical(self, msg: str) -> None:
        if self.isEnabledFor(logging.CRITICAL):
            Console.PrintCritical(msg)
        return super().critical(msg)


logger = Logger("ComponentLibraryAddon", logging.WARNING)