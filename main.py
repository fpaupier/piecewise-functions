import math
from src.PiecewiseFunctions.PiecewiseConstantFunction import PiecewiseConstantFunction
from src.PiecewiseFunctions.PiecewiseLinearFunction import PiecewiseLinearFunction
from src.PiecewiseFunctions.utils import draw


def example_piecewise_constant_function():
    piecewise_fn = PiecewiseConstantFunction(
        breakpoints=[-100.00, -50, 10, 20, 31.0], values=[30, 20, 10, -10]
    )
    draw(
        piecewise_fn,
        x_min=-100,
        x_max=30,
        num_points=1000,
        title="Piecewise Constant Function",
    )


def example_piecewise_linear_function() -> None:
    breakpoints = [1, math.pi, 4, 10, 20.5, 10000]
    slopes = [0, -100.02, math.pi, 5, 7]
    intercepts = [10, -2, 1, 3, math.pi]
    piecewise_fn = PiecewiseLinearFunction(breakpoints, slopes, intercepts)
    draw(
        piecewise_fn,
        x_min=1,
        x_max=30,
        num_points=10000,
        title="Piecewise Linear Function",
    )


if __name__ == "__main__":
    example_piecewise_linear_function()
