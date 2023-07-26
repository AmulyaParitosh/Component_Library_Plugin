# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'component_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from src.interface.widgets import (FileItem, FileList, TagBar)

class Ui_ComponentCreationForm(object):
    def setupUi(self, ComponentCreationForm):
        if not ComponentCreationForm.objectName():
            ComponentCreationForm.setObjectName(u"ComponentCreationForm")
        ComponentCreationForm.resize(686, 871)
        self.verticalLayout = QVBoxLayout(ComponentCreationForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.componentNameWidget = QWidget(ComponentCreationForm)
        self.componentNameWidget.setObjectName(u"componentNameWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.componentNameWidget.sizePolicy().hasHeightForWidth())
        self.componentNameWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.componentNameWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.componentNameLabel = QLabel(self.componentNameWidget)
        self.componentNameLabel.setObjectName(u"componentNameLabel")

        self.horizontalLayout_3.addWidget(self.componentNameLabel)

        self.componentNameInput = QLineEdit(self.componentNameWidget)
        self.componentNameInput.setObjectName(u"componentNameInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.componentNameInput.sizePolicy().hasHeightForWidth())
        self.componentNameInput.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(18)
        self.componentNameInput.setFont(font)

        self.horizontalLayout_3.addWidget(self.componentNameInput)


        self.verticalLayout.addWidget(self.componentNameWidget)

        self.metadataWidget = QWidget(ComponentCreationForm)
        self.metadataWidget.setObjectName(u"metadataWidget")
        sizePolicy.setHeightForWidth(self.metadataWidget.sizePolicy().hasHeightForWidth())
        self.metadataWidget.setSizePolicy(sizePolicy)
        self.metadataWidget.setMouseTracking(False)
        self.metadataWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.gridLayout = QGridLayout(self.metadataWidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.authorLabel = QLabel(self.metadataWidget)
        self.authorLabel.setObjectName(u"authorLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.authorLabel.sizePolicy().hasHeightForWidth())
        self.authorLabel.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.authorLabel, 1, 0, 1, 1)

        self.maintainerInput = QLineEdit(self.metadataWidget)
        self.maintainerInput.setObjectName(u"maintainerInput")
        sizePolicy1.setHeightForWidth(self.maintainerInput.sizePolicy().hasHeightForWidth())
        self.maintainerInput.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(12)
        self.maintainerInput.setFont(font1)

        self.gridLayout.addWidget(self.maintainerInput, 2, 1, 1, 1)

        self.mainteinerLabel = QLabel(self.metadataWidget)
        self.mainteinerLabel.setObjectName(u"mainteinerLabel")
        sizePolicy.setHeightForWidth(self.mainteinerLabel.sizePolicy().hasHeightForWidth())
        self.mainteinerLabel.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.mainteinerLabel, 2, 0, 1, 1)

        self.licenseInput = QComboBox(self.metadataWidget)
        self.licenseInput.setObjectName(u"licenseInput")
        sizePolicy1.setHeightForWidth(self.licenseInput.sizePolicy().hasHeightForWidth())
        self.licenseInput.setSizePolicy(sizePolicy1)
        self.licenseInput.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.licenseInput, 4, 1, 1, 1)

        self.tagsWidget = TagBar(self.metadataWidget)
        self.tagsWidget.setObjectName(u"tagsWidget")
        sizePolicy1.setHeightForWidth(self.tagsWidget.sizePolicy().hasHeightForWidth())
        self.tagsWidget.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.tagsWidget, 3, 1, 1, 1)

        self.licenseLabel = QLabel(self.metadataWidget)
        self.licenseLabel.setObjectName(u"licenseLabel")
        sizePolicy.setHeightForWidth(self.licenseLabel.sizePolicy().hasHeightForWidth())
        self.licenseLabel.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.licenseLabel, 4, 0, 1, 1)

        self.tagsLabel = QLabel(self.metadataWidget)
        self.tagsLabel.setObjectName(u"tagsLabel")
        sizePolicy2.setHeightForWidth(self.tagsLabel.sizePolicy().hasHeightForWidth())
        self.tagsLabel.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.tagsLabel, 3, 0, 1, 1)

        self.authorInput = QLineEdit(self.metadataWidget)
        self.authorInput.setObjectName(u"authorInput")
        sizePolicy1.setHeightForWidth(self.authorInput.sizePolicy().hasHeightForWidth())
        self.authorInput.setSizePolicy(sizePolicy1)
        self.authorInput.setFont(font1)

        self.gridLayout.addWidget(self.authorInput, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.metadataWidget)

        self.compLabel = QLabel(ComponentCreationForm)
        self.compLabel.setObjectName(u"compLabel")
        sizePolicy1.setHeightForWidth(self.compLabel.sizePolicy().hasHeightForWidth())
        self.compLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.compLabel)

        self.componentFiles = FileList(ComponentCreationForm)
        self.componentFiles.setObjectName(u"componentFiles")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.componentFiles.sizePolicy().hasHeightForWidth())
        self.componentFiles.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.componentFiles)

        self.thumbLabel = QLabel(ComponentCreationForm)
        self.thumbLabel.setObjectName(u"thumbLabel")
        sizePolicy1.setHeightForWidth(self.thumbLabel.sizePolicy().hasHeightForWidth())
        self.thumbLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.thumbLabel)

        self.thumbnailFile = FileItem(ComponentCreationForm)
        self.thumbnailFile.setObjectName(u"thumbnailFile")
        sizePolicy1.setHeightForWidth(self.thumbnailFile.sizePolicy().hasHeightForWidth())
        self.thumbnailFile.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.thumbnailFile)

        self.descriptionLabel = QLabel(ComponentCreationForm)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        sizePolicy.setHeightForWidth(self.descriptionLabel.sizePolicy().hasHeightForWidth())
        self.descriptionLabel.setSizePolicy(sizePolicy)
        self.descriptionLabel.setMaximumSize(QSize(16777213, 16777215))

        self.verticalLayout.addWidget(self.descriptionLabel)

        self.descriptionInput = QPlainTextEdit(ComponentCreationForm)
        self.descriptionInput.setObjectName(u"descriptionInput")
        sizePolicy1.setHeightForWidth(self.descriptionInput.sizePolicy().hasHeightForWidth())
        self.descriptionInput.setSizePolicy(sizePolicy1)
        self.descriptionInput.setFont(font1)

        self.verticalLayout.addWidget(self.descriptionInput)

        self.bottomWidget = QWidget(ComponentCreationForm)
        self.bottomWidget.setObjectName(u"bottomWidget")
        sizePolicy.setHeightForWidth(self.bottomWidget.sizePolicy().hasHeightForWidth())
        self.bottomWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.bottomWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.bottomWidget)


        self.retranslateUi(ComponentCreationForm)

        QMetaObject.connectSlotsByName(ComponentCreationForm)
    # setupUi

    def retranslateUi(self, ComponentCreationForm):
        ComponentCreationForm.setWindowTitle(QCoreApplication.translate("ComponentCreationForm", u"Dialog", None))
        self.componentNameLabel.setText(QCoreApplication.translate("ComponentCreationForm", u"<html><head/><body><p><span style=\" font-size:18pt;\">Component Name</span></p></body></html>", None))
        self.componentNameInput.setInputMask("")
        self.componentNameInput.setPlaceholderText(QCoreApplication.translate("ComponentCreationForm", u"name of the component", None))
        self.authorLabel.setText(QCoreApplication.translate("ComponentCreationForm", u"<html><head/><body><p><span style=\" font-size:12pt;\">Author:</span></p></body></html>", None))
        self.maintainerInput.setPlaceholderText(QCoreApplication.translate("ComponentCreationForm", u"maintailer@email.com", None))
        self.mainteinerLabel.setText(QCoreApplication.translate("ComponentCreationForm", u"<html><head/><body><p><span style=\" font-size:12pt;\">Maintainer:</span></p></body></html>", None))
        self.licenseLabel.setText(QCoreApplication.translate("ComponentCreationForm", u"<html><head/><body><p><span style=\" font-size:12pt;\">License:</span></p></body></html>", None))
        self.tagsLabel.setText(QCoreApplication.translate("ComponentCreationForm", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tags</span></p></body></html>", None))
        self.authorInput.setPlaceholderText(QCoreApplication.translate("ComponentCreationForm", u"author@email.com", None))
        self.compLabel.setText(QCoreApplication.translate("ComponentCreationForm", u"<html><head/><body><p><span style=\" font-size:12pt;\">Component Files</span></p></body></html>", None))
        self.thumbLabel.setText(QCoreApplication.translate("ComponentCreationForm", u"<html><head/><body><p><span style=\" font-size:12pt;\">Thumbnail File</span></p></body></html>", None))
        self.descriptionLabel.setText(QCoreApplication.translate("ComponentCreationForm", u"<html><head/><body><p><span style=\" font-size:12pt;\">Description</span></p></body></html>", None))
        self.descriptionInput.setPlaceholderText(QCoreApplication.translate("ComponentCreationForm", u"a short description about the component", None))
    # retranslateUi

