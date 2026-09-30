from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QFontMetrics, QPainter

from .base import MathElement


class Integral(MathElement):
    def __init__(self, lower, upper, expression, variable="x"):
        self.lower = lower
        self.upper = upper
        self.expression = expression
        self.variable = variable

        self.symbol_font = QFont("Cambria Math", 48)
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
        lower_size = self._size_of(
            self.lower,
            self.text_font
        )

        upper_size = self._size_of(
            self.upper,
            self.text_font
        )

        expression_size = self._size_of(
            self.expression,
            self.expression_font
        )

        variable_size = self._size_of(
            self.variable,
            self.text_font
        )

        symbol_width = 35
        spacing = 10

        width = (
            symbol_width
            + spacing
            + expression_size.width()
            + spacing
            + variable_size.width()
        )

        height = max(
            expression_size.height(),
            upper_size.height()
            + lower_size.height()
            + 10
        )

        return QSize(width, height)

    def draw(self, painter, x, y):
        lower_size = self._size_of(
            self.lower,
            self.text_font
        )

        upper_size = self._size_of(
            self.upper,
            self.text_font
        )

        expression_size = self._size_of(
            self.expression,
            self.expression_font
        )

        variable_size = self._size_of(
            self.variable,
            self.text_font
        )

        # Integral symbol
        painter.setFont(self.symbol_font)

        symbol_metrics = QFontMetrics(
            self.symbol_font
        )

        symbol_y = (
            y
            + expression_size.height()
        )

        painter.drawText(
            int(x),
            int(symbol_y),
            "∫"
        )

        # Upper limit
        painter.setFont(self.text_font)

        upper_x = x

        upper_y = y

        painter.drawText(
            int(upper_x),
            int(upper_y + upper_size.height()),
            str(self.upper)
        )

        # Lower limit
        lower_x = x

        lower_y = (
            y
            + expression_size.height()
            - 2
        )

        painter.drawText(
            int(lower_x),
            int(lower_y),
            str(self.lower)
        )

        # Expression
        expression_x = (
            x
            + 35
            + 10
        )

        expression_y = y

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

        # Differential
        differential_x = (
            expression_x
            + expression_size.width()
            + 10
        )

        painter.setFont(
            self.text_font
        )

        painter.drawText(
            int(differential_x),
            int(
                y
                + self.text_font.pointSize()
                + 5
            ),
            f"d{self.variable}"
        )