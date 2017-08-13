import unittest
from calcsolver.core import State
from calcsolver.operators import (
    OperatorWithNumber,
    AddOperator,
    MultiplyOperator,
    DivideOperator,
    DiscardOperator,
)

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


class TestMultiplyOperator(unittest.TestCase):
    def test_multiply_positive(self):
        state = State(current_number=6)
        state.apply(MultiplyOperator(4))
        self.assertEqual(state.current_number, 24)

    def test_multiply_negative(self):
        state = State(current_number=5)
        state.apply(MultiplyOperator(-3))
        self.assertEqual(state.current_number, -15)

    def test_str_positive(self):
        string = str(MultiplyOperator(4))
        self.assertEqual(string, "[ * 4 ]")

    def test_str_negative(self):
        string = str(MultiplyOperator(-6))
        self.assertEqual(string, "[ * -6 ]")

class TestDivideOperator(unittest.TestCase):
    def test_divide_positive(self):
        state = State(current_number=50)
        state.apply(DivideOperator(5))
        self.assertEqual(state.current_number, 10)

    def test_divide_negative(self):
        state = State(current_number=24)
        state.apply(DivideOperator(-3))
        self.assertEqual(state.current_number, -8)

    def test_positive_good_fraction(self):
        state = State(current_number=1)
        state.apply(DivideOperator(8))
        self.assertEqual(state.current_number, 0.125)

    def test_positive_bad_fraction(self):
        state = State(current_number=100)
        with self.assertRaises(ValueError):
            state.apply(DivideOperator(3))

    def test_negative_bad_fraction(self):
        state = State(current_number=-1)
        with self.assertRaises(ValueError):
            state.apply(DivideOperator(16))

    def test_str_positive(self):
        string = str(DivideOperator(2))
        self.assertEqual(string, "[ / 2 ]")

    def test_str_negative(self):
        string = str(DivideOperator(-7))
        self.assertEqual(string, "[ / -7 ]")

class TestDiscardOperator(unittest.TestCase):
    def test_discard_positive(self):
        output = DiscardOperator().operate(1234)
        self.assertEqual(output, 123)

    def test_discard_negative(self):
        output = DiscardOperator().operate(-7890)
        self.assertEqual(output, -789)

    def test_discard_single_digit(self):
        output = DiscardOperator().operate(5)
        self.assertEqual(output, 0)

    def test_discard_zero(self):
        output = DiscardOperator().operate(0)
        self.assertEqual(output, 0)

    def test_str(self):
        self.assertEqual(str(DiscardOperator()), "[ << ]")

