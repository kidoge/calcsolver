import unittest
from calcsolver.core import State
from calcsolver.operators import AddOperator

class TestAddOperator(unittest.TestCase):

  def test_add_zero(self):
    state = State(current_number=2)
    state.apply(AddOperator(0))
    self.assertEqual(state.current_number, 2)

  def test_add_positive(self):
    state = State(current_number=10)
    state.apply(AddOperator(5))
    self.assertEqual(state.current_number, 15)

  def test_add_negative(self):
    state = State(current_number=5)
    state.apply(AddOperator(-8))
    self.assertEqual(state.current_number, -3)

  def test_str_positive(self):
    string = str(AddOperator(3))
    self.assertEqual(string, "[ + 3 ]")

  def test_str_negative(self):
    string = str(AddOperator(-5))
    self.assertEqual(string, "[ - 5 ]")
