from abc import abstractmethod
from typing import Any

from PySide6.QtWidgets import QWidget

from ...controller.manager_interface import ManagerInterface
from ...utils import AbstractQObject


class BaseView(QWidget, metaclass=AbstractQObject):

	@abstractmethod
	def setupUi(self):...

	@abstractmethod
	def setupSignals(self):...

	@abstractmethod
	def setupManager(self, manager: ManagerInterface):
		self.manager: ManagerInterface = manager

	@abstractmethod
	def updateContent(self, content: Any):...
