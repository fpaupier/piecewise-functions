import pytest
import math
from PiecewiseFunctions.PiecewiseConstantFunction import PiecewiseConstantFunction


class TestBadInputs:
    def test_valid_examples(self):
        breakpoints = [1, math.pi, 4, 10, 20.5, 10000]
        values = [0, -100.02, math.pi, 5, 7]
        piecewise_constant_fn = PiecewiseConstantFunction(breakpoints, values)
        min_val, min_arg = piecewise_constant_fn.minimum()
        assert min_val == -100.02
        assert math.pi <= min_arg <= 4

    def test_invalid_breakpoints_type(self):
        breakpoints = []
        values = []
        with pytest.raises(ValueError):
            PiecewiseConstantFunction(breakpoints, values)

    def test_unsorted_breakpoints_type(self):
        breakpoints = [-10, 1, 10, 5]
        values = [0, 3, 4]
        with pytest.raises(ValueError):
            PiecewiseConstantFunction(breakpoints, values)

    def test_unsorted_breakpoints_type_str(self):
        breakpoints = [-10, 1, 10, 20, "40"]
        values = [0, 3, 7, 4]
        with pytest.raises(ValueError):
            PiecewiseConstantFunction(breakpoints, values)

    def test_invalid_values_type(self):
        breakpoints = [-10, 1, 10, 20]
        values = [None, 3, "thirty three"]
        with pytest.raises(ValueError):
            PiecewiseConstantFunction(breakpoints, values)

    def test_invalid_values_type_container(self):
        breakpoints = [-10, 1, 10, 20]
        values = (None, 3, "thirty three")
        with pytest.raises(ValueError):
            PiecewiseConstantFunction(breakpoints, values)

    def test_incoherent_input_dimensions(self):
        breakpoints = [-10, 1, 10, 20]
        values = [2]
        with pytest.raises(ValueError):
            PiecewiseConstantFunction(breakpoints, values)
