import sys

from PySide6.QtWidgets import QApplication, QScrollArea
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt

from app.math_display.display import MathDisplay
from app.math_display.fraction import Fraction
from app.math_display.power import Power
from app.math_display.root import Root
from app.math_display.summation import Summation
from app.math_display.limit import Limit
from app.math_display.function import Function
from app.math_display.parentheses import Parentheses
from app.math_display.binary_operation import BinaryOperation


def main():
    app = QApplication(sys.argv)

    ui_file = QFile("ui/calculator.ui")
    ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)

    ui_file.close()

    if window is None:
        print("Failed to load calculator.ui")
        sys.exit(1)

    scroll_area = window.findChild(
        QScrollArea,
        "expressionScrollArea"
    )

    if scroll_area is None:
        print("Could not find expressionScrollArea")
        sys.exit(1)

    scroll_area.setWidgetResizable(True)

    scroll_area.setAlignment(
        Qt.AlignCenter
    )

    scroll_area.setHorizontalScrollBarPolicy(
        Qt.ScrollBarAlwaysOff
    )

    scroll_area.setVerticalScrollBarPolicy(
        Qt.ScrollBarAlwaysOff
    )

    math_display = MathDisplay()

    scroll_area.setWidget(
        math_display
    )

    # Test expression
    math_display.set_expression(
    Fraction(
        BinaryOperation(
            Power("x", "2"),
            "+",
            "1"
        ),
        Root(
            BinaryOperation(
                "x",
                "+",
                "1"
            )
        )
    )
)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()