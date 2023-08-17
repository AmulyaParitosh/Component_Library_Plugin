
# SPDX-License-Identifier: MIT
# --------------------------------------------------------------
#|																|
#|             Copyright 2023 - 2023, Amulya Paritosh			|
#|																|
#|  This file is part of Component Library Plugin for FreeCAD.	|
#|																|
#|               This file was created as a part of				|
#|              Google Summer Of Code Program - 2023			|
#|																|
# --------------------------------------------------------------

from __future__ import annotations

from PySide6.QtCore import QUrl
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel, QWidget

from ....manager.download_manager import ImageLoader


class Thumbnail(QLabel):
    # Custom QLabel class for displaying image thumbnails.

    def __init__(self, parent: QWidget, url: str | None = None) -> None:
        # Constructor to initialize the Thumbnail.

        super().__init__(parent)

        # Set the scaled contents property to ensure the image is scaled to fit the label.
        self.setScaledContents(True)

        # Set the pixmap to a loading thumbnail image.
        self.setPixmap(QPixmap(ImageLoader.LOADING_THUMBNAIL_PATH))

        # Create an ImageLoader to handle image downloads.
        self.downloader = ImageLoader()
        self.downloader.finished.connect(self.loadImage)

        # If a URL is provided during initialization, setup the thumbnail with the image from the URL.
        if url:
            self.setupThumbnail(url)

    def setupThumbnail(self, url_str: str):
        # Method to start downloading the image from the provided URL.

        self.downloader.start_download(QUrl.fromUserInput(url_str))

    def loadImage(self, image: QImage):
        # Method to display the downloaded image as the thumbnail.

        pixmap = QPixmap(image)
        self.setPixmap(pixmap)

    @staticmethod
    def from_existing(parent, thumbnail: Thumbnail):
        # Static method to create a new Thumbnail from an existing Thumbnail's pixmap.

        new_thumbnail = Thumbnail(parent)
        new_thumbnail.setPixmap(thumbnail.pixmap())
        return new_thumbnail
