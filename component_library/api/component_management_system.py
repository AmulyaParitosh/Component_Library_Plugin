from typing import Any, Iterable

from PySide6.QtCore import QRunnable, QUrl, QUrlQuery, Slot


class _Worker(QRunnable):

	def __init__(self, fn, *args, **kwargs) -> None:
		super().__init__()
		self.fn = fn
		self.args = args
		self.kwargs = kwargs

	@Slot()
	def run(self) -> None:
		self.fn(*self.args, **self.kwargs)


class Api(QUrl):

	def __init__(self, url: str):
		super().__init__(url)

		self.query_parameter = QUrlQuery()
		# self.setQuery(self.query_parameter.query())

	def addQueryParameter(self, parameter: str, value: Any):
		if isinstance(value, (str, bool, int, float)):
			self.addSingleQueryParam(parameter, value)
		elif isinstance(value, Iterable):
			self.addIterableQueryParam(parameter, value)
		else:
			raise TypeError(f"{type(value)} not supported for query parameter.")

	def addSingleQueryParam(self, panameter: str, value: str|bool|int|float):
		self.query_parameter.addQueryItem(panameter, str(value))
		self.setQuery(self.query_parameter.query())

	def addIterableQueryParam(self, panameter: str, value: Iterable):...


component_management_api = Api("http://127.0.0.1:5000/api")
