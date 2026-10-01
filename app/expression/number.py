from .base import Expression


class Number(Expression):
    def __init__(self, value):
        self.value = float(value)

    def evaluate(self, context=None):
        return self.value

    def __repr__(self):
        return f"Number({self.value})"