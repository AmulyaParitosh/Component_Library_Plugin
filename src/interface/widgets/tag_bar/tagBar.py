
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

from functools import partial
from typing import Sequence

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (QCompleter, QFrame, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QWidget)

from ....data import Tag


class TagBar(QWidget):
    # Custom QWidget class to manage tags using a tag bar.

    tags_edited = Signal(list)

    def __init__(self, parent):
        # Constructor to initialize the TagBar.

        super(TagBar, self).__init__()

        # Set the parent widget.
        self.setParent(parent)

        # Set the window title.
        self.setWindowTitle('Tag Bar')

        # Initialize the tags list.
        self.tags: list[str] = []

        # Create the horizontal layout for the tag bar.
        self.h_layout = QHBoxLayout()
        self.setLayout(self.h_layout)

        # Create the line edit for user input.
        self.line_edit = QLineEdit()
        self.line_edit.setSizePolicy(
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Minimum,
        )

        # Set size policies for the TagBar widget.
        self.setSizePolicy(
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Minimum,
        )
        self.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setContentsMargins(0, 0, 0, 0)

        # Refresh and setup the UI.
        self.refresh()
        self.setupUi()
        self.show()

    def setupUi(self):
        # Method to setup the UI elements.

        # Connect the returnPressed signal of the line edit to create_tags method.
        self.line_edit.returnPressed.connect(self.create_tags)

    def create_tags(self):
        # Method to create tags from user input in the line edit.

        # Split the user input into new tags and remove empty tags.
        new_tags = [tag for tag in self.line_edit.text().split(', ') if tag]

        # Clear the line edit.
        self.line_edit.setText('')

        # Extend the tags list with the new tags, remove duplicates, and sort the tags.
        self.tags.extend(new_tags)
        self.tags = list(set(self.tags))
        self.tags.sort(key=lambda x: x.lower())

        # Refresh the tag bar to reflect the changes.
        self.refresh()

    def refresh(self):
        # Method to refresh the tag bar with the current tags.

        # Remove all existing widgets from the tag bar.
        for i in reversed(range(self.h_layout.count())):
            self.h_layout.itemAt(i).widget().setParent(None)

        # Add each tag to the tag bar.
        for tag in self.tags:
            self.add_tag_to_bar(tag)

        # Add the line edit to the tag bar and set focus on it.
        self.h_layout.addWidget(self.line_edit)
        self.line_edit.setFocus()

    def add_tag_to_bar(self, text):
        # Method to add a tag to the tag bar.

        # Create a QFrame for the tag.
        tag = QFrame()
        tag.setStyleSheet('border:1px solid rgb(192, 192, 192); border-radius: 4px;')
        tag.setContentsMargins(0, 0, 0, 0)

        # Set size policy for the tag frame.
        tag.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Minimum,
        )

        # Create a QHBoxLayout to add label and delete button to the tag frame.
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(10)
        tag.setLayout(hbox)

        # Create a label to display the tag text.
        label = QLabel(text)
        label.setStyleSheet('border:0px')

        # Set size policy for the tag label.
        label.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Minimum,
        )

        # Add the label to the tag frame.
        hbox.addWidget(label)

        # Create a delete button to remove the tag.
        x_button = QPushButton('x')
        x_button.setFixedSize(20, 20)
        x_button.setStyleSheet('border:0px; font-weight:bold')

        # Set size policy for the delete button.
        x_button.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Minimum,
        )

        # Connect the clicked signal of the delete button to the delete_tag method.
        x_button.clicked.connect(partial(self.delete_tag, text))

        # Add the delete button to the tag frame.
        hbox.addWidget(x_button)

        # Add the tag frame to the tag bar layout.
        self.h_layout.addWidget(tag)

        # Emit the tags_edited signal with the updated tags list.
        self.tags_edited.emit(self.tags)

    def delete_tag(self, tag_name):
        # Method to delete a tag from the tag bar.

        # Remove the tag from the tags list and refresh the tag bar.
        self.tags.remove(tag_name)
        self.refresh()

        # Emit the tags_edited signal with the updated tags list.
        self.tags_edited.emit(self.tags)

    def set_suggestions(self, tag_list: Sequence[Tag]):
        # Method to set tag suggestions for the line edit.

        # Create a QCompleter with tag labels from the given tag_list.
        tagsCompleter = QCompleter([tag.label for tag in tag_list])

        # Connect the activated signal of the completer to the create_tags method.
        tagsCompleter.activated.connect(self.create_tags)

        # Set case sensitivity for the completer.
        tagsCompleter.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)

        # Set the completer for the line edit.
        self.line_edit.setCompleter(tagsCompleter)
