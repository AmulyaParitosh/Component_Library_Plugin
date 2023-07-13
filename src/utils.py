from abc import ABC, ABCMeta

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject

QObjectMeta = type(QObject)
QWidgetMeta = type(QWidget)

class ABCQObjectMeta(QObjectMeta, ABCMeta):...

class ABCQObject(QObject, ABC, metaclass=ABCQObjectMeta):...

class ABCQWidgetMeta(QObjectMeta, ABCMeta):...

class ABCQWidget(QWidget, ABC, metaclass=ABCQWidgetMeta):...
