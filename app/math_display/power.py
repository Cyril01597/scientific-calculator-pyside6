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
            metrics.horizontalAdvance(str(element)),
            metrics.height()
        )

    def _draw_element(self, painter, element, x, y, font):
        if isinstance(element, MathElement):
            element.draw(painter, x, y)
            return

        painter.setFont(font)

        metrics = QFontMetrics(font)

        painter.drawText(
            int(x),
            int(y + metrics.ascent()),
            str(element)
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

        height = max(
            base_size.height(),
            exponent_size.height()
            + base_size.height() // 2
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

        base_y = (
            y
            + exponent_size.height() // 2
        )

        self._draw_element(
            painter,
            self.base,
            x,
            base_y,
            self.base_font
        )

        exponent_x = (
            x
            + base_size.width()
        )

        self._draw_element(
            painter,
            self.exponent,
            exponent_x,
            y,
            self.exponent_font
        )