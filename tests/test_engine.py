from app.engine import CalculatorEngine


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