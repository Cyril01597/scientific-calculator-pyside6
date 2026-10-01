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