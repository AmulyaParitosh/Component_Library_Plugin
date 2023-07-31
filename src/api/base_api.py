from abc import abstractmethod

from ..utils import ABCQObject


class ApiInterface(ABCQObject):

	@abstractmethod
	def create(self, *args, **kwargs):...

	@abstractmethod
	def read(self, *args, **kwargs):...

	@abstractmethod
	def update(self, *args, **kwargs):...

	@abstractmethod
	def delete(self, *args, **kwargs):...
