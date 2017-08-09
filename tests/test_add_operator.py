import unittest
from calcsolver.state import State
from calcsolver.operators import AddOperator

class TestAddOperator(unittest.TestCase):

  def test_add_zero(self):
    state = State(value=2)
    state.apply(AddOperator(0))
    self.assertEqual(state.value(), 2)

  def test_add_positive(self):
    state = State(value=10)
    state.apply(AddOperator(5))
    self.assertEqual(state.value(), 15)

  def test_add_negative(self):
    state = State(value=5)
    state.apply(AddOperator(-8))
    self.assertEqual(state.value(), -3)
