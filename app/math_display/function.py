from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QFontMetrics, QPainter

from .base import MathElement


class Function(MathElement):
    def __init__(self, name, argument):
        self.name = name
        self.argument = argument

        self.font = QFont("Cambria Math", 28)

    def _size_of(self, element):
        if isinstance(element, MathElement):
            return element.size()

        metrics = QFontMetrics(self.font)

        return QSize(
            metrics.horizontalAdvance(str(element)),
            metrics.height()
        )

    def size(self):
        argument_size = self._size_of(
            self.argument
        )

        metrics = QFontMetrics(
            self.font
        )

        name_width = metrics.horizontalAdvance(
            self.name
        )

        parenthesis_width = (
            metrics.horizontalAdvance("(")
            + metrics.horizontalAdvance(")")
        )

        width = (
            name_width
            + parenthesis_width
            + argument_size.width()
        )

        height = max(
            argument_size.height(),
            metrics.height()
        )

        return QSize(
            width,
            height
        )

    def draw(self, painter, x, y):
        painter.setFont(
            self.font
        )

        metrics = QFontMetrics(
            self.font
        )

        argument_size = self._size_of(
            self.argument
        )

        name_width = metrics.horizontalAdvance(
            self.name
        )

        left_parenthesis_width = (
            metrics.horizontalAdvance("(")
        )

        # Function name
        painter.drawText(
            int(x),
            int(y + metrics.ascent()),
            self.name
        )

        # Left parenthesis
        left_x = (
            x
            + name_width
        )

        painter.drawText(
            int(left_x),
            int(y + metrics.ascent()),
            "("
        )

        # Argument
        argument_x = (
            left_x
            + left_parenthesis_width
        )

        argument_y = y

        if isinstance(
            self.argument,
            MathElement
        ):
            self.argument.draw(
                painter,
                argument_x,
                argument_y
            )
        else:
            painter.drawText(
                int(argument_x),
                int(y + metrics.ascent()),
                str(self.argument)
            )

        # Right parenthesis
        right_x = (
            argument_x
            + argument_size.width()
        )

        painter.drawText(
            int(right_x),
            int(y + metrics.ascent()),
            ")"
        )