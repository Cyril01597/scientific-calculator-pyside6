from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QFont
from PySide6.QtWidgets import QWidget, QSizePolicy

from .base import MathElement


class MathDisplay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.expression = "0"

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

        painter.setRenderHint(
            QPainter.Antialiasing
        )

        if isinstance(self.expression, MathElement):

            expression_size = self.expression.size()

            x = (
                self.width()
                - expression_size.width()
            ) / 2

            y = (
                self.height()
                - expression_size.height()
            ) / 2

            self.expression.draw(
                painter,
                x,
                y
            )

        else:
            font = QFont(
                "Cambria Math",
                28
            )

            painter.setFont(font)

            painter.drawText(
                self.rect(),
                Qt.AlignCenter,
                str(self.expression)
            )

        painter.end()