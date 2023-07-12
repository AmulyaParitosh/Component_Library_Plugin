from abc import abstractmethod
from typing import Any

from PySide6.QtWidgets import QWidget

from ...utils import AbstractQObject


class BaseView(QWidget, metaclass=AbstractQObject):

	@abstractmethod
	def setupUi(self):
		raise NotImplementedError

	@abstractmethod
	def setupSignals(self):
		raise NotImplementedError

	@abstractmethod
	def setupManager(self):
		raise NotImplementedError
	# TODO after making base manager, add it to the parameter here

	@abstractmethod
	def updateContent(self, content: Any):
		raise NotImplementedError
