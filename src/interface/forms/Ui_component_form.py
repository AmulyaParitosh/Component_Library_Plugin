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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPlainTextEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from src.interface.widgets import TagBar

class Ui_componentCreationForm(object):
    def setupUi(self, componentCreationForm):
        if not componentCreationForm.objectName():
            componentCreationForm.setObjectName(u"componentCreationForm")
        componentCreationForm.resize(1079, 722)
        self.verticalLayout_2 = QVBoxLayout(componentCreationForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.componentNameWidget = QWidget(componentCreationForm)
        self.componentNameWidget.setObjectName(u"componentNameWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.componentNameInput.sizePolicy().hasHeightForWidth())
        self.componentNameInput.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(18)
        self.componentNameInput.setFont(font)

        self.horizontalLayout_3.addWidget(self.componentNameInput)


        self.verticalLayout_2.addWidget(self.componentNameWidget)

        self.formArea1 = QWidget(componentCreationForm)
        self.formArea1.setObjectName(u"formArea1")
        self.horizontalLayout_2 = QHBoxLayout(self.formArea1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.thumbnail = QWidget(self.formArea1)
        self.thumbnail.setObjectName(u"thumbnail")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.thumbnail.sizePolicy().hasHeightForWidth())
        self.thumbnail.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.thumbnail)

        self.descriptionWidget = QWidget(self.formArea1)
        self.descriptionWidget.setObjectName(u"descriptionWidget")
        sizePolicy1.setHeightForWidth(self.descriptionWidget.sizePolicy().hasHeightForWidth())
        self.descriptionWidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.descriptionWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.descriptionLabel = QLabel(self.descriptionWidget)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.verticalLayout_3.addWidget(self.descriptionLabel)

        self.descriptionInput = QPlainTextEdit(self.descriptionWidget)
        self.descriptionInput.setObjectName(u"descriptionInput")
        font1 = QFont()
        font1.setPointSize(12)
        self.descriptionInput.setFont(font1)

        self.verticalLayout_3.addWidget(self.descriptionInput)


        self.horizontalLayout_2.addWidget(self.descriptionWidget)


        self.verticalLayout_2.addWidget(self.formArea1)

        self.formArea2 = QWidget(componentCreationForm)
        self.formArea2.setObjectName(u"formArea2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.formArea2.sizePolicy().hasHeightForWidth())
        self.formArea2.setSizePolicy(sizePolicy3)
        self.horizontalLayout_4 = QHBoxLayout(self.formArea2)
        self.horizontalLayout_4.setSpacing(18)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.metadataWidget = QWidget(self.formArea2)
        self.metadataWidget.setObjectName(u"metadataWidget")
        self.metadataWidget.setMouseTracking(False)
        self.metadataWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.gridLayout = QGridLayout(self.metadataWidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.thumbUrlLabel = QLabel(self.metadataWidget)
        self.thumbUrlLabel.setObjectName(u"thumbUrlLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.thumbUrlLabel.sizePolicy().hasHeightForWidth())
        self.thumbUrlLabel.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.thumbUrlLabel, 1, 0, 1, 1)

        self.licenseLabel = QLabel(self.metadataWidget)
        self.licenseLabel.setObjectName(u"licenseLabel")
        sizePolicy3.setHeightForWidth(self.licenseLabel.sizePolicy().hasHeightForWidth())
        self.licenseLabel.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.licenseLabel, 6, 0, 1, 1)

        self.authorInput = QLineEdit(self.metadataWidget)
        self.authorInput.setObjectName(u"authorInput")
        sizePolicy2.setHeightForWidth(self.authorInput.sizePolicy().hasHeightForWidth())
        self.authorInput.setSizePolicy(sizePolicy2)
        self.authorInput.setFont(font1)

        self.gridLayout.addWidget(self.authorInput, 3, 1, 1, 1)

        self.maintainerInput = QLineEdit(self.metadataWidget)
        self.maintainerInput.setObjectName(u"maintainerInput")
        sizePolicy2.setHeightForWidth(self.maintainerInput.sizePolicy().hasHeightForWidth())
        self.maintainerInput.setSizePolicy(sizePolicy2)
        self.maintainerInput.setFont(font1)

        self.gridLayout.addWidget(self.maintainerInput, 4, 1, 1, 1)

        self.compUrlInput = QLineEdit(self.metadataWidget)
        self.compUrlInput.setObjectName(u"compUrlInput")
        sizePolicy2.setHeightForWidth(self.compUrlInput.sizePolicy().hasHeightForWidth())
        self.compUrlInput.setSizePolicy(sizePolicy2)
        self.compUrlInput.setFont(font1)

        self.gridLayout.addWidget(self.compUrlInput, 0, 1, 1, 1)

        self.mainteinerLabel = QLabel(self.metadataWidget)
        self.mainteinerLabel.setObjectName(u"mainteinerLabel")
        sizePolicy3.setHeightForWidth(self.mainteinerLabel.sizePolicy().hasHeightForWidth())
        self.mainteinerLabel.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.mainteinerLabel, 4, 0, 1, 1)

        self.licenseInput = QComboBox(self.metadataWidget)
        self.licenseInput.setObjectName(u"licenseInput")
        sizePolicy2.setHeightForWidth(self.licenseInput.sizePolicy().hasHeightForWidth())
        self.licenseInput.setSizePolicy(sizePolicy2)
        self.licenseInput.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.licenseInput, 6, 1, 1, 1)

        self.authorLabel = QLabel(self.metadataWidget)
        self.authorLabel.setObjectName(u"authorLabel")
        sizePolicy4.setHeightForWidth(self.authorLabel.sizePolicy().hasHeightForWidth())
        self.authorLabel.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.authorLabel, 3, 0, 1, 1)

        self.compUrlLabel = QLabel(self.metadataWidget)
        self.compUrlLabel.setObjectName(u"compUrlLabel")
        sizePolicy4.setHeightForWidth(self.compUrlLabel.sizePolicy().hasHeightForWidth())
        self.compUrlLabel.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.compUrlLabel, 0, 0, 1, 1)

        self.thumbUrlInput = QLineEdit(self.metadataWidget)
        self.thumbUrlInput.setObjectName(u"thumbUrlInput")
        sizePolicy2.setHeightForWidth(self.thumbUrlInput.sizePolicy().hasHeightForWidth())
        self.thumbUrlInput.setSizePolicy(sizePolicy2)
        self.thumbUrlInput.setFont(font1)

        self.gridLayout.addWidget(self.thumbUrlInput, 1, 1, 1, 1)

        self.tagsLabel = QLabel(self.metadataWidget)
        self.tagsLabel.setObjectName(u"tagsLabel")
        sizePolicy4.setHeightForWidth(self.tagsLabel.sizePolicy().hasHeightForWidth())
        self.tagsLabel.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.tagsLabel, 5, 0, 1, 1)

        self.tagsWidget = TagBar(self.metadataWidget)
        self.tagsWidget.setObjectName(u"tagsWidget")
        sizePolicy2.setHeightForWidth(self.tagsWidget.sizePolicy().hasHeightForWidth())
        self.tagsWidget.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.tagsWidget, 5, 1, 1, 1)


        self.horizontalLayout_4.addWidget(self.metadataWidget)

        self.listWidget = QListWidget(self.formArea2)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)
        self.listWidget.setLineWidth(0)

        self.horizontalLayout_4.addWidget(self.listWidget)


        self.verticalLayout_2.addWidget(self.formArea2)

        self.bottomWidget = QWidget(componentCreationForm)
        self.bottomWidget.setObjectName(u"bottomWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.bottomWidget.sizePolicy().hasHeightForWidth())
        self.bottomWidget.setSizePolicy(sizePolicy5)
        self.horizontalLayout = QHBoxLayout(self.bottomWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.bottomWidget)


        self.retranslateUi(componentCreationForm)

        QMetaObject.connectSlotsByName(componentCreationForm)
    # setupUi

    def retranslateUi(self, componentCreationForm):
        componentCreationForm.setWindowTitle(QCoreApplication.translate("componentCreationForm", u"Component creation", None))
        self.componentNameLabel.setText(QCoreApplication.translate("componentCreationForm", u"<html><head/><body><p><span style=\" font-size:18pt;\">Component Name</span></p></body></html>", None))
        self.componentNameInput.setInputMask("")
        self.componentNameInput.setPlaceholderText(QCoreApplication.translate("componentCreationForm", u"name of the component", None))
        self.descriptionLabel.setText(QCoreApplication.translate("componentCreationForm", u"<html><head/><body><p><span style=\" font-size:14pt;\">Description</span></p></body></html>", None))
        self.descriptionInput.setPlaceholderText(QCoreApplication.translate("componentCreationForm", u"a short description about the component", None))
        self.thumbUrlLabel.setText(QCoreApplication.translate("componentCreationForm", u"<html><head/><body><p><span style=\" font-size:12pt;\">Thumbnail</span></p></body></html>", None))
        self.licenseLabel.setText(QCoreApplication.translate("componentCreationForm", u"<html><head/><body><p><span style=\" font-size:12pt;\">License:</span></p></body></html>", None))
        self.authorInput.setPlaceholderText(QCoreApplication.translate("componentCreationForm", u"author@email.com", None))
        self.maintainerInput.setPlaceholderText(QCoreApplication.translate("componentCreationForm", u"maintailer@email.com", None))
        self.compUrlInput.setPlaceholderText(QCoreApplication.translate("componentCreationForm", u"compoent url", None))
        self.mainteinerLabel.setText(QCoreApplication.translate("componentCreationForm", u"<html><head/><body><p><span style=\" font-size:12pt;\">Maintainer:</span></p></body></html>", None))
        self.authorLabel.setText(QCoreApplication.translate("componentCreationForm", u"<html><head/><body><p><span style=\" font-size:12pt;\">Author:</span></p></body></html>", None))
        self.compUrlLabel.setText(QCoreApplication.translate("componentCreationForm", u"<html><head/><body><p><span style=\" font-size:12pt;\">Component</span></p></body></html>", None))
        self.thumbUrlInput.setPlaceholderText(QCoreApplication.translate("componentCreationForm", u"thumbnail url", None))
        self.tagsLabel.setText(QCoreApplication.translate("componentCreationForm", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tags</span></p></body></html>", None))
    # retranslateUi

