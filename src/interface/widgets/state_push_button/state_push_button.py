
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

import contextlib
from enum import Enum

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton


class StatefullPushButton(QPushButton):
    # Custom QPushButton class that manages different button states.

    def __init__(self, parent=None):
        super().__init__(parent)
        self.states = {}  # Dictionary to store different button states and their corresponding data.

    def register_state(self, state: Enum, slot: Slot | None, text: str, enable: bool):
        # Register a button state along with its properties.

        self.states[state] = {
            "slot": slot,       # Slot (function) to be connected when this state is active. Can be None.
            "text": text,       # Text to be displayed on the button when this state is active.
            "enable": enable,   # Enable or disable the button when this state is active.
        }

    def setState(self, state: Enum):
        # Set the button state based on the provided Enum value.

        if state not in self.states:
            raise ValueError(f"{state} not registered!")

        state_data = self.states[state]

        self.setText(state_data["text"])  # Set the button text based on the state.

        # Disconnect slots of other states, leaving only the slot for the current state connected.
        for key, value in self.states.items():
            if key == state:
                continue
            with contextlib.suppress(Exception):
                self.clicked.disconnect(value["slot"])

        if state_data["slot"]:
            # If the current state has a slot, connect it to the clicked signal of the button.
            self.clicked.connect(state_data["slot"])

        self.setEnabled(state_data["enable"])  # Set the enabled state of the button based on the state.
