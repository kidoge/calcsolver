import unittest
from calcsolver.core import Problem
from calcsolver.operators import AddOperator
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
