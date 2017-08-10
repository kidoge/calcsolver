import unittest
from unittest.mock import Mock

from calcsolver.core import State


class TestState(unittest.TestCase):

  def test_default_init(self):
    state = State()
    self.assertEqual(state.current_number, 0)
    self.assertEqual(state.steps, [])
  
  def test_init_with_current_number(self):
    state = State(current_number=10)
    self.assertEqual(state.current_number, 10)
    self.assertEqual(state.steps, [])

  def test_init_with_steps(self):
    state = State(steps=['a','b'])
    self.assertEqual(state.current_number, 0)
    self.assertEqual(state.steps, ['a', 'b'])

  def test_apply_once(self):
    state = State()
    op = Mock()
    op.operate = Mock(return_value=3)
    state.apply(op)
    op.operate.assert_called_with(state)

    self.assertEqual(state.current_number, 3)
    self.assertEqual(state.steps, [op])

  def test_apply_twice(self):
    state = State()
    op1 = Mock()
    op1.operate = Mock(return_value=3)
    state.apply(op1)
    op1.operate.assert_called_with(state)

    def addTwo(state):
      return state.current_number + 4

    op2 = Mock()
    op2.operate.side_effect = addTwo
    state.apply(op2)
    op2.operate.assert_called_with(state)

    self.assertEqual(state.current_number, 7)
    self.assertEqual(state.steps, [op1, op2])
