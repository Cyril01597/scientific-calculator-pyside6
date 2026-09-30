from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QFontMetrics, QPainter


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        self.font = QFont("Cambria Math", 28)

    def size(self):
        metrics = QFontMetrics(self.font)

        numerator_width = metrics.horizontalAdvance(self.numerator)
        denominator_width = metrics.horizontalAdvance(self.denominator)

        width = max(numerator_width, denominator_width) + 20
        height = metrics.height() * 2 + 10

        return QSize(width, height)

    def draw(self, painter, x, y):
        painter.setFont(self.font)

        metrics = QFontMetrics(self.font)

        numerator_width = metrics.horizontalAdvance(self.numerator)
        denominator_width = metrics.horizontalAdvance(self.denominator)

        width = max(numerator_width, denominator_width) + 20

        center_x = x + width / 2

        numerator_x = center_x - numerator_width / 2
        denominator_x = center_x - denominator_width / 2

        baseline = y + metrics.ascent()

        painter.drawText(
            int(numerator_x),
            int(baseline),
            self.numerator
        )

        line_y = y + metrics.height()

        painter.drawLine(
            int(x),
            int(line_y),
            int(x + width),
            int(line_y)
        )

        painter.drawText(
            int(denominator_x),
            int(line_y + metrics.height()),
            self.denominator
        )