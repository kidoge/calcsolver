"""This module contains the operators supported by calcsolver."""

import abc

class Operator(object, metaclass=abc.ABCMeta): # pylint: disable=too-few-public-methods
    """Abstract base class for all operators."""
    @abc.abstractmethod
    def operate(self, state):
        """Performs an operation on the passed value."""
        pass

class AddOperator(Operator):
    """Operator that adds a number to the current number."""
    def __init__(self, value):
        self._value = value

    def operate(self, state):
        return state.current_number + self._value

    def __str__(self):
        if self._value > 0:
            sign = "+"
        else:
            sign = "-"
        return "[ %s %d ]" % (sign, abs(self._value))

    @property
    def value(self):
        """Returns the value to add to the current number."""
        return self._value

class MultiplyOperator(Operator):
    """Operator that multiplies the current number by a number."""
    def __init__(self, value):
        self._value = value

    def operate(self, state):
        return state.current_number * self._value

    def __str__(self):
        return "[ * %d ]" % self._value

    @property
    def value(self):
        """Returns the value to multiply the current number by."""
        return self._value

class DivideOperator(Operator):
    """Operator that divides the current number by a number."""
    def __init__(self, value):
        self._value = value

    def operate(self, state):
        return state.current_number / self._value

    def __str__(self):
        return "[ / %d ]" % self._value

    @property
    def value(self):
        """Returns the value to divide the current number by."""
        return self._value

