from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QFontMetrics, QPainter

from .base import MathElement


class Parentheses(MathElement):
    def __init__(self, expression):
        self.expression = expression

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
        expression_size = self._size_of(
            self.expression
        )

        metrics = QFontMetrics(
            self.font
        )

        parenthesis_width = (
            metrics.horizontalAdvance("(")
            + metrics.horizontalAdvance(")")
        )

        return QSize(
            expression_size.width()
            + parenthesis_width,
            expression_size.height()
        )

    def draw(self, painter, x, y):
        painter.setFont(
            self.font
        )

        metrics = QFontMetrics(
            self.font
        )

        expression_size = self._size_of(
            self.expression
        )

        left_width = metrics.horizontalAdvance(
            "("
        )

        painter.drawText(
            int(x),
            int(y + metrics.ascent()),
            "("
        )

        expression_x = (
            x
            + left_width
        )

        if isinstance(
            self.expression,
            MathElement
        ):
            self.expression.draw(
                painter,
                expression_x,
                y
            )
        else:
            painter.drawText(
                int(expression_x),
                int(y + metrics.ascent()),
                str(self.expression)
            )

        right_x = (
            expression_x
            + expression_size.width()
        )

        painter.drawText(
            int(right_x),
            int(y + metrics.ascent()),
            ")"
        )