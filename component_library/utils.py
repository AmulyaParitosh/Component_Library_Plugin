from abc import ABCMeta
from typing import Protocol

from PySide6.QtCore import QObject

QObjectWrapperType = type(QObject)
ProtocolWrapperType = type(Protocol)

class AbstractQObject(QObjectWrapperType, ABCMeta):...

class Interface(QObjectWrapperType, ProtocolWrapperType):...
