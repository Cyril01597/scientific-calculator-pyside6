import ast
from platform import node

from .number import Number
from .binary import BinaryOperation
from .unary import UnaryOperation
from .constant import Constant


class ExpressionParser:

    OPERATORS = {
        ast.Add: "+",
        ast.Sub: "-",
        ast.Mult: "*",
        ast.Div: "/",
        ast.Pow: "^",
    }

    FUNCTIONS = {
        "sqrt": "sqrt",
        "sin": "sin",
        "cos": "cos",
        "tan": "tan",
        "asin": "asin",
        "acos": "acos",
        "atan": "atan",
        "ln": "ln",
        "log": "log",
        "abs": "abs",
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

        if isinstance(node, ast.Call):

            if not isinstance(node.func, ast.Name):
                raise ValueError(
                    "Unsupported function"
                )

            function_name = node.func.id

            operator = self.FUNCTIONS.get(
                function_name
            )

            if operator is None:
                raise ValueError(
                    f"Unknown function '{function_name}'"
                )

            if len(node.args) != 1:
                raise ValueError(
                    f"Function '{function_name}' "
                    "requires one argument"
                )

            operand = self._convert(
                node.args[0]
            )

            return UnaryOperation(
                operator,
                operand
            )

        if isinstance(node, ast.Name):
            if node.id in Constant.VALUES:
                return Constant(node.id)
            
            raise ValueError(
                f"Unknown constant '{node.id}'"
            )
        
        raise ValueError(
            "Unsupported expression"
        )