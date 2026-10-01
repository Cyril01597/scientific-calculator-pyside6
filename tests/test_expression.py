from app.expression.number import Number
from app.expression.variable import Variable
from app.expression.constant import Constant
from app.expression.unary import UnaryOperation
from app.expression.binary import BinaryOperation


def test_number():
    expression = Number(5)

    assert expression.evaluate() == 5


def test_variable():
    expression = Variable("x")

    assert expression.evaluate({
        "x": 10
    }) == 10


def test_constant():
    expression = Constant("pi")

    assert expression.evaluate() > 3.14
    assert expression.evaluate() < 3.15


def test_unary():
    expression = UnaryOperation(
        "sqrt",
        Number(25)
    )

    assert expression.evaluate() == 5


def test_binary():
    expression = BinaryOperation(
        Number(2),
        "+",
        Number(3)
    )

    assert expression.evaluate() == 5