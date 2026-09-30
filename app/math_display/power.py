from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QFontMetrics, QPainter

from .base import MathElement


class Power(MathElement):
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

        self.base_font = QFont("Cambria Math", 28)
        self.exponent_font = QFont("Cambria Math", 18)

    def _size_of(self, element, font):
        if isinstance(element, MathElement):
            return element.size()

        metrics = QFontMetrics(font)

        return QSize(
            metrics.horizontalAdvance(element),
            metrics.height()
        )

    def size(self):
        base_size = self._size_of(
            self.base,
            self.base_font
        )

        exponent_size = self._size_of(
            self.exponent,
            self.exponent_font
        )

        width = (
            base_size.width()
            + exponent_size.width()
        )

        height = (
            base_size.height()
            + exponent_size.height() // 2
        )

        return QSize(width, height)

    def draw(self, painter, x, y):
        base_size = self._size_of(
            self.base,
            self.base_font
        )

        exponent_size = self._size_of(
            self.exponent,
            self.exponent_font
        )

        painter.setFont(self.base_font)

        base_y = y + exponent_size.height() // 2

        if isinstance(self.base, MathElement):
            self.base.draw(
                painter,
                x,
                base_y
            )
        else:
            metrics = QFontMetrics(self.base_font)

            painter.drawText(
                int(x),
                int(base_y + metrics.ascent()),
                self.base
            )

        exponent_x = (
            x
            + base_size.width()
        )

        exponent_y = y

        if isinstance(self.exponent, MathElement):
            self.exponent.draw(
                painter,
                exponent_x,
                exponent_y
            )
        else:
            painter.setFont(self.exponent_font)

            metrics = QFontMetrics(
                self.exponent_font
            )

            painter.drawText(
                int(exponent_x),
                int(exponent_y + metrics.ascent()),
                self.exponent
            )