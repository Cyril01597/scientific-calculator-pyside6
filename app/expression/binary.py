from .base import Expression


class BinaryOperation(Expression):

    OPERATORS = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "^": lambda a, b: a ** b,
    }

    def __init__(self, left, operator, right):
        if operator not in self.OPERATORS:
            raise ValueError(
                f"Unknown binary operator '{operator}'"
            )

        self.left = left
        self.operator = operator
        self.right = right

    def evaluate(self, context=None):
        left_value = self.left.evaluate(
            context
        )

        right_value = self.right.evaluate(
            context
        )

        operation = self.OPERATORS[
            self.operator
        ]

        return operation(
            left_value,
            right_value
        )

    def __repr__(self):
        return (
            f"BinaryOperation("
            f"{self.left!r}, "
            f"'{self.operator}', "
            f"{self.right!r})"
        )