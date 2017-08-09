import unittest
from calcsolver.state import State
from calcsolver.operators import MultiplyOperator

class TestMultiplyOperator(unittest.TestCase):

  def test_multiply_positive(self):
    state = State(value=6)
    state.apply(MultiplyOperator(4))
    self.assertEqual(state.value(), 24)

  def test_multiply_negative(self):
    state = State(value=5)
    state.apply(MultiplyOperator(-3))
    self.assertEqual(state.value(), -15)

  def test_str_positive(self):
    string = str(MultiplyOperator(4))
    self.assertEqual(string, "[ * 4 ]")

  def test_str_negative(self):
    string = str(MultiplyOperator(-6))
    self.assertEqual(string, "[ * -6 ]")
