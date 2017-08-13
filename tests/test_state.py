import unittest
from unittest.mock import Mock

from calcsolver.core import State


def add_four(current_number):
    return current_number + 4


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
        state = State(steps=['a', 'b'])
        self.assertEqual(state.current_number, 0)
        self.assertEqual(state.steps, ['a', 'b'])

    def test_apply_once(self):
        state = State(current_number=1)
        op1 = Mock()
        op1.operate = Mock(return_value=3)
        state.apply(op1)
        op1.operate.assert_called_with(1)

        self.assertEqual(state.current_number, 3)
        self.assertEqual(state.steps, [op1])

    def test_apply_twice(self):
        state = State()

        op1 = Mock()
        op1.operate.side_effect = add_four
        state.apply(op1)
        op1.operate.assert_called_with(0)

        op2 = Mock()
        op2.operate = Mock(return_value=7)
        state.apply(op2)
        op2.operate.assert_called_with(4)

        self.assertEqual(state.current_number, 7)
        self.assertEqual(state.steps, [op1, op2])

    def test_clone_values(self):
        state = State(current_number=3, steps=[2, 4, 8])
        cloned_state = state.clone()

        self.assertEqual(cloned_state.current_number, 3)
        self.assertEqual(cloned_state.steps, [2, 4, 8])

    def test_clone_is_separate_instance(self):
        state = State(current_number=3, steps=[2, 4, 8])
        cloned_state = state.clone()

        op1 = Mock()
        op1.operate.side_effect = add_four
        state.apply(op1)

        self.assertEqual(cloned_state.current_number, 3)
        self.assertEqual(cloned_state.steps, [2, 4, 8])
