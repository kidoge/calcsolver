import unittest
from calcsolver.core import State
from calcsolver.operators import MultiplyOperator


class TestMultiplyOperator(unittest.TestCase):

    def test_multiply_positive(self):
        state = State(current_number=6)
        state.apply(MultiplyOperator(4))
        self.assertEqual(state.current_number, 24)

    def test_multiply_negative(self):
        state = State(current_number=5)
        state.apply(MultiplyOperator(-3))
        self.assertEqual(state.current_number, -15)

    def test_str_positive(self):
        string = str(MultiplyOperator(4))
        self.assertEqual(string, "[ * 4 ]")

    def test_str_negative(self):
        string = str(MultiplyOperator(-6))
        self.assertEqual(string, "[ * -6 ]")
