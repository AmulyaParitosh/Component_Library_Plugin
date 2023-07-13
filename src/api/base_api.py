from abc import abstractmethod

from PySide6.QtCore import QObject

from ..utils import AbstractQObject


class ApiInterface(AbstractQObject):

	@abstractmethod
	def create(self):...

	@abstractmethod
	def read(self):...

	@abstractmethod
	def update(self):...

	@abstractmethod
	def delete(self):...
