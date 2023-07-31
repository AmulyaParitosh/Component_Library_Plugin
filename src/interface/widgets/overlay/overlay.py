from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QPainter
from PySide6.QtWidgets import QGraphicsBlurEffect, QWidget


class Overlay(QWidget):
	overlay_text: str = ""

	def paintEvent(self, event):
		popup_width, popup_height = 300, 120
		ow = int(self.size().width()/2-popup_width/2)
		oh = int(self.size().height()/2-popup_height/2)

		tolw, tolh = 80, -5

		qp = self.create_painter()
		qp.drawText(
			ow + popup_width // 2 - tolw,
			oh + popup_height // 2 - tolh,
			self.overlay_text,
		)

		qp.end()

	def create_painter(self):
		font = QFont()
		font.setPixelSize(20)
		font.setItalic(True)

		qp = QPainter()
		qp.begin(self)

		qp.setRenderHint(QPainter.RenderHint.Antialiasing, True)
		qp.setFont(font)
		qp.setPen(Qt.GlobalColor.white)
		return qp

	def show(self):
		self.move(0, 0)
		self.resize(self.parent().size()) # type: ignore
		self.blur_effect = QGraphicsBlurEffect()
		self.blur_effect.setBlurRadius(30)
		self.parent().widget().setGraphicsEffect(self.blur_effect) # type: ignore

		return super().show()

	def hide(self) -> None:
		self.parent().widget().setGraphicsEffect(None) # type: ignore
		return super().hide()
