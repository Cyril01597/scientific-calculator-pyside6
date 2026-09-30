import sys

from PySide6.QtWidgets import QApplication, QWidget, QScrollArea
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt

from app.math_display.display import MathDisplay


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

    scroll_area = window.findChild(QScrollArea, "expressionScrollArea")
    
    if scroll_area is None:
        print("Could not find expressionScrollArea")
        sys.exit(1)

    scroll_area.setWidgetResizable(True)
    scroll_area.setAlignment(Qt.AlignCenter)
    scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    

    math_display = MathDisplay()

    scroll_area.setWidget(math_display)

    math_display.set_expression("x + 1")

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()