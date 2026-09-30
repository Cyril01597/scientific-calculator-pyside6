from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QFont
from PySide6.QtWidgets import QWidget, QSizePolicy


class MathDisplay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.expression = "x + 1"

        self.setMinimumSize(0, 180)

        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

    def set_expression(self, expression):
        self.expression = expression
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        font = QFont("Cambria Math", 28)
        painter.setFont(font)

        painter.drawText(
            self.rect(),
            Qt.AlignCenter,
            self.expression
        )

        painter.end()