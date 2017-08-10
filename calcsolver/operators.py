"""This module contains the operators supported by calcsolver."""

import abc

class Operator(object, metaclass=abc.ABCMeta): # pylint: disable=too-few-public-methods
    """Abstract base class for all operators."""
    @abc.abstractmethod
    def operate(self, state):
        """Performs an operation on the passed value"""
        pass

class AddOperator(Operator):
    """Adds a number."""
    def __init__(self, value):
        self._value = value

    def operate(self, state):
        return state.value() + self._value

    def __str__(self):
        if self._value > 0:
            sign = "+"
        else:
            sign = "-"
        return "[ %s %d ]" % (sign, abs(self._value))

    @property
    def value(self):
        """Returns value."""
        return self._value

class MultiplyOperator(Operator):
    """Multiplies a number."""
    def __init__(self, value):
        self._value = value

    def operate(self, state):
        return state.value() * self._value

    def __str__(self):
        return "[ * %d ]" % self._value

    @property
    def value(self):
        """Returns value."""
        return self._value

class DivideOperator(Operator):
    """Divides a number."""
    def __init__(self, value):
        self._value = value

    def operate(self, state):
        return state.value() / self._value

    def __str__(self):
        return "[ / %d ]" % self._value

    @property
    def value(self):
        """Returns value."""
        return self._value

