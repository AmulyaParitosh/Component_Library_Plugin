from PySide6.QtCore import QUrl, QUrlQuery
from PySide6.QtNetwork import QNetworkRequest

from ...controller.query import RepoComponentQuery


class ComponentRequest(QNetworkRequest):

	endpoint: str = "component"

	def __init__(self, state: RepoComponentQuery|None=None, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.setUrl(self.endpoint)
		self.query = QUrlQuery()
		if isinstance(state, RepoComponentQuery):
			self.from_states(state)

	def from_states(self, state: RepoComponentQuery) -> None:
		query_list: list[str] = [
			state.page,
			state.page_size,
			state.search_key,
			state.sort_by,
			state.sort_ord,
			state.file_types,
			state.tags,
			state.columns,
		]
		self.query.setQuery("&".join(item for item in query_list if item))

		url: QUrl = self.url()
		url.setQuery(self.query)
		self.setUrl(url)
