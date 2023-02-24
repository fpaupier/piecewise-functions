from src.PiecewiseConstantFunction import PiecewiseConstantFunction
import math


class TestPiecewiseConstant:
    breakpoints = [-math.inf, -1, 1, math.inf]
    values = [0, 1, -1]
    piecewise_constant = PiecewiseConstantFunction(breakpoints, values)

    def test_evaluate_neg_int(self):
        evaluation = self.piecewise_constant.evaluate(-10)
        assert evaluation == 0

    def test_evaluate_neg_float(self):
        evaluation = self.piecewise_constant.evaluate(-0.5)
        assert evaluation == 1

    def test_evaluate_pos_int(self):
        evaluation = self.piecewise_constant.evaluate(3)
        assert evaluation == -1

    def test_evaluate_pos_float(self):
        evaluation = self.piecewise_constant.evaluate(0.5)
        assert evaluation == 1

    def test_boundary_left(self):
        evaluation = self.piecewise_constant.evaluate(-1)
        assert evaluation == 1

    def test_boundary_right(self):
        evaluation = self.piecewise_constant.evaluate(1)
        assert evaluation == -1

    def test_boundary_inf(self):
        """Expect to break for infinity testing comparison"""
        value_error_raised = False
        try:
            self.piecewise_constant.evaluate(math.inf)
        except ValueError:
            value_error_raised = True
        assert value_error_raised

    def test_boundary_minus_inf(self):
        evaluation = self.piecewise_constant.evaluate(-math.inf)
        assert evaluation == 0

    def test_min(self):
        min_val, arg_min = self.piecewise_constant.minimum()
        assert min_val == -1
        assert 1 <= arg_min <= math.inf

    def test_max(self):
        max_val, arg_max = self.piecewise_constant.maximum()
        assert max_val == 1
        assert -1 <= arg_max <= 1
