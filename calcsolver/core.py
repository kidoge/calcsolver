"""This module contains classes that are used in the rest of the module."""


class Problem:
    """This class describes the problem definition."""

    def __init__(self, start_number, end_number, move_count, operators):
        self._start_number = start_number
        self._end_number = end_number
        self._move_count = move_count
        self._operators = operators

    def starting_state(self):
        return State(self._start_number)

    @property
    def start_number(self):
        """Returns the starting number."""
        return self._start_number

    @property
    def end_number(self):
        """Returns the final number."""
        return self._end_number

    @property
    def move_count(self):
        """Returns the number of moves available."""
        return self._move_count

    @property
    def operators(self):
        """Returns the list of available operators."""
        return self._operators


class State:
    """This class describes the state of the game, and how the state was reached."""

    def __init__(self, current_number=None, steps=None):

        if current_number is None:
            current_number = 0
        if steps is None:
            steps = []

        self._current_number = current_number
        self._steps = steps

    def clone(self):
        """Returns a clone object."""
        return State(self._current_number, list(self._steps))

    def apply(self, operator):
        """Applies an operator to the current state."""
        self._steps.append(operator)
        self._current_number = operator.operate(self._current_number)

    @property
    def current_number(self):
        """Returns the current number."""
        return self._current_number

    @property
    def steps(self):
        """Returns steps."""
        return self._steps
