import math
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

def test_default_angle_mode():
    engine = CalculatorEngine()

    assert engine.angle_mode == "DEG"


def test_set_angle_mode():
    engine = CalculatorEngine()

    assert engine.set_angle_mode("RAD") == "RAD"
    assert engine.angle_mode == "RAD"

    assert engine.set_angle_mode("GRAD") == "GRAD"
    assert engine.angle_mode == "GRAD"


def test_toggle_angle_mode():
    engine = CalculatorEngine()

    assert engine.toggle_angle_mode() == "RAD"
    assert engine.toggle_angle_mode() == "GRAD"
    assert engine.toggle_angle_mode() == "DEG"


def test_invalid_angle_mode():
    engine = CalculatorEngine()

    try:
        engine.set_angle_mode("INVALID")
        assert False
    except ValueError:
        assert True


def test_sin_degrees():
    engine = CalculatorEngine()

    engine.set_angle_mode("DEG")

    assert abs(engine.sin(30) - 0.5) < 1e-10


def test_sin_radians():
    engine = CalculatorEngine()

    engine.set_angle_mode("RAD")

    assert abs(
        engine.sin(math.pi / 6) - 0.5
    ) < 1e-10


def test_sin_gradians():
    engine = CalculatorEngine()

    engine.set_angle_mode("GRAD")

    assert abs(engine.sin(50) - 0.707106781) < 1e-8