from src.PiecewiseConstantFunction import PiecewiseConstantFunction
import math


class TestConstant:
    breakpoints = [-math.inf, math.inf]
    values = [1]
    constant = PiecewiseConstantFunction(breakpoints, values)

    def test_evaluate_neg_int(self):
        evaluation = self.constant.evaluate(-10)
        assert evaluation == 1

    def test_evaluate_pos_int(self):
        evaluation = self.constant.evaluate(193)
        assert evaluation == 1

    def test_boundary(self):
        evaluation = self.constant.evaluate(0)
        assert evaluation == 1

    def test_boundary_inf(self):
        """Expect to break for math.inf"""
        value_error_raised = False
        try:
            self.constant.evaluate(math.inf)
        except ValueError:
            value_error_raised = True
        assert value_error_raised

    def test_boundary_minus_inf(self):
        evaluation = self.constant.evaluate(-math.inf)
        assert evaluation == 1

    def test_min(self):
        min_val, arg_min = self.constant.minimum()
        assert min_val == 1
        assert -math.inf <= arg_min <= math.inf

    def test_max(self):
        max_val, arg_max = self.constant.maximum()
        assert max_val == 1
        assert -math.inf <= arg_max <= math.inf
