from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QFontMetrics, QPainter

from .base import MathElement


class Summation(MathElement):
    def __init__(self, variable, lower, upper, expression):
        self.variable = variable
        self.lower = lower
        self.upper = upper
        self.expression = expression

        self.symbol_font = QFont("Cambria Math", 42)
        self.text_font = QFont("Cambria Math", 18)
        self.expression_font = QFont("Cambria Math", 28)

    def _size_of(self, element, font):
        if isinstance(element, MathElement):
            return element.size()

        metrics = QFontMetrics(font)

        return QSize(
            metrics.horizontalAdvance(str(element)),
            metrics.height()
        )

    def size(self):
        upper_size = self._size_of(
            self.upper,
            self.text_font
        )

        lower_size = self._size_of(
            f"{self.variable}={self.lower}",
            self.text_font
        )

        expression_size = self._size_of(
            self.expression,
            self.expression_font
        )

        symbol_width = 42
        spacing = 15

        width = (
            symbol_width
            + spacing
            + expression_size.width()
        )

        height = max(
            expression_size.height(),
            upper_size.height()
            + lower_size.height()
            + 10
        )

        return QSize(
            width,
            height
        )

    def draw(self, painter, x, y):
        upper_size = self._size_of(
            self.upper,
            self.text_font
        )

        lower_text = (
            f"{self.variable}={self.lower}"
        )

        lower_size = self._size_of(
            lower_text,
            self.text_font
        )

        expression_size = self._size_of(
            self.expression,
            self.expression_font
        )

        # Summation symbol
        painter.setFont(self.symbol_font)

        symbol_metrics = QFontMetrics(
            self.symbol_font
        )

        symbol_x = x

        symbol_y = (
            y
            + expression_size.height() / 2
            + symbol_metrics.ascent() / 2
        )

        painter.drawText(
            int(symbol_x),
            int(symbol_y),
            "∑"
        )

        # Upper limit
        painter.setFont(self.text_font)

        upper_x = (
            x
            + 10
        )

        upper_y = y

        painter.drawText(
            int(upper_x),
            int(upper_y + upper_size.height()),
            str(self.upper)
        )

        # Lower limit
        lower_x = x + 2

        lower_y = (
            y
            + expression_size.height()
            - 2
        )

        painter.drawText(
            int(lower_x),
            int(lower_y),
            lower_text
        )

        # Expression
        expression_x = (
            x
            + 42
            + 15
        )

        expression_y = (
            y
            + max(
                0,
                (
                    expression_size.height()
                    - expression_size.height()
                ) / 2
            )
        )

        if isinstance(
            self.expression,
            MathElement
        ):
            self.expression.draw(
                painter,
                expression_x,
                expression_y
            )
        else:
            painter.setFont(
                self.expression_font
            )

            metrics = QFontMetrics(
                self.expression_font
            )

            painter.drawText(
                int(expression_x),
                int(
                    expression_y
                    + metrics.ascent()
                ),
                str(self.expression)
            )