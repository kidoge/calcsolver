import unittest
from unittest.mock import Mock

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

  def test_apply_once(self):
    state = State()
    op = Mock()
    op.operate = Mock(return_value=3)
    state.apply(op)
    op.operate.assert_called_with(state)

    self.assertEqual(state.value(), 3)
    self.assertEqual(state.steps(), [op])

  def test_apply_twice(self):
    state = State()
    op1 = Mock()
    op1.operate = Mock(return_value=3)
    state.apply(op1)
    op1.operate.assert_called_with(state)

    def addTwo(state):
      return state.value() + 4

    op2 = Mock()
    op2.operate.side_effect = addTwo
    state.apply(op2)
    op2.operate.assert_called_with(state)

    self.assertEqual(state.value(), 7)
    self.assertEqual(state.steps(), [op1, op2])
