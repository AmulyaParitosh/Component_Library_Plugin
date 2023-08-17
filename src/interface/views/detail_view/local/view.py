
# SPDX-License-Identifier: MIT
# --------------------------------------------------------------
#|																|
#|             Copyright 2023 - 2023, Amulya Paritosh			|
#|																|
#|  This file is part of Component Library Plugin for FreeCAD.	|
#|																|
#|               This file was created as a part of				|
#|              Google Summer Of Code Program - 2023			|
#|																|
# --------------------------------------------------------------

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QWidget

from .....manager import LocalStorageManager, ManagerInterface
from ..base_detail_view import BaseDetailedView


class LocalDetailedView(BaseDetailedView):

	manager: LocalStorageManager

	# Constructor for the OnlineDetailedView class
	def __init__(self, parent: QWidget) -> None:
		super().__init__(parent)

		# Call the setupUi and setupSignals methods
		self.setupUi()
		self.setupSignals()

	# Initialize the user interface elements
	def setupUi(self):
		super().setupUi()

		self.removePushButton = QPushButton(self)
		self.removePushButton.setText("Remove")
		self.addControlWidget(self.removePushButton)

	def setupSignals(self):
		self.removePushButton.clicked.connect(self.removed)


	def setupManager(self, manager: ManagerInterface):
		super().setupManager(manager)


	@Slot()
	def removed(self):
		self.manager.remove_file(self.component, self.current_file().type)
		self.ui.filetypeComboBox.removeItem(self.ui.filetypeComboBox.currentIndex())
		if self.ui.filetypeComboBox.count() == 0:
			self.backPushButton_click()
		self.parent().parent().localGridView.components_response_handler()
