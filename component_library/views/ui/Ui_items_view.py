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
    QLabel, QLineEdit, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from component_library.views.items_widget import ItemWigdet

class Ui_itemsView(object):
    def setupUi(self, itemsView):
        if not itemsView.objectName():
            itemsView.setObjectName(u"itemsView")
        itemsView.resize(885, 552)
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

        self.searchAreaFrame = QFrame(self.searchWidget)
        self.searchAreaFrame.setObjectName(u"searchAreaFrame")
        self.searchAreaFrame.setMinimumSize(QSize(250, 0))
        self.searchAreaFrame.setMaximumSize(QSize(16777210, 16777215))
        self.searchAreaFrame.setStyleSheet(u"border: 1px solid #4a4a4a;\n"
"border-radius : 15px;")
        self.searchAreaFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.searchAreaFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.searchAreaFrame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.searchLineEdit = QLineEdit(self.searchAreaFrame)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchLineEdit.sizePolicy().hasHeightForWidth())
        self.searchLineEdit.setSizePolicy(sizePolicy1)
        self.searchLineEdit.setStyleSheet(u"border: 0px ;\n"
"")

        self.verticalLayout_2.addWidget(self.searchLineEdit)


        self.horizontalLayout_2.addWidget(self.searchAreaFrame)


        self.horizontalLayout_7.addWidget(self.searchWidget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.sortWidget = QWidget(self.titleFrame)
        self.sortWidget.setObjectName(u"sortWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.sortWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sortLabel = QLabel(self.sortWidget)
        self.sortLabel.setObjectName(u"sortLabel")
        sizePolicy.setHeightForWidth(self.sortLabel.sizePolicy().hasHeightForWidth())
        self.sortLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.sortLabel)

        self.sortComboBox = QComboBox(self.sortWidget)
        self.sortComboBox.addItem("")
        self.sortComboBox.addItem("")
        self.sortComboBox.setObjectName(u"sortComboBox")

        self.horizontalLayout_3.addWidget(self.sortComboBox)


        self.horizontalLayout_7.addWidget(self.sortWidget)

        self.filterWidget = QWidget(self.titleFrame)
        self.filterWidget.setObjectName(u"filterWidget")
        self.horizontalLayout_6 = QHBoxLayout(self.filterWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.filterLabel = QLabel(self.filterWidget)
        self.filterLabel.setObjectName(u"filterLabel")
        sizePolicy.setHeightForWidth(self.filterLabel.sizePolicy().hasHeightForWidth())
        self.filterLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.filterLabel)

        self.filterComboBox = QComboBox(self.filterWidget)
        self.filterComboBox.addItem("")
        self.filterComboBox.setObjectName(u"filterComboBox")

        self.horizontalLayout_6.addWidget(self.filterComboBox)


        self.horizontalLayout_7.addWidget(self.filterWidget)


        self.verticalLayout.addWidget(self.titleFrame)

        self.scrollArea = QScrollArea(itemsView)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContentItemsWidget = ItemWigdet()
        self.scrollAreaContentItemsWidget.setObjectName(u"scrollAreaContentItemsWidget")
        self.scrollAreaContentItemsWidget.setGeometry(QRect(0, 0, 869, 479))
        self.scrollArea.setWidget(self.scrollAreaContentItemsWidget)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(itemsView)

        QMetaObject.connectSlotsByName(itemsView)
    # setupUi

    def retranslateUi(self, itemsView):
        itemsView.setWindowTitle(QCoreApplication.translate("itemsView", u"Form", None))
        self.searchLabel.setText(QCoreApplication.translate("itemsView", u"Search", None))
        self.sortLabel.setText(QCoreApplication.translate("itemsView", u"sort", None))
        self.sortComboBox.setItemText(0, QCoreApplication.translate("itemsView", u"Rating", None))
        self.sortComboBox.setItemText(1, QCoreApplication.translate("itemsView", u"Preference", None))

        self.filterLabel.setText(QCoreApplication.translate("itemsView", u"filter", None))
        self.filterComboBox.setItemText(0, QCoreApplication.translate("itemsView", u"Category", None))

    # retranslateUi
