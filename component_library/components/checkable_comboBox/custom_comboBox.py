from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import QComboBox


# creating checkable combo box class
class CheckableComboBox(QComboBox):
	def __init__(self, parent):
		super().__init__()
		self.setParent(parent)
		self.view().pressed.connect(self.handle_item_pressed)
		self.setModel(QStandardItemModel(self))

	# when any item get pressed
	def handle_item_pressed(self, index):

		# getting which item is pressed
		item = self.model().itemFromIndex(index)

		# make it check if unchecked and vice-versa
		if item.checkState() == Qt.CheckState.Checked:
			item.setCheckState(Qt.CheckState.Unchecked)
		else:
			item.setCheckState(Qt.CheckState.Checked)

		# calling method
		self.check_items()

	# method called by check_items
	def item_checked(self, index):

		# getting item at index
		item = self.model().item(index, 0)

		# return true if checked else false
		return item.checkState() == Qt.CheckState.Checked

	# calling method
	def check_items(self):
		# blank list
		checkedItems = []

		# traversing the items
		for i in range(self.count()):

			# if item is checked add it to the list
			if self.item_checked(i):
				checkedItems.append(i)

		# call this method
		self.update_labels(checkedItems)

	# method to update the label
	def update_labels(self, item_list):

		n = ''
		count = 0

		# traversing the list
		for i in item_list:

			# if count value is 0 don't add comma
			if count == 0:
				n += ' % s' % i
			# else value is greater than 0
			# add comma
			else:
				n += ', % s' % i

			# increment count
			count += 1


		# loop
		for i in range(self.count()):

			# getting label
			text_label = self.model().item(i, 0).text()

			# default state
			if text_label.find('-') >= 0:
				text_label = text_label.split('-')[0]

			# shows the selected items
			# item_new_text_label = text_label + ' - selected index: ' + n
			item_new_text_label = text_label

		# setting text to combo box
			self.setItemText(i, item_new_text_label)

	# flush
	# sys.stdout.flush()


# class __Window(QMainWindow):
# 	def __init__(self):
# 		super(QMainWindow, self).__init__()

# 		# creating a widget object
# 		myQWidget = QWidget()

# 		# vertical box layout
# 		myBoxLayout = QVBoxLayout()
# 		myQWidget.setLayout(myBoxLayout)

# 		# central widget
# 		self.setCentralWidget(myQWidget)

# 		# creating checkable combo box
# 		self.ComboBox = CheckableComboBox()

# 		# traversing items
# 		for i in range(3):
# 			# adding item
# 			self.ComboBox.addItem("Combobox Item " + str(i))
# 			item = self.ComboBox.model().item(i, 0)

# 			# setting item unchecked
# 			item.setCheckState(Qt.Unchecked)

# 		# adding combo box to the layout
# 		myBoxLayout.addWidget(self.ComboBox)
