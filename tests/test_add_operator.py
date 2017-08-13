import unittest
from calcsolver.core import State
from calcsolver.operators import OperatorWithNumber, AddOperator

class OperatorWithNumber1(OperatorWithNumber):
    def operate(self, number):
        pass

class OperatorWithNumber2(OperatorWithNumber):
    def operate(self, number):
        pass

class TestOperatorWithNumber(unittest.TestCase):
    def test_same_operators(self):
        op1 = OperatorWithNumber1(2)
        op2 = OperatorWithNumber1(2)
        self.assertEqual(op1, op2)
        self.assertEqual(op2, op1)

    def test_different_numbers(self):
        op1 = OperatorWithNumber1(3)
        op2 = OperatorWithNumber1(5)
        self.assertNotEqual(op1, op2)
        self.assertNotEqual(op2, op1)

    def test_different_operators(self):
        op1 = OperatorWithNumber1(3)
        op2 = OperatorWithNumber2(3)
        self.assertNotEqual(op1, op2)
        self.assertNotEqual(op2, op1)

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


