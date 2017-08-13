"""This module contains the solvers for calcsolver."""

import random

def random_solve(problem):
    while True:
        state = problem.starting_state()
        for idx in range(problem.move_count):
            operator = random.choice(problem.operators)
            state.apply(operator)
        if state.current_number == problem.end_number:
            return state.steps
