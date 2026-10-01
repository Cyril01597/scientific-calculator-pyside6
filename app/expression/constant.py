import math

from .base import Expression


class Constant(Expression):
    VALUES = {
        "pi": math.pi,
        "e": math.e,
    }

    def __init__(self, name):
        if name not in self.VALUES:
            raise ValueError(
                f"Unknown constant '{name}'"
            )

        self.name = name

    def evaluate(self, context=None):
        return self.VALUES[self.name]

    def __repr__(self):
        return f"Constant('{self.name}')"