# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plugin.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

from src.interface.views import (OnlineDetailedView, GridView)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1411, 898)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMinimumSize(QSize(150, 0))
        self.sidebar.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout = QVBoxLayout(self.sidebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.controlArea = QFrame(self.sidebar)
        self.controlArea.setObjectName(u"controlArea")
        self.controlArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.controlArea.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.controlArea)

        self.notificationArea = QFrame(self.sidebar)
        self.notificationArea.setObjectName(u"notificationArea")
        self.notificationArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.notificationArea.setFrameShadow(QFrame.Shadow.Raised)
        self.notificationAreaLayout = QVBoxLayout(self.notificationArea)
        self.notificationAreaLayout.setObjectName(u"notificationAreaLayout")

        self.verticalLayout.addWidget(self.notificationArea)


        self.horizontalLayout.addWidget(self.sidebar)

        self.mainArea = QFrame(self.centralwidget)
        self.mainArea.setObjectName(u"mainArea")
        self.mainArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainArea.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainArea)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.mainArea)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.repoBrowser = GridView()
        self.repoBrowser.setObjectName(u"repoBrowser")
        self.stackedWidget.addWidget(self.repoBrowser)
        self.componentDetail = OnlineDetailedView()
        self.componentDetail.setObjectName(u"componentDetail")
        self.stackedWidget.addWidget(self.componentDetail)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.mainArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi
