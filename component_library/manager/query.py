from ..network.api import ComponenetQueryParameters
from .page import PageState


class ComponentQueryStateManager:
	query_states = ComponenetQueryParameters()


	def set_page(self, value):
		self.query_states.page = value

	def set_next_page(self, page: PageState):
		self.set_page(page.next_page)

	def set_prev_page(self, page: PageState):
		self.set_page(page.prev_page)

	def set_page_size(self, value):
		self.query_states.page_size = value

	def set_search_key(self, value):
		self.query_states.search_key = value
		self.set_page(1)

	def set_sort_by(self, value):
		self.query_states.sort_by = value
		self.set_page(1)

	def set_sort_ord(self, value):
		self.query_states.sort_ord = value
		self.set_page(1)

	def set_file_types(self, value):
		self.query_states.file_types = value
		self.set_page(1)

	def set_tags(self, value):
		self.query_states.tags = value
		self.set_page(1)

	def set_columns(self, value):
		self.query_states.columns = value
