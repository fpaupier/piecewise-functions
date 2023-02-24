from typing import List, Tuple, Any


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

        Args:
            breakpoints:
            slopes:
            intercepts:

        Raises: ValueError if one of the input is invalid

        """
        return

    def evaluate(self, x: float) -> float:
        """
        Works similarly to the PiecewiseConstantFunction class, except it evaluates the function
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
