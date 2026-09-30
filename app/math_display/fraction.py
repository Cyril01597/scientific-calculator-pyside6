from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QFontMetrics, QPainter

from .base import MathElement


class Fraction(MathElement):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        self.font = QFont("Cambria Math", 28)

    def _text_size(self, text):
        metrics = QFontMetrics(self.font)

        return QSize(
            metrics.horizontalAdvance(str(text)),
            metrics.height()
        )

    def _size_of(self, element):
        if isinstance(element, MathElement):
            return element.size()

        return self._text_size(element)

    def size(self):
        numerator_size = self._size_of(self.numerator)
        denominator_size = self._size_of(self.denominator)

        width = max(
            numerator_size.width(),
            denominator_size.width()
        ) + 20

        height = (
            numerator_size.height()
            + denominator_size.height()
            + 10
        )

        return QSize(width, height)

    def _draw_element(self, painter, element, x, y):
        if isinstance(element, MathElement):
            element.draw(painter, x, y)
            return

        painter.setFont(self.font)

        metrics = QFontMetrics(self.font)

        painter.drawText(
            int(x),
            int(y + metrics.ascent()),
            str(element)
        )

    def draw(self, painter, x, y):
        numerator_size = self._size_of(self.numerator)
        denominator_size = self._size_of(self.denominator)

        width = max(
            numerator_size.width(),
            denominator_size.width()
        ) + 20

        center_x = x + width / 2

        numerator_x = (
            center_x
            - numerator_size.width() / 2
        )

        denominator_x = (
            center_x
            - denominator_size.width() / 2
        )

        self._draw_element(
            painter,
            self.numerator,
            numerator_x,
            y
        )

        line_y = (
            y
            + numerator_size.height()
            + 5
        )

        painter.drawLine(
            int(x),
            int(line_y),
            int(x + width),
            int(line_y)
        )

        self._draw_element(
            painter,
            self.denominator,
            denominator_x,
            line_y + 5
        )