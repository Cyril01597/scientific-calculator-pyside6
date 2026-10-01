import math

from .base import Expression


class UnaryOperation(Expression):

    FUNCTIONS = {
        "negate": lambda x: -x,
        "sqrt": math.sqrt,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "asin": math.asin,
        "acos": math.acos,
        "atan": math.atan,
        "ln": math.log,
        "log": math.log10,
        "abs": abs,
    }

    def __init__(self, operator, operand):
        if operator not in self.FUNCTIONS:
            raise ValueError(
                f"Unknown unary operator '{operator}'"
            )

        self.operator = operator
        self.operand = operand

    def evaluate(self, context=None):
        value = self.operand.evaluate(context)

        operation = self.FUNCTIONS[
            self.operator
        ]

        return operation(value)

    def __repr__(self):
        return (
            f"UnaryOperation("
            f"'{self.operator}', "
            f"{self.operand!r})"
        )