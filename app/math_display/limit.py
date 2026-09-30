from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QFontMetrics, QPainter

from .base import MathElement


class Limit(MathElement):
    def __init__(self, variable, approach, expression):
        self.variable = variable
        self.approach = approach
        self.expression = expression

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
        limit_text = (
            f"{self.variable} → {self.approach}"
        )

        limit_size = self._size_of(
            limit_text,
            self.text_font
        )

        expression_size = self._size_of(
            self.expression,
            self.expression_font
        )

        width = max(
            limit_size.width(),
            expression_size.width()
        )

        height = (
            limit_size.height()
            + expression_size.height()
            + 5
        )

        return QSize(
            width,
            height
        )

    def draw(self, painter, x, y):
        limit_text = (
            f"{self.variable} → {self.approach}"
        )

        limit_size = self._size_of(
            limit_text,
            self.text_font
        )

        expression_size = self._size_of(
            self.expression,
            self.expression_font
        )

        total_width = max(
            limit_size.width(),
            expression_size.width()
        )

        # "lim"
        painter.setFont(
            self.text_font
        )

        lim_metrics = QFontMetrics(
            self.text_font
        )

        lim_x = (
            x
            + (
                total_width
                - limit_size.width()
            ) / 2
        )

        painter.drawText(
            int(lim_x),
            int(
                y
                + lim_metrics.ascent()
            ),
            "lim"
        )

        # Variable → value
        variable_x = (
            x
            + (
                total_width
                - limit_size.width()
            ) / 2
        )

        variable_y = (
            y
            + limit_size.height()
        )

        painter.drawText(
            int(variable_x),
            int(variable_y),
            limit_text
        )

        # Expression
        expression_x = (
            x
            + (
                total_width
                - expression_size.width()
            ) / 2
        )

        expression_y = (
            y
            + limit_size.height()
            + 5
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