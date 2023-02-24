import pytest
import math
from PiecewiseFunctions.PiecewiseLinearFunction import PiecewiseLinearFunction


class TestBadInputs:
    def test_valid_examples(self):
        breakpoints = [1, math.pi, 4, 10, 20.5, 10000]
        slopes = [0, -100.02, math.pi, 5, 7]
        intercepts = [10, -2, 1, 3, math.pi]
        piecewise_linear_fn = PiecewiseLinearFunction(breakpoints, slopes, intercepts)
        min_val, min_arg = piecewise_linear_fn.minimum()
        assert min_val == -100.02 * 4 - 2
        assert min_arg == 4

    def test_invalid_breakpoints_type(self):
        breakpoints = []
        slopes = []
        intercepts = []
        with pytest.raises(ValueError):
            PiecewiseLinearFunction(breakpoints, slopes, intercepts)

    def test_duplicate_breakpoints_type(self):
        breakpoints = [10, 10]
        slopes = [1]
        intercepts = [1]
        with pytest.raises(ValueError):
            PiecewiseLinearFunction(breakpoints, slopes, intercepts)

    def test_unsorted_breakpoints_type(self):
        breakpoints = [-10, 1, 10, 5]
        slopes = [0, 3, 4]
        intercepts = [2, 3, 4]
        with pytest.raises(ValueError):
            PiecewiseLinearFunction(breakpoints, slopes, intercepts)

    def test_unsorted_breakpoints_type_str(self):
        breakpoints = [-10, 1, 10, 20, "40"]
        slopes = [0, 3, 7, 4]
        intercepts = [1, 2, 3, 4]
        with pytest.raises(ValueError):
            PiecewiseLinearFunction(breakpoints, slopes, intercepts)

    def test_invalid_slopes_type(self):
        breakpoints = [-10, 1, 10, 20]
        slopes = [None, 3, "thirty three"]
        intercepts = [1, 2, 3]
        with pytest.raises(ValueError):
            PiecewiseLinearFunction(breakpoints, slopes, intercepts)

    def test_invalid_intercepts_type(self):
        breakpoints = [-10, 1, 10, 20]
        slopes = [1, 2, 3]
        intercepts = [None, 3, "thirty three"]
        with pytest.raises(ValueError):
            PiecewiseLinearFunction(breakpoints, slopes, intercepts)

    def test_invalid_slopes_type_container(self):
        breakpoints = [-10, 1, 10, 20]
        slopes = (None, 3, "thirty three")
        intercepts = [1, 2, 3]
        with pytest.raises(ValueError):
            PiecewiseLinearFunction(breakpoints, slopes, intercepts)

    def test_invalid_intercepts_type_container(self):
        breakpoints = [-10, 1, 10, 20]
        slopes = [1, 2, 3]
        intercepts = (None, 3, "thirty three")
        with pytest.raises(ValueError):
            PiecewiseLinearFunction(breakpoints, slopes, intercepts)

    def test_incoherent_input_dimensions(self):
        breakpoints = [-10, 1, 10, 20]
        slopes = [2, 3]
        intercepts = [3, 4, 3]
        with pytest.raises(ValueError):
            PiecewiseLinearFunction(breakpoints, slopes, intercepts)
