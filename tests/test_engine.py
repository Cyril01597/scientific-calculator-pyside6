from app.engine import CalculatorEngine
from app.expression.number import Number
from app.expression.binary import BinaryOperation


def test_add():
    engine = CalculatorEngine()

    assert engine.add(2, 3) == 5


def test_subtract():
    engine = CalculatorEngine()

    assert engine.subtract(10, 4) == 6


def test_multiply():
    engine = CalculatorEngine()

    assert engine.multiply(6, 7) == 42


def test_divide():
    engine = CalculatorEngine()

    assert engine.divide(10, 2) == 5


def test_power():
    engine = CalculatorEngine()

    assert engine.power(2, 3) == 8


def test_sqrt():
    engine = CalculatorEngine()

    assert engine.sqrt(25) == 5


def test_division_by_zero():
    engine = CalculatorEngine()

    assert engine.divide(10, 0) == "Error: Division by zero"

def test_evaluate_nested_expression():
    engine = CalculatorEngine()

    expression = BinaryOperation(
        BinaryOperation(
            Number(2),
            "*",
            Number(3)
        ),
        "+",
        Number(4)
    )

    assert engine.evaluate(expression) == 10

def test_engine_input():
    engine = CalculatorEngine()

    assert engine.input("2") == "2"
    assert engine.input("+") == "2+"
    assert engine.input("3") == "2+3"

    assert engine.current_expression == "2+3"

def test_engine_clear():
    engine = CalculatorEngine()

    engine.input("123")

    assert engine.clear() == ""
    assert engine.current_expression == ""
    assert engine.result is None

def test_engine_backspace():
    engine = CalculatorEngine()

    engine.input("123")

    assert engine.backspace() == "12"
    assert engine.backspace() == "1"
    assert engine.backspace() == ""