from app.expression.number import Number
from app.expression.binary import BinaryOperation
from app.expression.unary import UnaryOperation


class CalculatorEngine:

    def evaluate(self, expression):
        try:
            return expression.evaluate()

        except ZeroDivisionError:
            return "Error: Division by zero"

        except ValueError as error:
            return f"Error: {error}"

        except Exception as error:
            return f"Error: {error}"

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