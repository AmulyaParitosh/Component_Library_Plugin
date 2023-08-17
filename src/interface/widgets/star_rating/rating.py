
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

from __future__ import annotations

from enum import Enum

from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget


class Star(QLabel):
    # Custom QLabel representing a star.

    class State(Enum):
        # Enum class to represent star states (filled or empty).
        Empty = "src/interface/resources/emptystar.png"
        Filled = "src/interface/resources/filledstar.png"

    def __init__(self, parent):
        # Constructor to initialize the Star.

        super().__init__(parent)

        # Set the fixed size of the star.
        self.setFixedSize(QSize(25, 25))

        # Enable scaled contents to resize the star while maintaining its aspect ratio.
        self.setScaledContents(True)

        # Initialize the state of the star.
        self.state = None

        # Set the default state of the star to empty.
        self.setState(self.State.Empty)

    def setState(self, state: Star.State):
        # Method to set the state of the star.

        if self.state == state:
            return

        # Set the state of the star and update its pixmap accordingly.
        self.state = state
        self.setPixmap(QPixmap(state.value))


class StarRating(QWidget):
    # Custom QWidget class to represent a star rating system.

    def __init__(self, parent: QWidget | None = None, default_value: float = 0, max_value: int = 5) -> None:
        # Constructor to initialize the StarRating.

        super().__init__(parent)

        # Initialize the current value and the maximum value for the star rating.
        self.value: float = default_value
        self.max_value: int = max_value

        # Setup the user interface.
        self.setupUi()

    def setupUi(self):
        # Method to setup the user interface elements.

        # Create a horizontal layout for the star rating.
        self.hbox_layout = QHBoxLayout()
        self.setLayout(self.hbox_layout)

        # Create a label to display the current value of the star rating.
        self.value_label = QLabel()
        self.value_label.setFont(QFont('Arial', 14))
        self.hbox_layout.addWidget(self.value_label)

        # Create stars and add them to the layout based on the maximum value.
        for i in range(1, self.max_value + 1):
            star = Star(self)
            if i <= self.value:
                star.setState(Star.State.Filled)
            self.hbox_layout.addWidget(star)

    def setRating(self, rating: float):
        # Method to set the star rating value.

        # Update the value and display it on the value label.
        self.value = rating
        self.value_label.setNum(self.value)

        # Update the state of each star based on the current value.
        for i in range(1, self.hbox_layout.count()):
            star: Star = self.hbox_layout.itemAt(i).widget()

            if i <= self.value:
                star.setState(Star.State.Filled)
            else:
                star.setState(Star.State.Empty)
