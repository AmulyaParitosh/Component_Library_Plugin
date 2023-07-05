# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailed_view.ui'
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
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_detailedView(object):
    def setupUi(self, detailedView):
        if not detailedView.objectName():
            detailedView.setObjectName(u"detailedView")
        detailedView.resize(1128, 831)
        self.verticalLayout = QVBoxLayout(detailedView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topArea = QWidget(detailedView)
        self.topArea.setObjectName(u"topArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topArea.sizePolicy().hasHeightForWidth())
        self.topArea.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.topArea)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.backPushButton = QPushButton(self.topArea)
        self.backPushButton.setObjectName(u"backPushButton")

        self.horizontalLayout.addWidget(self.backPushButton)

        self.horizontalSpacer = QSpacerItem(807, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.downloadPushButton = QPushButton(self.topArea)
        self.downloadPushButton.setObjectName(u"downloadPushButton")

        self.horizontalLayout.addWidget(self.downloadPushButton)

        self.filetypeComboBox = QComboBox(self.topArea)
        self.filetypeComboBox.addItem("")
        self.filetypeComboBox.setObjectName(u"filetypeComboBox")

        self.horizontalLayout.addWidget(self.filetypeComboBox)


        self.verticalLayout.addWidget(self.topArea)

        self.mainScrollArea = QScrollArea(detailedView)
        self.mainScrollArea.setObjectName(u"mainScrollArea")
        self.mainScrollArea.setWidgetResizable(True)
        self.mainScrollAreaWidgetContents = QWidget()
        self.mainScrollAreaWidgetContents.setObjectName(u"mainScrollAreaWidgetContents")
        self.mainScrollAreaWidgetContents.setGeometry(QRect(0, 0, 1112, 763))
        self.verticalLayout_2 = QVBoxLayout(self.mainScrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelFrame = QFrame(self.mainScrollAreaWidgetContents)
        self.labelFrame.setObjectName(u"labelFrame")
        sizePolicy.setHeightForWidth(self.labelFrame.sizePolicy().hasHeightForWidth())
        self.labelFrame.setSizePolicy(sizePolicy)
        self.labelFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.labelFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.labelFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.contentLabel = QLabel(self.labelFrame)
        self.contentLabel.setObjectName(u"contentLabel")

        self.horizontalLayout_2.addWidget(self.contentLabel, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addWidget(self.labelFrame)

        self.thumbnailArea = QWidget(self.mainScrollAreaWidgetContents)
        self.thumbnailArea.setObjectName(u"thumbnailArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.thumbnailArea.sizePolicy().hasHeightForWidth())
        self.thumbnailArea.setSizePolicy(sizePolicy1)
        self.thumbnailArea.setMinimumSize(QSize(0, 250))
        self.thumbnailArea.setMaximumSize(QSize(700, 350))
        self.thumbnailAreaHorizontalLayout = QHBoxLayout(self.thumbnailArea)
        self.thumbnailAreaHorizontalLayout.setObjectName(u"thumbnailAreaHorizontalLayout")

        self.verticalLayout_2.addWidget(self.thumbnailArea, 0, Qt.AlignmentFlag.AlignLeft)

        self.metadataFrame = QFrame(self.mainScrollAreaWidgetContents)
        self.metadataFrame.setObjectName(u"metadataFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.metadataFrame.sizePolicy().hasHeightForWidth())
        self.metadataFrame.setSizePolicy(sizePolicy2)
        self.metadataFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.metadataFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.metadataFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.descriptionWidget = QWidget(self.metadataFrame)
        self.descriptionWidget.setObjectName(u"descriptionWidget")
        self.verticalLayout_3 = QVBoxLayout(self.descriptionWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.descriptionLabel = QLabel(self.descriptionWidget)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        sizePolicy.setHeightForWidth(self.descriptionLabel.sizePolicy().hasHeightForWidth())
        self.descriptionLabel.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.descriptionLabel)

        self.descriptionTextBrowser = QTextBrowser(self.descriptionWidget)
        self.descriptionTextBrowser.setObjectName(u"descriptionTextBrowser")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.descriptionTextBrowser.sizePolicy().hasHeightForWidth())
        self.descriptionTextBrowser.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.descriptionTextBrowser)


        self.horizontalLayout_5.addWidget(self.descriptionWidget)

        self.saparator = QFrame(self.metadataFrame)
        self.saparator.setObjectName(u"saparator")
        self.saparator.setFrameShape(QFrame.Shape.VLine)
        self.saparator.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.saparator)

        self.metadataWidget = QWidget(self.metadataFrame)
        self.metadataWidget.setObjectName(u"metadataWidget")
        self.metadataWidget.setMouseTracking(False)
        self.metadataWidget.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_5.addWidget(self.metadataWidget)


        self.verticalLayout_2.addWidget(self.metadataFrame)

        self.mainScrollArea.setWidget(self.mainScrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.mainScrollArea)


        self.retranslateUi(detailedView)

        QMetaObject.connectSlotsByName(detailedView)
    # setupUi

    def retranslateUi(self, detailedView):
        detailedView.setWindowTitle(QCoreApplication.translate("detailedView", u"Form", None))
        self.backPushButton.setText(QCoreApplication.translate("detailedView", u"Back", None))
        self.downloadPushButton.setText(QCoreApplication.translate("detailedView", u"Download", None))
        self.filetypeComboBox.setItemText(0, QCoreApplication.translate("detailedView", u"filetype", None))

        self.contentLabel.setText(QCoreApplication.translate("detailedView", u"<html><head/><body><p><span style=\" font-size:28pt;\">Component Label</span></p></body></html>", None))
        self.descriptionLabel.setText(QCoreApplication.translate("detailedView", u"<html><head/><body><p><span style=\" font-size:18pt;\">Description :</span></p></body></html>", None))
    # retranslateUi

