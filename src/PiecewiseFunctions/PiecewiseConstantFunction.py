from typing import List, Tuple, Any

from PiecewiseFunctions.PiecewiseFunction import PiecewiseFunction


class PiecewiseConstantFunction(PiecewiseFunction):
    """
    Represents a Piecewise Constant Function

    A piecewise constant function can be modeled as a function whose value is given by the equation

        `y = b`

    over each of its domain of definitions.
    """

    def __init__(self, breakpoints: List[float], values: List[float]):
        """
        The PiecewiseConstantFunction class takes two arguments in the constructor: breakpoints and values.

        Args:
            breakpoints (List[float]): breakpoints is a list of the breakpoints of the function, i.e., the points at which the function changes value.
            values (List[float]): values is a list of the function's constant values between each pair of breakpoints.

        Examples:
            if the breakpoints are [0, 1, 2, 3] and the values are [1, 2, 1], then the function
            is equal to 1 on the interval [0, 1), equal to 2 on the interval [1, 2), and equal to 1
            on the interval [2, 3).

        Warnings: this implementation assumes that the breakpoints are given in increasing order, and that there are
        no repeated breakpoints. If these assumptions do not hold, the behavior of the class is not guaranteed to be
        correct. It is up to the user to ensure that the input is valid.

        Warnings: this implementation does not handle the case where the function is not defined at a breakpoint
        (i.e., where the function has a jump discontinuity). If such cases need to be handled,
        the implementation will need to be modified accordingly.
        """

        # Perform sanity checks over input
        self.sanity_check(breakpoints, values)
        self.breakpoints = breakpoints
        self.values = values

    @staticmethod
    def sanity_check(breakpoints: Any, values: Any) -> None:
        """
        Raises: ValueError if breakpoints or values are not of the expected type for PiecewiseConstantFunction
        Args:
            breakpoints: (expected list to boundaries to test)
            values: (expected list of numbers to test)

        Returns: None

        """
        # Ensure types are valid
        if type(breakpoints) != list:
            raise ValueError("PiecewiseConstantFunction expects list for breakpoints")
        if type(values) != list:
            raise ValueError("PiecewiseConstantFunction expects list for values")

        # Check that values are numbers
        for val in values:
            if type(val) not in (float, int):
                raise ValueError(
                    "PiecewiseConstantFunction expects value to be integer or floating point number"
                )
        # Check that boundaries are numbers
        seen = set()
        for border in breakpoints:
            if border in seen:
                raise ValueError(
                    "PiecewiseConstantFunction expects breakpoints to be unique"
                )
            seen.add(border)
            if type(border) not in (float, int):
                raise ValueError(
                    "PiecewiseConstantFunction expects breakpoint to be integer or floating point number"
                )

        # Ensure breakpoints are sorted
        sorted_breakpoints: bool = all(
            breakpoints[i] <= breakpoints[i + 1] for i in range(len(breakpoints) - 1)
        )
        if not sorted_breakpoints:
            raise ValueError(
                "PiecewiseConstantFunction expects breakpoints to be passed in increasing order"
            )

        # Ensure breakpoints and values dimensions are coherent
        n_breakpoints: int = len(breakpoints)
        n_values: int = len(values)
        if n_breakpoints < 2:
            raise ValueError(
                "PiecewiseConstantFunction expects to have at least 2 breakpoints"
            )
        if n_values < 1:
            raise ValueError(
                "PiecewiseConstantFunction expects to have at least 1 value"
            )
        correct_dimensions: bool = n_breakpoints == n_values + 1
        if not correct_dimensions:
            raise ValueError(
                "PiecewiseConstantFunction expects to have n breakpoints and n-1 values"
            )
        return

    def evaluate(self, x: float) -> float:
        """
        The evaluate method takes a single argument x, and returns the value of the function at that point.

        Args:
            x: (float) the argument to evaluate the function on.

        Raises:
            ValueError: If x is outside the domain of the function, i.e., less than the first breakpoint or
             greater than or equal to the last breakpoint, a ValueError is raised.

            ValueError: If x is within the domain of the function, the method searches for the interval containing x,
             and returns the corresponding value. If no interval is found, a ValueError is raised.

        Returns:
            The value of the piecewise constant function on the given argument

        """
        if x < self.breakpoints[0] or x >= self.breakpoints[-1]:
            raise ValueError(f"Input value {x} is out of bounds.")
        for i in range(len(self.breakpoints) - 1):
            if self.breakpoints[i] <= x < self.breakpoints[i + 1]:
                return self.values[i]
        raise ValueError(f"No interval found for input value {x}.")

    def minimum(self) -> Tuple[float, float]:
        """
        Returns: ((min value, arg min)) the minimum value of the function and the corresponding argmin, i.e., the left endpoint
        of the interval where the minimum is achieved.

        Notes: The maximum method works analogously.

        """
        min_val = min(self.values)
        argmin = self.breakpoints[self.values.index(min_val)]
        return min_val, argmin

    def maximum(self) -> Tuple[float, float]:
        """
        Analogs to minimum implementation
        Returns: (max value, arg max)
        """
        max_val = max(self.values)
        argmax = self.breakpoints[self.values.index(max_val)]
        return max_val, argmax
