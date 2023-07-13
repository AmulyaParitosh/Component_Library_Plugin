from abc import ABCMeta

from PySide6.QtCore import QObject

QObjectWrapperType = type(QObject)

class AbstractQObject(QObjectWrapperType, ABCMeta):...
