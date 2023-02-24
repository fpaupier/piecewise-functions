import time
import math
import random

from PiecewiseFunctions.PiecewiseLinearFunction import PiecewiseLinearFunction


class TestPiecewiseLinearFunction:
    breakpoints = [-math.inf, 0, math.inf]
    slopes = [0, 1]
    intercepts = [3, 4]
    plf = PiecewiseLinearFunction(breakpoints, slopes, intercepts)

    def test_evaluate_large_input(self):
        # Generate a large random input
        x = random.uniform(-1e6, 1e6)

        # Time the evaluation
        start_time = time.time()
        self.plf.evaluate(x)
        end_time = time.time()

        # Check that the evaluation took less than 1 second
        assert end_time - start_time < 1.0

    def test_get_min_large_input(self):
        # Generate a large number of breakpoints and slopes
        num_points = 100000
        breakpoints = (
            [-math.inf]
            + sorted([random.uniform(-1e6, 1e6) for _ in range(num_points)])
            + [math.inf]
        )
        slopes = [random.uniform(-1e6, 1e6) for _ in range(num_points + 1)]
        intercepts = [random.uniform(-1e6, 1e6) for _ in range(num_points + 1)]

        # Create a piecewise constant function with these breakpoints and slopes
        plf = PiecewiseLinearFunction(breakpoints, slopes, intercepts)

        # Time the minimum method
        start_time = time.time()
        plf.minimum()
        end_time = time.time()

        # Check that the minimum method took less than 0.5 second
        assert end_time - start_time < 0.5

    def test_get_max_large_input(self):
        # Generate a large number of breakpoints and slopes
        num_points = 100000
        breakpoints = (
            [-math.inf]
            + sorted([random.uniform(-1e6, 1e6) for _ in range(num_points)])
            + [math.inf]
        )
        slopes = [random.uniform(-1e6, 1e6) for _ in range(num_points + 1)]
        intercepts = [random.uniform(-1e6, 1e6) for _ in range(num_points + 1)]

        # Create a piecewise constant function with these breakpoints and slopes
        plf = PiecewiseLinearFunction(breakpoints, slopes, intercepts)

        # Time the maximum method
        start_time = time.time()
        plf.maximum()
        end_time = time.time()

        # Check that the maximum method took less than 0.5 second
        assert end_time - start_time < 0.5
