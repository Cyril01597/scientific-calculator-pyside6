from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QFontMetrics, QPainter

from .base import MathElement


class Vector(MathElement):
    def __init__(self, elements):
        self.elements = elements

        self.font = QFont(
            "Cambria Math",
            26
        )

        self.padding = 10
        self.row_spacing = 6

    def _size_of(self, element):
        if isinstance(element, MathElement):
            return element.size()

        metrics = QFontMetrics(self.font)

        return QSize(
            metrics.horizontalAdvance(str(element)),
            metrics.height()
        )

    def size(self):
        if not self.elements:
            return QSize(0, 0)

        widths = [
            self._size_of(element).width()
            for element in self.elements
        ]

        heights = [
            self._size_of(element).height()
            for element in self.elements
        ]

        width = (
            max(widths)
            + self.padding * 2
            + 16
        )

        height = (
            sum(heights)
            + self.row_spacing
            * max(0, len(heights) - 1)
            + self.padding * 2
        )

        return QSize(
            width,
            height
        )

    def draw(self, painter, x, y):
        if not self.elements:
            return

        element_sizes = [
            self._size_of(element)
            for element in self.elements
        ]

        content_width = max(
            size.width()
            for size in element_sizes
        )

        current_y = (
            y
            + self.padding
        )

        painter.setFont(self.font)

        metrics = QFontMetrics(
            self.font
        )

        # Left bracket
        painter.drawText(
            int(x),
            int(
                current_y
                + metrics.ascent()
            ),
            "["
        )

        for element, element_size in zip(
            self.elements,
            element_sizes
        ):
            element_x = (
                x
                + self.padding
                + 6
                + (
                    content_width
                    - element_size.width()
                ) / 2
            )

            if isinstance(
                element,
                MathElement
            ):
                element.draw(
                    painter,
                    element_x,
                    current_y
                )
            else:
                painter.drawText(
                    int(element_x),
                    int(
                        current_y
                        + metrics.ascent()
                    ),
                    str(element)
                )

            current_y += (
                element_size.height()
                + self.row_spacing
            )

        # Right bracket
        right_x = (
            x
            + self.padding
            + content_width
            + 10
        )

        painter.drawText(
            int(right_x),
            int(
                y
                + self.padding
                + metrics.ascent()
            ),
            "]"
        )