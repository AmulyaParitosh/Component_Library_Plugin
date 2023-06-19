from __future__ import annotations

from time import sleep
from urllib import request

from PySide6.QtCore import QRunnable, QThreadPool, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel, QWidget


class _Worker(QRunnable):

	def __init__(self, fn, *args, **kwargs) -> None:
		super().__init__()
		self.fn = fn
		self.args = args
		self.kwargs = kwargs

	@Slot()
	def run(self) -> None:
		self.fn(*self.args, **self.kwargs)


class Thumbnail(QLabel):
	def __init__(self, parent: QWidget) -> None:
		super().__init__(parent)
		self.setScaledContents(True)
		self.setPixmap(QPixmap("component_library/components/thumbnail/loading.jpeg"))
		self.threadpool = QThreadPool()

	def setupThumbnail(self, image_url: str):
		worker = _Worker(self._loadImage, image_url)
		self.threadpool.start(worker)

	def _loadImage(self, image_url: str):
		sleep(2)
		data = request.urlopen(image_url).read()
		image = QImage()
		image.loadFromData(data)
		self.setPixmap(QPixmap(image))
