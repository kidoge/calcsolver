import unittest
from calcsolver.state import State

class TestState(unittest.TestCase):

  def test_init(self):
    state = State(value=10)
    self.assertEqual(state.value(), 10)
