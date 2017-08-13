"""This module contains the solvers for calcsolver."""

import random

def random_solve(problem):
    """Finds the solution by trying a random combination of operators."""
    while True:
        state = problem.starting_state()
        for _ in range(problem.move_count):
            operator = random.choice(problem.operators)
            try:
                state.apply(operator)
            except ValueError:
                continue
        if state.current_number == problem.end_number:
            return state.steps
