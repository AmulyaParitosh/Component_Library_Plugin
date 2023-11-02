# SPDX-License-Identifier: MIT
# --------------------------------------------------------------
# |																|
# |             Copyright 2023 - 2023, Amulya Paritosh			|
# |																|
# |  This file is part of Component Library Plugin for FreeCAD.	|
# |																|
# |               This file was created as a part of				|
# |              Google Summer Of Code Program - 2023			|
# |																|
# --------------------------------------------------------------

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailed_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from src.interface.widgets import StarRating


class Ui_detailedWidget(object):
    def setupUi(self, detailedWidget):
        if not detailedWidget.objectName():
            detailedWidget.setObjectName("detailedWidget")
        detailedWidget.resize(1128, 831)
        self.verticalLayout = QVBoxLayout(detailedWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topArea = QWidget(detailedWidget)
        self.topArea.setObjectName("topArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topArea.sizePolicy().hasHeightForWidth())
        self.topArea.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.topArea)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backPushButton = QPushButton(self.topArea)
        self.backPushButton.setObjectName("backPushButton")

        self.horizontalLayout.addWidget(self.backPushButton)

        self.horizontalSpacer = QSpacerItem(
            807, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.controlArea = QHBoxLayout()
        self.controlArea.setObjectName("controlArea")

        self.horizontalLayout.addLayout(self.controlArea)

        self.filetypeComboBox = QComboBox(self.topArea)
        self.filetypeComboBox.setObjectName("filetypeComboBox")

        self.horizontalLayout.addWidget(self.filetypeComboBox)

        self.verticalLayout.addWidget(self.topArea)

        self.processesArea = QVBoxLayout()
        self.processesArea.setObjectName("processesArea")

        self.verticalLayout.addLayout(self.processesArea)

        self.mainScrollArea = QScrollArea(detailedWidget)
        self.mainScrollArea.setObjectName("mainScrollArea")
        self.mainScrollArea.setWidgetResizable(True)
        self.mainScrollAreaWidgetContents = QWidget()
        self.mainScrollAreaWidgetContents.setObjectName("mainScrollAreaWidgetContents")
        self.mainScrollAreaWidgetContents.setGeometry(QRect(0, 0, 1112, 755))
        self.verticalLayout_2 = QVBoxLayout(self.mainScrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelFrame = QFrame(self.mainScrollAreaWidgetContents)
        self.labelFrame.setObjectName("labelFrame")
        sizePolicy.setHeightForWidth(self.labelFrame.sizePolicy().hasHeightForWidth())
        self.labelFrame.setSizePolicy(sizePolicy)
        self.labelFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.labelFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.labelFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.contentLabel = QLabel(self.labelFrame)
        self.contentLabel.setObjectName("contentLabel")

        self.horizontalLayout_2.addWidget(self.contentLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_2.addWidget(self.labelFrame)

        self.thumbnailArea = QWidget(self.mainScrollAreaWidgetContents)
        self.thumbnailArea.setObjectName("thumbnailArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.thumbnailArea.sizePolicy().hasHeightForWidth())
        self.thumbnailArea.setSizePolicy(sizePolicy1)
        self.thumbnailArea.setMinimumSize(QSize(0, 250))
        self.thumbnailArea.setMaximumSize(QSize(700, 350))
        self.thumbnailAreaHorizontalLayout = QHBoxLayout(self.thumbnailArea)
        self.thumbnailAreaHorizontalLayout.setObjectName("thumbnailAreaHorizontalLayout")

        self.verticalLayout_2.addWidget(self.thumbnailArea, 0, Qt.AlignmentFlag.AlignLeft)

        self.metadataFrame = QFrame(self.mainScrollAreaWidgetContents)
        self.metadataFrame.setObjectName("metadataFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.metadataFrame.sizePolicy().hasHeightForWidth())
        self.metadataFrame.setSizePolicy(sizePolicy2)
        self.metadataFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.metadataFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.metadataFrame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.descriptionWidget = QWidget(self.metadataFrame)
        self.descriptionWidget.setObjectName("descriptionWidget")
        self.verticalLayout_3 = QVBoxLayout(self.descriptionWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.descriptionLabel = QLabel(self.descriptionWidget)
        self.descriptionLabel.setObjectName("descriptionLabel")
        sizePolicy.setHeightForWidth(self.descriptionLabel.sizePolicy().hasHeightForWidth())
        self.descriptionLabel.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.descriptionLabel)

        self.descriptionTextBrowser = QTextBrowser(self.descriptionWidget)
        self.descriptionTextBrowser.setObjectName("descriptionTextBrowser")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.descriptionTextBrowser.sizePolicy().hasHeightForWidth())
        self.descriptionTextBrowser.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.descriptionTextBrowser)

        self.horizontalLayout_5.addWidget(self.descriptionWidget)

        self.saparator = QFrame(self.metadataFrame)
        self.saparator.setObjectName("saparator")
        self.saparator.setFrameShape(QFrame.Shape.VLine)
        self.saparator.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.saparator)

        self.metadataWidget = QWidget(self.metadataFrame)
        self.metadataWidget.setObjectName("metadataWidget")
        self.metadataWidget.setMouseTracking(False)
        self.metadataWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.gridLayout = QGridLayout(self.metadataWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.authorLabel = QLabel(self.metadataWidget)
        self.authorLabel.setObjectName("authorLabel")

        self.gridLayout.addWidget(self.authorLabel, 0, 0, 1, 1)

        self.authorValue = QLabel(self.metadataWidget)
        self.authorValue.setObjectName("authorValue")

        self.gridLayout.addWidget(self.authorValue, 0, 1, 1, 1)

        self.mainteinerLabel = QLabel(self.metadataWidget)
        self.mainteinerLabel.setObjectName("mainteinerLabel")

        self.gridLayout.addWidget(self.mainteinerLabel, 1, 0, 1, 1)

        self.maintainerValue = QLabel(self.metadataWidget)
        self.maintainerValue.setObjectName("maintainerValue")

        self.gridLayout.addWidget(self.maintainerValue, 1, 1, 1, 1)

        self.licenseLabel = QLabel(self.metadataWidget)
        self.licenseLabel.setObjectName("licenseLabel")

        self.gridLayout.addWidget(self.licenseLabel, 2, 0, 1, 1)

        self.licenseValue = QLabel(self.metadataWidget)
        self.licenseValue.setObjectName("licenseValue")

        self.gridLayout.addWidget(self.licenseValue, 2, 1, 1, 1)

        self.createdLabel = QLabel(self.metadataWidget)
        self.createdLabel.setObjectName("createdLabel")

        self.gridLayout.addWidget(self.createdLabel, 3, 0, 1, 1)

        self.createdValue = QLabel(self.metadataWidget)
        self.createdValue.setObjectName("createdValue")

        self.gridLayout.addWidget(self.createdValue, 3, 1, 1, 1)

        self.updatedLabel = QLabel(self.metadataWidget)
        self.updatedLabel.setObjectName("updatedLabel")

        self.gridLayout.addWidget(self.updatedLabel, 4, 0, 1, 1)

        self.updatedValue = QLabel(self.metadataWidget)
        self.updatedValue.setObjectName("updatedValue")

        self.gridLayout.addWidget(self.updatedValue, 4, 1, 1, 1)

        self.ratingLabel = QLabel(self.metadataWidget)
        self.ratingLabel.setObjectName("ratingLabel")

        self.gridLayout.addWidget(self.ratingLabel, 5, 0, 1, 1)

        self.ratingwidget = StarRating(self.metadataWidget)
        self.ratingwidget.setObjectName("ratingwidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ratingwidget.sizePolicy().hasHeightForWidth())
        self.ratingwidget.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.ratingwidget, 5, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_5.addWidget(self.metadataWidget)

        self.verticalLayout_2.addWidget(self.metadataFrame)

        self.mainScrollArea.setWidget(self.mainScrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.mainScrollArea)

        self.retranslateUi(detailedWidget)

        self.filetypeComboBox.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(detailedWidget)

    # setupUi

    def retranslateUi(self, detailedWidget):
        detailedWidget.setWindowTitle(QCoreApplication.translate("detailedWidget", "Form", None))
        self.backPushButton.setText(QCoreApplication.translate("detailedWidget", "Back", None))
        self.filetypeComboBox.setPlaceholderText(
            QCoreApplication.translate("detailedWidget", "filetype", None)
        )
        self.contentLabel.setText(
            QCoreApplication.translate(
                "detailedWidget",
                '<html><head/><body><p><span style=" font-size:28pt;">Component Label</span></p></body></html>',
                None,
            )
        )
        self.descriptionLabel.setText(
            QCoreApplication.translate(
                "detailedWidget",
                '<html><head/><body><p><span style=" font-size:18pt;">Description :</span></p></body></html>',
                None,
            )
        )
        self.authorLabel.setText(
            QCoreApplication.translate(
                "detailedWidget",
                '<html><head/><body><p><span style=" font-size:14pt;">Author:</span></p></body></html>',
                None,
            )
        )
        self.authorValue.setText("")
        self.mainteinerLabel.setText(
            QCoreApplication.translate(
                "detailedWidget",
                '<html><head/><body><p><span style=" font-size:14pt;">Maintainer:</span></p></body></html>',
                None,
            )
        )
        self.maintainerValue.setText("")
        self.licenseLabel.setText(
            QCoreApplication.translate(
                "detailedWidget",
                '<html><head/><body><p><span style=" font-size:14pt;">License:</span></p></body></html>',
                None,
            )
        )
        self.licenseValue.setText("")
        self.createdLabel.setText(
            QCoreApplication.translate(
                "detailedWidget",
                '<html><head/><body><p><span style=" font-size:14pt;">Created on:</span></p></body></html>',
                None,
            )
        )
        self.createdValue.setText("")
        self.updatedLabel.setText(
            QCoreApplication.translate(
                "detailedWidget",
                '<html><head/><body><p><span style=" font-size:14pt;">Upadted on:</span></p></body></html>',
                None,
            )
        )
        self.updatedValue.setText("")
        self.ratingLabel.setText(
            QCoreApplication.translate(
                "detailedWidget",
                '<html><head/><body><p><span style=" font-size:14pt;">Rating:</span></p></body></html>',
                None,
            )
        )

    # retranslateUi
