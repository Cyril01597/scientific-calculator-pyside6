import ast

from .number import Number
from .binary import BinaryOperation
from .unary import UnaryOperation


class ExpressionParser:

    OPERATORS = {
        ast.Add: "+",
        ast.Sub: "-",
        ast.Mult: "*",
        ast.Div: "/",
        ast.Pow: "^",
    }

    def parse(self, expression):
        expression = expression.replace("^", "**")

        tree = ast.parse(
            expression,
            mode="eval"
        )

        return self._convert(tree.body)

    def _convert(self, node):

        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return Number(node.value)

            raise ValueError(
                "Invalid constant"
            )

        if isinstance(node, ast.BinOp):

            operator = self.OPERATORS.get(
                type(node.op)
            )

            if operator is None:
                raise ValueError(
                    "Unsupported operator"
                )

            left = self._convert(node.left)
            right = self._convert(node.right)

            return BinaryOperation(
                left,
                operator,
                right
            )

        if isinstance(node, ast.UnaryOp):

            if isinstance(node.op, ast.USub):
                operand = self._convert(
                    node.operand
                )

                return UnaryOperation(
                    "negate",
                    operand
                )

            if isinstance(node.op, ast.UAdd):
                return self._convert(
                    node.operand
                )

            raise ValueError(
                "Unsupported unary operator"
            )

        raise ValueError(
            "Unsupported expression"
        )