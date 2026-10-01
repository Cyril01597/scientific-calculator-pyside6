from app.expression.parser import ExpressionParser


def test_parse_number():
    parser = ExpressionParser()

    expression = parser.parse("5")

    assert expression.evaluate() == 5


def test_parse_addition():
    parser = ExpressionParser()

    expression = parser.parse("2 + 3")

    assert expression.evaluate() == 5


def test_parse_precedence():
    parser = ExpressionParser()

    expression = parser.parse("2 + 3 * 4")

    assert expression.evaluate() == 14


def test_parse_parentheses():
    parser = ExpressionParser()

    expression = parser.parse(
        "(2 + 3) * 4"
    )

    assert expression.evaluate() == 20


def test_parse_power():
    parser = ExpressionParser()

    expression = parser.parse("2 ^ 3")

def test_parse_negative_number():
    parser = ExpressionParser()

    expression = parser.parse("-5 + 2")

    assert expression.evaluate() == -3

def test_parse_sqrt():
    parser = ExpressionParser()

    expression = parser.parse("sqrt(25)")

    assert expression.evaluate() == 5


def test_parse_sin():
    parser = ExpressionParser()

    expression = parser.parse("sin(0)")

    assert expression.evaluate() == 0


def test_parse_cos():
    parser = ExpressionParser()

    expression = parser.parse("cos(0)")

    assert expression.evaluate() == 1


def test_parse_log():
    parser = ExpressionParser()

    expression = parser.parse("log(100)")

    assert expression.evaluate() == 2


def test_parse_nested_function():
    parser = ExpressionParser()

    expression = parser.parse(
        "sqrt(3 ^ 2 + 4 ^ 2)"
    )

    assert expression.evaluate() == 5

def test_parse_pi():
    parser = ExpressionParser()

    expression = parser.parse("pi")

    assert expression.evaluate() > 3.14
    assert expression.evaluate() < 3.15


def test_parse_e():
    parser = ExpressionParser()

    expression = parser.parse("e")

    assert expression.evaluate() > 2.71
    assert expression.evaluate() < 2.72


def test_parse_constant_expression():
    parser = ExpressionParser()

    expression = parser.parse("2 * pi")

    assert expression.evaluate() > 6.28
    assert expression.evaluate() < 6.29