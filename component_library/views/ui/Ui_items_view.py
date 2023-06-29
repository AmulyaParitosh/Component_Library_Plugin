# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'items_view.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from component_library.components.checkable_comboBox import CheckableComboBox
from component_library.components.tag_bar import TagBar
from component_library.views.items_widget import ItemWigdet

class Ui_itemsView(object):
    def setupUi(self, itemsView):
        if not itemsView.objectName():
            itemsView.setObjectName(u"itemsView")
        itemsView.resize(1136, 816)
        self.verticalLayout = QVBoxLayout(itemsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleFrame = QFrame(itemsView)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setMaximumSize(QSize(16777215, 51))
        self.titleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.searchWidget = QWidget(self.titleFrame)
        self.searchWidget.setObjectName(u"searchWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.searchWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchLabel = QLabel(self.searchWidget)
        self.searchLabel.setObjectName(u"searchLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLabel.sizePolicy().hasHeightForWidth())
        self.searchLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.searchLabel)

        self.searchLineEdit = QLineEdit(self.searchWidget)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchLineEdit.sizePolicy().hasHeightForWidth())
        self.searchLineEdit.setSizePolicy(sizePolicy1)
        self.searchLineEdit.setMinimumSize(QSize(0, 35))
        self.searchLineEdit.setStyleSheet(u"border: 0px ;\n"
"")

        self.horizontalLayout_2.addWidget(self.searchLineEdit)


        self.horizontalLayout_7.addWidget(self.searchWidget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.sortWidget = QWidget(self.titleFrame)
        self.sortWidget.setObjectName(u"sortWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.sortWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sortLabel = QLabel(self.sortWidget)
        self.sortLabel.setObjectName(u"sortLabel")
        sizePolicy.setHeightForWidth(self.sortLabel.sizePolicy().hasHeightForWidth())
        self.sortLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.sortLabel)

        self.sortComboBox = QComboBox(self.sortWidget)
        self.sortComboBox.addItem("")
        self.sortComboBox.addItem("")
        self.sortComboBox.addItem("")
        self.sortComboBox.addItem("")
        self.sortComboBox.setObjectName(u"sortComboBox")

        self.horizontalLayout_4.addWidget(self.sortComboBox)


        self.horizontalLayout_7.addWidget(self.sortWidget)

        self.orderWidget = QWidget(self.titleFrame)
        self.orderWidget.setObjectName(u"orderWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.orderWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.orderLabel = QLabel(self.orderWidget)
        self.orderLabel.setObjectName(u"orderLabel")
        sizePolicy.setHeightForWidth(self.orderLabel.sizePolicy().hasHeightForWidth())
        self.orderLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.orderLabel)

        self.orderComboBox = QComboBox(self.orderWidget)
        self.orderComboBox.addItem("")
        self.orderComboBox.addItem("")
        self.orderComboBox.setObjectName(u"orderComboBox")

        self.horizontalLayout_3.addWidget(self.orderComboBox)


        self.horizontalLayout_7.addWidget(self.orderWidget)


        self.verticalLayout.addWidget(self.titleFrame)

        self.titleFrame_2 = QFrame(itemsView)
        self.titleFrame_2.setObjectName(u"titleFrame_2")
        self.titleFrame_2.setMaximumSize(QSize(16777215, 51))
        self.titleFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.titleFrame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.tagBarWidget = QWidget(self.titleFrame_2)
        self.tagBarWidget.setObjectName(u"tagBarWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.tagBarWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tagBarLabel = QLabel(self.tagBarWidget)
        self.tagBarLabel.setObjectName(u"tagBarLabel")
        sizePolicy.setHeightForWidth(self.tagBarLabel.sizePolicy().hasHeightForWidth())
        self.tagBarLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.tagBarLabel)

        self.tagBar = TagBar(self.tagBarWidget)
        self.tagBar.setObjectName(u"tagBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tagBar.sizePolicy().hasHeightForWidth())
        self.tagBar.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.tagBar)


        self.horizontalLayout_8.addWidget(self.tagBarWidget)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.fileTypeWidget = QWidget(self.titleFrame_2)
        self.fileTypeWidget.setObjectName(u"fileTypeWidget")
        self.horizontalLayout_11 = QHBoxLayout(self.fileTypeWidget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fileTypeLabel = QLabel(self.fileTypeWidget)
        self.fileTypeLabel.setObjectName(u"fileTypeLabel")
        sizePolicy.setHeightForWidth(self.fileTypeLabel.sizePolicy().hasHeightForWidth())
        self.fileTypeLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fileTypeLabel)

        self.fileTypeComboBox = CheckableComboBox(self.fileTypeWidget)
        self.fileTypeComboBox.addItem("")
        self.fileTypeComboBox.addItem("")
        self.fileTypeComboBox.addItem("")
        self.fileTypeComboBox.addItem("")
        self.fileTypeComboBox.addItem("")
        self.fileTypeComboBox.setObjectName(u"fileTypeComboBox")
        self.fileTypeComboBox.setMinimumSize(QSize(106, 0))
        self.fileTypeComboBox.setEditable(False)

        self.horizontalLayout_11.addWidget(self.fileTypeComboBox)


        self.horizontalLayout_8.addWidget(self.fileTypeWidget)


        self.verticalLayout.addWidget(self.titleFrame_2)

        self.scrollArea = QScrollArea(itemsView)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContentItemsWidget = ItemWigdet()
        self.scrollAreaContentItemsWidget.setObjectName(u"scrollAreaContentItemsWidget")
        self.scrollAreaContentItemsWidget.setGeometry(QRect(0, 0, 1120, 637))
        self.scrollArea.setWidget(self.scrollAreaContentItemsWidget)

        self.verticalLayout.addWidget(self.scrollArea)

        self.bottomBar = QWidget(itemsView)
        self.bottomBar.setObjectName(u"bottomBar")
        self.horizontalLayout = QHBoxLayout(self.bottomBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bottomBarSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.bottomBarSpacer)

        self.prevButton = QPushButton(self.bottomBar)
        self.prevButton.setObjectName(u"prevButton")

        self.horizontalLayout.addWidget(self.prevButton)

        self.nextButton = QPushButton(self.bottomBar)
        self.nextButton.setObjectName(u"nextButton")

        self.horizontalLayout.addWidget(self.nextButton)


        self.verticalLayout.addWidget(self.bottomBar)


        self.retranslateUi(itemsView)

        QMetaObject.connectSlotsByName(itemsView)
    # setupUi

    def retranslateUi(self, itemsView):
        itemsView.setWindowTitle(QCoreApplication.translate("itemsView", u"Form", None))
        self.searchLabel.setText(QCoreApplication.translate("itemsView", u"Search", None))
        self.sortLabel.setText(QCoreApplication.translate("itemsView", u"sort", None))
        self.sortComboBox.setItemText(0, QCoreApplication.translate("itemsView", u"Name", None))
        self.sortComboBox.setItemText(1, QCoreApplication.translate("itemsView", u"Created", None))
        self.sortComboBox.setItemText(2, QCoreApplication.translate("itemsView", u"Updated", None))
        self.sortComboBox.setItemText(3, QCoreApplication.translate("itemsView", u"Rating", None))

        self.orderLabel.setText(QCoreApplication.translate("itemsView", u"order", None))
        self.orderComboBox.setItemText(0, QCoreApplication.translate("itemsView", u"ascending", None))
        self.orderComboBox.setItemText(1, QCoreApplication.translate("itemsView", u"descending", None))

        self.tagBarLabel.setText(QCoreApplication.translate("itemsView", u"Tags", None))
        self.fileTypeLabel.setText(QCoreApplication.translate("itemsView", u"filetype", None))
        self.fileTypeComboBox.setItemText(0, QCoreApplication.translate("itemsView", u"step", None))
        self.fileTypeComboBox.setItemText(1, QCoreApplication.translate("itemsView", u"fcstd", None))
        self.fileTypeComboBox.setItemText(2, QCoreApplication.translate("itemsView", u"fcstd1", None))
        self.fileTypeComboBox.setItemText(3, QCoreApplication.translate("itemsView", u"stl", None))
        self.fileTypeComboBox.setItemText(4, QCoreApplication.translate("itemsView", u"stp", None))

        self.prevButton.setText(QCoreApplication.translate("itemsView", u"Prev", None))
        self.nextButton.setText(QCoreApplication.translate("itemsView", u"Next", None))
    # retranslateUi

