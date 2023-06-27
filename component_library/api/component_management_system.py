from os import path

from PySide6.QtNetwork import (QNetworkAccessManager, QNetworkReply,
                               QNetworkRequest)


class ApiManager(QNetworkAccessManager):

	def __init__(self, base_url: str) -> None:
		super().__init__()
		self.base_url: str = path.join(base_url, "api")

	def make_absolutepath(self, request: QNetworkRequest):
		absolute_path = path.join(self.base_url, request.url().toString())
		request.setUrl(absolute_path)

	def get(self, request: QNetworkRequest) -> QNetworkReply:
		self.make_absolutepath(request)
		return super().get(request)

	def post(self, request: QNetworkRequest, data: bytes) -> QNetworkReply:
		self.make_absolutepath(request)
		return super().post(request, data)

	def put(self, request: QNetworkRequest, data: bytes) -> QNetworkReply:
		self.make_absolutepath(request)
		return super().put(request, data)


component_management_api = ApiManager("http://127.0.0.1:5000")

# class _Worker(QRunnable):

# 	def __init__(self, fn, *args, **kwargs) -> None:
# 		super().__init__()
# 		self.fn = fn
# 		self.args = args
# 		self.kwargs = kwargs

# 	@Slot()
# 	def run(self) -> None:
# 		self.fn(*self.args, **self.kwargs)


# class _Api(QUrl):

# 	def __init__(self, url: str):
# 		super().__init__(url)

# 		self.query_parameter = QUrlQuery()
# 		# self.setQuery(self.query_parameter.query())

# 	def addQueryParameter(self, parameter: str, value: Any):
# 		if isinstance(value, (str, bool, int, float)):
# 			self.addSingleQueryParam(parameter, value)
# 		elif isinstance(value, Iterable):
# 			self.addIterableQueryParam(parameter, value)
# 		else:
# 			raise TypeError(f"{type(value)} not supported for query parameter.")

# 	def addSingleQueryParam(self, panameter: str, value: str|bool|int|float):
# 		self.query_parameter.addQueryItem(panameter, str(value))
# 		self.setQuery(self.query_parameter.query())

# 	def addIterableQueryParam(self, panameter: str, value: Iterable):...
