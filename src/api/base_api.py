from abc import abstractmethod

from ..utils import ABCQObject


class ApiInterface(ABCQObject):

	@abstractmethod
	def create(self):...

	@abstractmethod
	def read(self):...

	@abstractmethod
	def update(self):...

	@abstractmethod
	def delete(self):...
