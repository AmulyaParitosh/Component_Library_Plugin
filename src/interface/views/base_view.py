from abc import abstractmethod
from typing import Any

from ...manager import ManagerInterface
from ...utils import ABCQWidget


class BaseView(ABCQWidget):

	@abstractmethod
	def setupUi(self):...

	@abstractmethod
	def setupSignals(self):...

	@abstractmethod
	def setupManager(self, manager: ManagerInterface):
		self.manager: ManagerInterface = manager

	@abstractmethod
	def updateContent(self, content: Any):...
