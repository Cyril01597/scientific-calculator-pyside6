from abc import ABC, abstractmethod
from PySide6.QtCore import QSize
from PySide6.QtGui import QPainter


class MathElement(ABC):

    @abstractmethod
    def size(self) -> QSize:
        pass

    @abstractmethod
    def draw(self, painter: QPainter, x: float, y: float):
        pass