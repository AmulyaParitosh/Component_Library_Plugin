from abc import ABCMeta

from PySide6.QtCore import QObject

pyqtWrapperType = type(QObject)

class AbstractQObject(pyqtWrapperType, ABCMeta):...
