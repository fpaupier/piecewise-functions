import numpy as np
import matplotlib.pyplot as plt

from PiecewiseFunctions.PiecewiseFunction import PiecewiseFunction


def draw(
    fn: PiecewiseFunction,
    x_min: float = -10.0,
    x_max: float = 10.0,
    num_points: int = 1000,
) -> None:
    """
    Generate a plot of the function over the input range.

    Args:
        fn (PiecewiseFunction):
        x_min: lower bound
        x_max: higher bound
        num_points: number of points to sample

    Returns: None - print the function

    Raises: `ValueError` if `x_min` and `x_max` are out of the range or at their boundaries
    """
    # Generate a range of x values
    x_values = np.linspace(x_min, x_max, num_points)

    # Evaluate the function at each x value
    y_values = [fn.evaluate(x) for x in x_values]

    # Plot the function
    plt.plot(x_values, y_values)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Piecewise Constant Function")
    plt.show()
