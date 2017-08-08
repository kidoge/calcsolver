import unittest
from calcsolver.state import State

class TestState(unittest.TestCase):

  def test_default_init(self):
    state = State()
    self.assertEqual(state.value(), 0)
    self.assertEqual(state.steps(), [])
  
  def test_init_with_value(self):
    state = State(value=10)
    self.assertEqual(state.value(), 10)
    self.assertEqual(state.steps(), [])

  def test_init_with_steps(self):
    state = State(steps=['a','b'])
    self.assertEqual(state.value(), 0)
    self.assertEqual(state.steps(), ['a', 'b'])
