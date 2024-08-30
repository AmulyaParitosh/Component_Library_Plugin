from PySide2.QtWidgets import (
    QWidget,
)
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import Qt, QUrl

from ....data.datadef import User
from .Ui_user_widget import Ui_UserWidget
from ....manager.download_manager import ImageLoader


class UserWidget(QWidget):
    def __init__(self, parent: QWidget, user: User) -> None:
        super().__init__(parent)
        self.user = user
        self.parent = parent

        self.ui = Ui_UserWidget()
        self.ui.setupUi(self)
        self.ui.authPushButtom.setText("Logout")
        self.ui.authPushButtom.clicked.connect(self.logout)

        self.ui.usernameLabel.setText(user.username)
        self.ui.displayNameLabel.setText(user.name)
        self.ui.emailLabel.setText(user.email)

        self.image_loader = ImageLoader()
        self.image_loader.finished.connect(self.loadImage)
        self.image_loader.start_download(QUrl.fromUserInput(self.user.avatar_url))

    def loadImage(self, image: QImage):
        self.ui.profilePhotoLabel.setPixmap(
            QPixmap(image).scaled(
                self.ui.profilePhotoLabel.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )

    def logout(self):
        self.parent.auth_manager.logout()
        self.parent.display_grid_view()
        self.parent.user_updated()
        self.close()
