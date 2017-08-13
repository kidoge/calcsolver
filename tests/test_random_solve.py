import unittest
from calcsolver.core import Problem
from calcsolver.operators import AddOperator, DivideOperator, MultiplyOperator
from calcsolver.solvers import random_solve 


class TestRandomSolve(unittest.TestCase):

    def test_only_option(self):
        operators = [AddOperator(3)]
        problem = Problem(start_number=2,
                          end_number=5,
                          move_count=1,
                          operators=operators)
        solution = random_solve(problem)
        self.assertEqual(solution, [AddOperator(3)])

    def test_multiple_options(self):
        operators = [AddOperator(1),
                     MultiplyOperator(2),
                     DivideOperator(3)]
        problem = Problem(start_number=10,
                          end_number=20,
                          move_count=1,
                          operators=operators)
        solution = random_solve(problem)
        self.assertEqual(solution, [MultiplyOperator(2)])

    def test_multiple_steps(self):
        operators = [AddOperator(1),
                     MultiplyOperator(20),
                     DivideOperator(3)]
        problem = Problem(start_number=2,
                          end_number=1,
                          move_count=2,
                          operators=operators)
        solution = random_solve(problem)
        self.assertEqual(solution, [AddOperator(1),
                                    DivideOperator(3)])

