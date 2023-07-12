from abc import abstractmethod
from typing import Any

from PySide6.QtWidgets import QWidget

from ...controller.manager_interface import ManagerInterface
from ...utils import AbstractQObject


class BaseView(QWidget, metaclass=AbstractQObject):

	@abstractmethod
	def setupUi(self):
		raise NotImplementedError

	@abstractmethod
	def setupSignals(self):
		raise NotImplementedError

	@abstractmethod
	def setupManager(self, manager: ManagerInterface):
		raise NotImplementedError

	@abstractmethod
	def updateContent(self, content: Any):
		raise NotImplementedError
