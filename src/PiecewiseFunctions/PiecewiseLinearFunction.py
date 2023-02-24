from typing import List, Tuple, Any

import numpy as np
import matplotlib.pyplot as plt


class PiecewiseLinearFunction:
    """
    Represents a Piecewise Linear Function

    A piecewise linear function can be modeled as a function whose value is given by the equation

        `y = ax + b`

    over each of its domain of definitions
    """

    def __init__(
        self, breakpoints: List[float], slopes: List[float], intercepts: List[float]
    ) -> None:
        """
        The PiecewiseLinearFunction class takes three arguments in the constructor: breakpoints, slopes and intercepts.

        Args:
            breakpoints (List[float]): breakpoints is a list of the breakpoints of the function, i.e., the points at
                which the function changes equation.
            slopes (List[float]): values of the coefficient `a` in the equation `y = ax + b`
            intercepts (List[float]): values of the constant `b` in the equation `y = ax + b`

        Examples:
            if the breakpoints are [-10, 0, 10], the slopes are [5, 4] and the intercepts [9, -12], then:
            - on [-10, 0] - the function is defined by the equation `y = 5x + 9`
            - on [0, 10] - the function is defined by the equation `y = 4x - 12`

        Warnings: this implementation assumes that the breakpoints are given in increasing order, and that there are
        no repeated breakpoints. If these assumptions do not hold, the behavior of the class is not guaranteed to be
        correct. It is up to the user to ensure that the input is valid.

        Warnings: this implementation does not handle the case where the function is not defined at a breakpoint
        (i.e., where the function has a jump discontinuity). If such cases need to be handled,
        the implementation will need to be modified accordingly.
        Args:
            breakpoints (List[float]): list of n+1 breakpoints that define the intervals on which the function is defined
            slopes (List[float]): list of n slopes, one for each interval
            intercepts (List[float]):list of n intercepts, one for each interval
        """
        # Perform sanity checks over input
        self.sanity_check(breakpoints, slopes, intercepts)
        self.breakpoints = breakpoints
        self.slopes = slopes
        self.intercepts = intercepts

    @staticmethod
    def sanity_check(breakpoints: Any, slopes: Any, intercepts: Any) -> None:
        """
        Raises: ValueError if breakpoints, slopes or intercepts are not of the expected type for PiecewiseLinearFunction
        Args:
            breakpoints: (expected list to boundaries to test)
            slopes: (expected list of coefficient to test)
            intercepts: (expected list of constants to test)

        Returns: None

        """
        # Ensure types are valid
        if type(breakpoints) != list:
            raise ValueError("PiecewiseLinearFunction expects list for breakpoints")
        if type(intercepts) != list:
            raise ValueError("PiecewiseLinearFunction expects list for intercepts")

        # Check that slopes are numbers
        for val in slopes:
            if type(val) not in (float, int):
                raise ValueError(
                    "PiecewiseLinearFunction expects slope to be integer or floating point number"
                )
        # Check that intercepts are numbers
        for val in intercepts:
            if type(val) not in (float, int):
                raise ValueError(
                    "PiecewiseLinearFunction expects intercept to be integer or floating point number"
                )
        # Check that boundaries are numbers
        seen = set()
        for border in breakpoints:
            if border in seen:
                raise ValueError(
                    "PiecewiseLinearFunction expects breakpoints to be unique"
                )
            seen.add(border)
            if type(border) not in (float, int):
                raise ValueError(
                    "PiecewiseLinearFunction expects breakpoint to be integer or floating point number"
                )

        # Ensure breakpoints are sorted
        sorted_breakpoints: bool = all(
            breakpoints[i] <= breakpoints[i + 1] for i in range(len(breakpoints) - 1)
        )
        if not sorted_breakpoints:
            raise ValueError(
                "PiecewiseLinearFunction expects breakpoints to be passed in increasing order"
            )

        # Ensure breakpoints and values dimensions are coherent
        n_breakpoints: int = len(breakpoints)
        n_slopes: int = len(slopes)
        n_intercepts: int = len(intercepts)
        if n_breakpoints < 2:
            raise ValueError(
                "PiecewiseLinearFunction expects to have at least 2 breakpoints"
            )
        if n_slopes < 1:
            raise ValueError("PiecewiseLinearFunction expects to have at least 1 slope")
        if n_intercepts < 1:
            raise ValueError(
                "PiecewiseLinearFunction expects to have at least 1 intercept"
            )
        correct_dimensions: bool = (n_breakpoints == n_slopes + 1) and (
            n_breakpoints == n_intercepts + 1
        )
        if not correct_dimensions:
            raise ValueError(
                "PiecewiseLinearFunction expects to have n breakpoints and n-1 slopes and n-1 intercepts"
            )
        return

    def evaluate(self, x: float) -> float:
        """
        Works similarly to the PiecewiseLinearFunction class, except it evaluates the function
         using linear interpolation between the breakpoints.

        Args:
            x (float): value to evaluate the function on

        Returns:
            float the value of the evaluatioN

        """
        for i in range(len(self.breakpoints) - 1):
            if self.breakpoints[i] <= x < self.breakpoints[i + 1]:
                return self.slopes[i] * x + self.intercepts[i]
        raise ValueError(f"x={x} is out of bounds")

    def minimum(self) -> Tuple[float, float]:
        """
        Returns (min_value: float, arg_min: float): the minimum value of the function over its domain of definition,
        as well as the corresponding argument where this minimum value is attained.
        """
        min_value = float("inf")
        argmin = None
        for i in range(len(self.breakpoints) - 1):
            if self.slopes[i] == 0:
                value = self.intercepts[i]
            elif self.slopes[i] < 0:
                value = self.slopes[i] * self.breakpoints[i + 1] + self.intercepts[i]
            else:
                value = self.slopes[i] * self.breakpoints[i] + self.intercepts[i]
            if value < min_value:
                min_value = value
                argmin = self.breakpoints[i]
        return min_value, argmin

    def maximum(self) -> Tuple[float, float]:
        """
        Returns (max_value: float, arg_max: float): the maximum value of the function over its domain of definition,
        as well as the corresponding argument where this maximum value is attained.
        """
        max_value = float("-inf")
        argmax = None
        for i in range(len(self.breakpoints) - 1):
            if self.slopes[i] == 0:
                value = self.intercepts[i]
            elif self.slopes[i] > 0:
                value = self.slopes[i] * self.breakpoints[i + 1] + self.intercepts[i]
            else:
                value = self.slopes[i] * self.breakpoints[i] + self.intercepts[i]
            if value > max_value:
                max_value = value
                argmax = self.breakpoints[i]
        return max_value, argmax

    def draw(
        self, x_min: float = -10.0, x_max: float = 10.0, num_points: int = 1000
    ) -> None:
        """
        Generate a plot of the function over the input range.

        Args:
            x_min: lower bound
            x_max: higher bound
            num_points: number of points to sample

        Returns: None - print the function

        Raises: `ValueError` if `x_min` and `x_max` are out of the range or at their boundaries
        """
        # Generate a range of x values
        x_values = np.linspace(x_min, x_max, num_points)

        # Evaluate the function at each x value
        y_values = [self.evaluate(x) for x in x_values]

        # Plot the function
        plt.plot(x_values, y_values)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Piecewise Constant Function")
        plt.show()
