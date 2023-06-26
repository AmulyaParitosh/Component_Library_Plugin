from PySide6.QtWidgets import QGridLayout, QWidget

from ..components import ComponentItem


class ItemWigdet(QWidget):

	def __init__(self, ) -> None:

		super().__init__()

		self.grid = QGridLayout()
		self.setLayout(self.grid)

		self.__MAX_COL = 3
		self.__cur_row = 0
		self.__cur_col = 0

		# self.show()
		# self.populate()


	def populate(self, metadata:list[dict]):
		for data in metadata:
			component = ComponentItem(self, data)
			self.addItem(component)

	def __next_row(self):
		self.__cur_row = self.__cur_col // self.__MAX_COL
		return self.__cur_row

	def __next_col(self):
		self.__cur_col += 1
		return (self.__cur_col-1) % self.__MAX_COL

	def addItem(self, item: ComponentItem):
		self.grid.addWidget(item, self.__next_row(), self.__next_col())
