from pathlib import Path

from PySide6.QtCore import QFile, QIODevice, QObject, QUrl, Signal, Slot
from PySide6.QtGui import QImage
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

from ...network.network_manager import get_network_access_manager


class FileDownloader(QObject):
    # A class for downloading files from the network.

    finished = Signal(Path)  # Signal emitted when the download is finished.
    error = Signal(QNetworkReply.NetworkError)  # Signal emitted when there's an error during download.

    network_access_manager, sslConfig = get_network_access_manager()

    def __init__(self, url: str, save_path: Path, filename: str) -> None:
        super().__init__()

        # Store the URL, save_path, and filename for the file to be downloaded
        self.url = QUrl(url)
        save_path.mkdir(exist_ok=True)
        self.filename: str = filename
        self.filepath = save_path / self.filename

        # Create a network request to download the file
        request = QNetworkRequest(self.url)
        self.reply: QNetworkReply = self.network_access_manager.get(request)
        self.reply.finished.connect(lambda: self.__downloaded(self.reply))
        self.downloadProgress = self.reply.downloadProgress

    @Slot(QNetworkReply)
    def __downloaded(self, reply: QNetworkReply):
        """Slot to handle the download completion and saving the downloaded file."""

        if reply.error() != QNetworkReply.NetworkError.NoError:
            # If there was an error during the download, emit the error signal with the error code
            print(f"Error: {reply.error()}")
            self.error.emit(reply.error())

        file = QFile(self.filepath)

        if file.open(QIODevice.OpenModeFlag.WriteOnly):
            # Write the downloaded data to the file
            file.write(reply.readAll())

        file.close()

        # Emit the finished signal with the path of the downloaded file
        self.finished.emit(self.filepath)

        # Clean up resources
        reply.deleteLater()
        self.deleteLater()


class ImageLoader(QObject):
    # A class for loading images from the network.

    LOADING_THUMBNAIL_PATH = "src/interface/resources/loading.jpeg"
    DEFAULT_THUMBNAIL_PATH = "src/interface/resources/default.png"

    finished = Signal(QImage)  # Signal emitted when the image is loaded.

    network_access_manager, sslConfig = get_network_access_manager()

    def __init__(self, parent=None):
        super().__init__(parent)

    def start_download(self, url: QUrl):
        """Method to start downloading the image from the given URL."""

        # Create a network request to download the image
        reply: QNetworkReply = self.network_access_manager.get(QNetworkRequest(url))
        reply.finished.connect(lambda: self.handle_finished(reply))

    def handle_finished(self, reply: QNetworkReply):
        """Method to handle the finished download and emit the loaded image."""

        # Load the image from the network reply and emit the finished signal with the loaded image
        image = self.load_image_from_reply(reply)

        if image.isNull():
            # If the image loading failed, print an error message and return
            print("Error: Unable to load image from the reply.")
            return

        self.finished.emit(image)

        # Clean up resources
        reply.deleteLater()

    def load_image_from_reply(self, reply: QNetworkReply) -> QImage:
        """Method to load an image from the network reply."""
        image = QImage()

        if reply.error() == QNetworkReply.NetworkError.ProtocolUnknownError:
            # If the network protocol is unknown, load a default thumbnail image
            default_thumbnail_file = QFile(self.DEFAULT_THUMBNAIL_PATH)

            if default_thumbnail_file.open(QIODevice.OpenModeFlag.ReadOnly):
                content = default_thumbnail_file.readAll()
                default_thumbnail_file.close()
                image.loadFromData(content)

        elif reply.error() == QNetworkReply.NetworkError.NoError:
            # Load the image from the reply data if there was no error
            image.loadFromData(reply.readAll())

        return image
