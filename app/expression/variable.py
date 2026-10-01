from .base import Expression


class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def evaluate(self, context=None):
        if context is None:
            raise ValueError(
                f"No value provided for variable '{self.name}'"
            )

        if self.name not in context:
            raise ValueError(
                f"No value provided for variable '{self.name}'"
            )

        return context[self.name]

    def __repr__(self):
        return f"Variable('{self.name}')"