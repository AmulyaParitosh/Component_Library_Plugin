#!.venv/bin/python
import sys

from PySide6.QtWidgets import QApplication

from src import Window

# Create a QApplication instance to manage the application's GUI event loop
app = QApplication(sys.argv)

# Instantiate the Window class from the 'src' module, representing the main application window
plugin = Window()

# Start the application's GUI event loop, allowing it to respond to user interactions and events
# The program will remain in the event loop until the application is terminated
sys.exit(app.exec())
