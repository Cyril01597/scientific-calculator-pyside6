from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QFontMetrics, QPainter

from .base import MathElement


class Root(MathElement):
    def __init__(self, radicand, index=2):
        self.radicand = radicand
        self.index = index

        self.font = QFont("Cambria Math", 28)
        self.index_font = QFont("Cambria Math", 16)

    def _size_of(self, element, font):
        if isinstance(element, MathElement):
            return element.size()

        metrics = QFontMetrics(font)

        return QSize(
            metrics.horizontalAdvance(str(element)),
            metrics.height()
        )

    def size(self):
        radicand_size = self._size_of(
            self.radicand,
            self.font
        )

        index_size = self._size_of(
            self.index,
            self.index_font
        )

        width = (
            index_size.width()
            + 10
            + radicand_size.width()
            + 10
        )

        height = max(
            radicand_size.height(),
            index_size.height() + 5
        ) + 10

        return QSize(width, height)

    def _draw_radicand(self, painter, x, y):
        if isinstance(self.radicand, MathElement):
            self.radicand.draw(
                painter,
                x,
                y
            )
            return

        painter.setFont(self.font)

        metrics = QFontMetrics(self.font)

        painter.drawText(
            int(x),
            int(y + metrics.ascent()),
            str(self.radicand)
        )

    def draw(self, painter, x, y):
        radicand_size = self._size_of(
            self.radicand,
            self.font
        )

        index_size = self._size_of(
            self.index,
            self.index_font
        )

        radicand_x = (
            x
            + index_size.width()
            + 10
        )

        radicand_y = y + 5

        self._draw_radicand(
            painter,
            radicand_x,
            radicand_y
        )

        # Radical symbol
        painter.setFont(self.font)

        metrics = QFontMetrics(self.font)

        symbol_x = x

        symbol_y = (
            radicand_y
            + metrics.ascent()
        )

        painter.drawText(
            int(symbol_x),
            int(symbol_y),
            "√"
        )

        # Radical bar
        bar_x = radicand_x - 2

        bar_y = radicand_y + 2

        painter.drawLine(
            int(bar_x),
            int(bar_y),
            int(
                radicand_x
                + radicand_size.width()
            ),
            int(bar_y)
        )

        # Index
        if self.index != 2:
            painter.setFont(self.index_font)

            index_metrics = QFontMetrics(
                self.index_font
            )

            painter.drawText(
                int(x),
                int(
                    y
                    + index_metrics.ascent()
                ),
                str(self.index)
            )