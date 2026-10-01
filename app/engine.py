import math

from app.expression.number import Number
from app.expression.binary import BinaryOperation
from app.expression.unary import UnaryOperation


class CalculatorEngine:

    def __init__(self):
        self.current_expression = ""
        self.result = None
        self.angle_mode = "DEG"

    def evaluate(self, expression):
        try:
            return expression.evaluate()

        except ZeroDivisionError:
            return "Error: Division by zero"

        except ValueError as error:
            return f"Error: {error}"

        except Exception as error:
            return f"Error: {error}"

    def input(self, value):
        self.current_expression += str(value)

        return self.current_expression

    def clear(self):
        self.current_expression = ""
        self.result = None

        return self.current_expression

    def backspace(self):
        self.current_expression = (
            self.current_expression[:-1]
        )

        return self.current_expression

    def add(self, left, right):
        expression = BinaryOperation(
            Number(left),
            "+",
            Number(right)
        )

        return self.evaluate(expression)

    def subtract(self, left, right):
        expression = BinaryOperation(
            Number(left),
            "-",
            Number(right)
        )

        return self.evaluate(expression)

    def multiply(self, left, right):
        expression = BinaryOperation(
            Number(left),
            "*",
            Number(right)
        )

        return self.evaluate(expression)

    def divide(self, left, right):
        expression = BinaryOperation(
            Number(left),
            "/",
            Number(right)
        )

        return self.evaluate(expression)

    def power(self, base, exponent):
        expression = BinaryOperation(
            Number(base),
            "^",
            Number(exponent)
        )

        return self.evaluate(expression)

    def sqrt(self, value):
        expression = UnaryOperation(
            "sqrt",
            Number(value)
        )

        return self.evaluate(expression)

    def convert_angle(self, value):
        if self.angle_mode == "DEG":
            return math.radians(value)

        if self.angle_mode == "GRAD":
            return value * math.pi / 200

        return value

    def sin(self, value):
        expression = UnaryOperation(
            "sin",
            Number(
                self.convert_angle(value)
            )
        )

        return self.evaluate(expression)

    def cos(self, value):
        expression = UnaryOperation(
            "cos",
            Number(
                self.convert_angle(value)
            )
        )

        return self.evaluate(expression)

    def tan(self, value):
        expression = UnaryOperation(
            "tan",
            Number(
                self.convert_angle(value)
            )
        )

        return self.evaluate(expression)

    def set_angle_mode(self, mode):
        if mode not in ("DEG", "RAD", "GRAD"):
            raise ValueError(
                f"Invalid angle mode '{mode}'"
            )

        self.angle_mode = mode

        return self.angle_mode

    def toggle_angle_mode(self):
        modes = [
            "DEG",
            "RAD",
            "GRAD"
        ]

        current_index = modes.index(
            self.angle_mode
        )

        next_index = (
            current_index + 1
        ) % len(modes)

        self.angle_mode = modes[next_index]

        return self.angle_mode