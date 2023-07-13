from abc import ABC, ABCMeta

from PySide6.QtCore import QObject

QObjectMeta = type(QObject)

class ABCQObjectMeta(QObjectMeta, ABCMeta):...

class AbstractQObject(QObject, ABC, metaclass=ABCQObjectMeta):...
