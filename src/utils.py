from abc import ABC, ABCMeta

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget

QObjectMeta = type(QObject)
QWidgetMeta = type(QWidget)

class _ABCQObjectMeta(QObjectMeta, ABCMeta):...
class _ABCQWidgetMeta(QObjectMeta, ABCMeta):...


class ABCQObject(QObject, ABC, metaclass=_ABCQObjectMeta):...
class ABCQWidget(QWidget, ABC, metaclass=_ABCQWidgetMeta):...
