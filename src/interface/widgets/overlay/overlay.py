
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

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPainter
from PySide6.QtWidgets import QGraphicsBlurEffect, QWidget


class Overlay(QWidget):
    # Custom widget class representing a popup-style overlay with centered text.

    overlay_text: str = ""  # Text to be displayed on the overlay.

    def paintEvent(self, event):
        # Paint event for drawing the overlay on the widget.

        popup_width, popup_height = 300, 120
        ow = int(self.size().width()/2-popup_width/2)  # Calculate the x-coordinate to center the overlay.
        oh = int(self.size().height()/2-popup_height/2)  # Calculate the y-coordinate to center the overlay.

        # Offset to center the text within the overlay.
        tolw, tolh = 80, -5

        qp = self.create_painter()
        qp.drawText(
            ow + popup_width // 2 - tolw,
            oh + popup_height // 2 - tolh,
            self.overlay_text,
        )

        qp.end()

    def create_painter(self):
        # Create a QPainter object with specified font and settings for drawing on the widget.

        font = QFont()
        font.setPixelSize(20)
        font.setItalic(True)

        qp = QPainter()
        qp.begin(self)

        # Enable antialiasing for smoother text rendering.
        qp.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        qp.setFont(font)
        # Set the text color to white.
        qp.setPen(Qt.GlobalColor.white)
        return qp

    def show(self):
        # Show the overlay with a blurred background.

        # Move the overlay to the top-left corner of the parent widget.
        self.move(0, 0)
        # Resize the overlay to match the size of the parent widget.
        self.resize(self.parent().size())
        self.blur_effect = QGraphicsBlurEffect()
        # Set the blur radius for the background effect.
        self.blur_effect.setBlurRadius(30)
        # Apply the blur effect to the parent widget.
        self.parent().widget().setGraphicsEffect(self.blur_effect)

        return super().show()

    def hide(self) -> None:
        # Hide the overlay and remove the blur effect from the parent widget.

        # Remove the blur effect from the parent widget.
        self.parent().widget().setGraphicsEffect(None)
        return super().hide()
