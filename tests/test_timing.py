import time
import math
import random

from PiecewiseFunctions.PiecewiseConstantFunction import PiecewiseConstantFunction


class TestPiecewiseConstantFunction:
    breakpoints = [-math.inf, 0, math.inf]
    values = [0, 1]
    heaviside = PiecewiseConstantFunction(breakpoints, values)

    def test_evaluate_large_input(self):
        # Generate a large random input
        x = random.uniform(-1e6, 1e6)

        # Time the evaluation
        start_time = time.time()
        self.heaviside.evaluate(x)
        end_time = time.time()

        # Check that the evaluation took less than 1 second
        assert end_time - start_time < 1.0

    def test_get_min_large_input(self):
        # Generate a large number of breakpoints and values
        num_points = 100000
        breakpoints = (
            [-math.inf]
            + sorted([random.uniform(-1e6, 1e6) for _ in range(num_points)])
            + [math.inf]
        )
        values = [random.uniform(-1e6, 1e6) for _ in range(num_points + 1)]

        # Create a piecewise constant function with these breakpoints and values
        pcf = PiecewiseConstantFunction(breakpoints, values)

        # Time the minimum method
        start_time = time.time()
        pcf.minimum()
        end_time = time.time()

        # Check that the minimum method took less than 0.5 second
        assert end_time - start_time < 0.5

    def test_get_max_large_input(self):
        # Generate a large number of breakpoints and values
        num_points = 100000
        breakpoints = (
            [-math.inf]
            + sorted([random.uniform(-1e6, 1e6) for _ in range(num_points)])
            + [math.inf]
        )
        values = [random.uniform(-1e6, 1e6) for _ in range(num_points + 1)]

        # Create a piecewise constant function with these breakpoints and values
        pcf = PiecewiseConstantFunction(breakpoints, values)

        # Time the maximum method
        start_time = time.time()
        pcf.maximum()
        end_time = time.time()

        # Check that the maximum method took less than 0.5 second
        assert end_time - start_time < 0.5
