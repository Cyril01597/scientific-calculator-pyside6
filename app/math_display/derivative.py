from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QFontMetrics, QPainter

from .base import MathElement


class Derivative(MathElement):
    def __init__(self, expression, variable="x", order=1):
        self.expression = expression
        self.variable = variable
        self.order = order

        self.font = QFont("Cambria Math", 28)
        self.small_font = QFont("Cambria Math", 18)

    def _size_of(self, element):
        if isinstance(element, MathElement):
            return element.size()

        metrics = QFontMetrics(self.font)

        return QSize(
            metrics.horizontalAdvance(str(element)),
            metrics.height()
        )

    def size(self):
        expression_size = self._size_of(
            self.expression
        )

        metrics = QFontMetrics(
            self.small_font
        )

        if self.order == 1:
            numerator = "d"
            denominator = f"d{self.variable}"
        else:
            numerator = f"d{self.order}"
            denominator = f"d{self.variable}{self.order}"

        numerator_width = metrics.horizontalAdvance(
            numerator
        )

        denominator_width = metrics.horizontalAdvance(
            denominator
        )

        fraction_width = max(
            numerator_width,
            denominator_width
        ) + 8

        width = (
            fraction_width
            + 8
            + expression_size.width()
        )

        height = (
            metrics.height() * 2
            + 8
        )

        return QSize(
            width,
            max(
                height,
                expression_size.height()
            )
        )

    def draw(self, painter, x, y):
        expression_size = self._size_of(
            self.expression
        )

        painter.setFont(
            self.small_font
        )

        metrics = QFontMetrics(
            self.small_font
        )

        if self.order == 1:
            numerator = "d"
            denominator = f"d{self.variable}"
        else:
            numerator = f"d{self.order}"
            denominator = f"d{self.variable}{self.order}"

        numerator_width = metrics.horizontalAdvance(
            numerator
        )

        denominator_width = metrics.horizontalAdvance(
            denominator
        )

        fraction_width = max(
            numerator_width,
            denominator_width
        ) + 8

        # Numerator
        numerator_x = (
            x
            + (
                fraction_width
                - numerator_width
            ) / 2
        )

        painter.drawText(
            int(numerator_x),
            int(y + metrics.ascent()),
            numerator
        )

        # Fraction line
        line_y = (
            y
            + metrics.height()
            + 2
        )

        painter.drawLine(
            int(x),
            int(line_y),
            int(x + fraction_width),
            int(line_y)
        )

        # Denominator
        denominator_x = (
            x
            + (
                fraction_width
                - denominator_width
            ) / 2
        )

        painter.drawText(
            int(denominator_x),
            int(
                line_y
                + metrics.height()
            ),
            denominator
        )

        # Expression
        expression_x = (
            x
            + fraction_width
            + 8
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
                self.font
            )

            expression_metrics = QFontMetrics(
                self.font
            )

            painter.drawText(
                int(expression_x),
                int(
                    expression_y
                    + expression_metrics.ascent()
                ),
                str(self.expression)
            )