# from PySide6 import
from functools import partial

from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QWidget)


class TagBar(QWidget):
    def __init__(self, parent):
        super(TagBar, self).__init__()
        self.setParent(parent)
        self.setWindowTitle('Tag Bar')
        self.tags = []
        self.h_layout = QHBoxLayout()
        self.setLayout(self.h_layout)
        self.line_edit = QLineEdit()
        self.line_edit.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.setContentsMargins(0,0,0,0)
        self.h_layout.setContentsMargins(0,0,0,0)
        self.refresh()
        self.setup_ui()
        self.show()

    def setup_ui(self):
        self.line_edit.returnPressed.connect(self.create_tags)

    def create_tags(self):
        new_tags = self.line_edit.text().split(', ')
        self.line_edit.setText('')
        self.tags.extend(new_tags)
        self.tags = list(set(self.tags))
        self.tags.sort(key=lambda x: x.lower())
        self.refresh()

    def refresh(self):
        for i in reversed(range(self.h_layout.count())):
            self.h_layout.itemAt(i).widget().setParent(None)
        for tag in self.tags:
            self.add_tag_to_bar(tag)
        self.h_layout.addWidget(self.line_edit)
        self.line_edit.setFocus()

    def add_tag_to_bar(self, text):
        tag = QFrame()
        tag.setStyleSheet('border:1px solid rgb(192, 192, 192); border-radius: 4px;')
        tag.setContentsMargins(0,0,0,0)
        tag.setFixedHeight(28)
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)
        hbox.setSpacing(10)
        tag.setLayout(hbox)
        label = QLabel(text)
        label.setStyleSheet('border:0px')
        label.setFixedHeight(16)
        hbox.addWidget(label)
        x_button = QPushButton('x')
        x_button.setFixedSize(20, 20)
        x_button.setStyleSheet('border:0px; font-weight:bold')
        x_button.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        x_button.clicked.connect(partial(self.delete_tag, text))
        hbox.addWidget(x_button)
        tag.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        self.h_layout.addWidget(tag)

    def delete_tag(self, tag_name):
        self.tags.remove(tag_name)
        self.refresh()
