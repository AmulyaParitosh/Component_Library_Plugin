from abc import ABC, ABCMeta
from typing import Type

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget

QObjectMeta = type(QObject)
QWidgetMeta = type(QWidget)

class _ABCQObjectMeta(QObjectMeta, ABCMeta):...
class _ABCQWidgetMeta(QObjectMeta, ABCMeta):...


class ABCQObject(QObject, ABC, metaclass=_ABCQObjectMeta):...
class ABCQWidget(QWidget, ABC, metaclass=_ABCQWidgetMeta):...


def singleton(cls: Type):

	instances = {}

	def get_instance(*args, **kwargs):
		if cls not in instances:
			instances[cls] = cls(*args, **kwargs)
		return instances[cls]

	return get_instance
