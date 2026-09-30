from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QFontMetrics, QPainter

from .base import MathElement


class BinaryOperation(MathElement):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

        self.font = QFont(
            "Cambria Math",
            28
        )

    def _size_of(self, element):
        if isinstance(element, MathElement):
            return element.size()

        metrics = QFontMetrics(
            self.font
        )

        return QSize(
            metrics.horizontalAdvance(str(element)),
            metrics.height()
        )

    def size(self):
        left_size = self._size_of(
            self.left
        )

        right_size = self._size_of(
            self.right
        )

        metrics = QFontMetrics(
            self.font
        )

        operator_width = metrics.horizontalAdvance(
            self.operator
        )

        spacing = 12

        width = (
            left_size.width()
            + spacing
            + operator_width
            + spacing
            + right_size.width()
        )

        height = max(
            left_size.height(),
            right_size.height(),
            metrics.height()
        )

        return QSize(
            width,
            height
        )

    def _draw_element(
        self,
        painter,
        element,
        x,
        y
    ):
        if isinstance(
            element,
            MathElement
        ):
            element.draw(
                painter,
                x,
                y
            )
            return

        painter.setFont(
            self.font
        )

        metrics = QFontMetrics(
            self.font
        )

        painter.drawText(
            int(x),
            int(y + metrics.ascent()),
            str(element)
        )

    def draw(self, painter, x, y):
        left_size = self._size_of(
            self.left
        )

        metrics = QFontMetrics(
            self.font
        )

        spacing = 12

        # Left expression
        self._draw_element(
            painter,
            self.left,
            x,
            y
        )

        # Operator
        operator_x = (
            x
            + left_size.width()
            + spacing
        )

        painter.setFont(
            self.font
        )

        painter.drawText(
            int(operator_x),
            int(y + metrics.ascent()),
            self.operator
        )

        # Right expression
        operator_width = metrics.horizontalAdvance(
            self.operator
        )

        right_x = (
            operator_x
            + operator_width
            + spacing
        )

        self._draw_element(
            painter,
            self.right,
            right_x,
            y
        )