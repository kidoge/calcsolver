import unittest
from calcsolver.state import State
from calcsolver.operators import DivideOperator

class TestDivideOperator(unittest.TestCase):

  def test_divide_positive(self):
    state = State(value=50)
    state.apply(DivideOperator(5))
    self.assertEqual(state.value(), 10)

  def test_divide_negative(self):
    state = State(value=24)
    state.apply(DivideOperator(-3))
    self.assertEqual(state.value(), -8)

  def test_str_positive(self):
    string = str(DivideOperator(2))
    self.assertEqual(string, "[ / 2 ]")

  def test_str_negative(self):
    string = str(DivideOperator(-7))
    self.assertEqual(string, "[ / -7 ]")
