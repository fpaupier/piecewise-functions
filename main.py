from src.PiecewiseFunctions.PiecewiseConstantFunction import PiecewiseConstantFunction
from src.PiecewiseFunctions.PiecewiseLinearFunction import PiecewiseLinearFunction
from src.PiecewiseFunctions.utils import draw


def example_piecewise_constant_function():
    piecewise_fn = PiecewiseConstantFunction(
        breakpoints=[-100.00, -50, 10, 20, 31.0], values=[30, 20, 10, -10]
    )
    draw(piecewise_fn, x_min=-100, x_max=30, num_points=1000)


def example_piecewise_linear_function() -> None:
    piecewise_fn = PiecewiseLinearFunction(
        breakpoints=[0, 10, 20, 31.0],
        slopes=[2, 4, 8],
        intercepts=[0, 1, 2],
    )
    draw(piecewise_fn, x_min=0, x_max=30, num_points=1000)


if __name__ == "__main__":
    example_piecewise_linear_function()
