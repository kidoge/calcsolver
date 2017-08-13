import unittest
from calcsolver.core import Problem


class TestProblem(unittest.TestCase):

    def test_init(self):
        prob = Problem(start_number=10,
                       end_number=24,
                       move_count=5,
                       operators=[1, 2, 3])
        self.assertEqual(prob.start_number, 10)
        self.assertEqual(prob.end_number, 24)
        self.assertEqual(prob.move_count, 5)
        self.assertEqual(prob.operators, [1, 2, 3])
    
    def test_starting_state(self):
        prob = Problem(start_number=10,
                       end_number=24,
                       move_count=5,
                       operators=[1, 2, 3])
        state = prob.starting_state()
        self.assertEqual(state.current_number, 10)
        self.assertEqual(state.steps, [])
