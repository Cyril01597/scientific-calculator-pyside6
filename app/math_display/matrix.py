from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QFontMetrics, QPainter

from .base import MathElement


class Matrix(MathElement):
    def __init__(self, rows):
        self.rows = rows

        self.font = QFont(
            "Cambria Math",
            26
        )

        self.padding = 12
        self.row_spacing = 8
        self.column_spacing = 16

    def _size_of(self, element):
        if isinstance(element, MathElement):
            return element.size()

        metrics = QFontMetrics(self.font)

        return QSize(
            metrics.horizontalAdvance(str(element)),
            metrics.height()
        )

    def size(self):
        if not self.rows:
            return QSize(0, 0)

        column_count = max(
            len(row)
            for row in self.rows
        )

        column_widths = []

        for column in range(column_count):
            width = 0

            for row in self.rows:
                if column < len(row):
                    element_size = self._size_of(
                        row[column]
                    )

                    width = max(
                        width,
                        element_size.width()
                    )

            column_widths.append(width)

        row_heights = []

        for row in self.rows:
            height = 0

            for element in row:
                element_size = self._size_of(
                    element
                )

                height = max(
                    height,
                    element_size.height()
                )

            row_heights.append(height)

        content_width = (
            sum(column_widths)
            + self.column_spacing
            * max(0, column_count - 1)
        )

        content_height = (
            sum(row_heights)
            + self.row_spacing
            * max(0, len(row_heights) - 1)
        )

        return QSize(
            content_width
            + self.padding * 2
            + 12,
            content_height
            + self.padding * 2
        )

    def draw(self, painter, x, y):
        if not self.rows:
            return

        column_count = max(
            len(row)
            for row in self.rows
        )

        column_widths = []

        for column in range(column_count):
            width = 0

            for row in self.rows:
                if column < len(row):
                    width = max(
                        width,
                        self._size_of(
                            row[column]
                        ).width()
                    )

            column_widths.append(width)

        row_heights = []

        for row in self.rows:
            height = 0

            for element in row:
                height = max(
                    height,
                    self._size_of(element).height()
                )

            row_heights.append(height)

        content_width = (
            sum(column_widths)
            + self.column_spacing
            * max(0, column_count - 1)
        )

        content_height = (
            sum(row_heights)
            + self.row_spacing
            * max(0, len(row_heights) - 1)
        )

        # Brackets
        painter.setFont(self.font)

        metrics = QFontMetrics(self.font)

        left_x = x
        right_x = (
            x
            + self.padding
            + content_width
            + 4
        )

        top_y = (
            y
            + self.padding
        )

        bottom_y = (
            top_y
            + content_height
        )

        painter.drawText(
            int(left_x),
            int(top_y + metrics.ascent()),
            "["
        )

        painter.drawText(
            int(right_x),
            int(top_y + metrics.ascent()),
            "]"
        )

        # Matrix contents
        current_y = top_y

        for row_index, row in enumerate(self.rows):
            current_x = (
                x
                + self.padding
                + 6
            )

            row_height = row_heights[row_index]

            for column_index in range(column_count):
                if column_index >= len(row):
                    continue

                element = row[column_index]

                element_size = self._size_of(
                    element
                )

                cell_width = column_widths[
                    column_index
                ]

                element_x = (
                    current_x
                    + (
                        cell_width
                        - element_size.width()
                    ) / 2
                )

                element_y = (
                    current_y
                    + (
                        row_height
                        - element_size.height()
                    ) / 2
                )

                if isinstance(
                    element,
                    MathElement
                ):
                    element.draw(
                        painter,
                        element_x,
                        element_y
                    )
                else:
                    painter.setFont(
                        self.font
                    )

                    painter.drawText(
                        int(element_x),
                        int(
                            element_y
                            + metrics.ascent()
                        ),
                        str(element)
                    )

                current_x += (
                    cell_width
                    + self.column_spacing
                )

            current_y += (
                row_height
                + self.row_spacing
            )