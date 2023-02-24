from src.PiecewiseConstantFunction import PiecewiseConstantFunction
import math


class TestHeaviside:
    breakpoints = [-math.inf, 0, math.inf]
    values = [0, 1]
    heaviside = PiecewiseConstantFunction(breakpoints, values)

    def test_evaluate_neg_int(self):
        evaluation = self.heaviside.evaluate(-10)
        assert evaluation == 0

    def test_evaluate_neg_float(self):
        evaluation = self.heaviside.evaluate(-math.pi)
        assert evaluation == 0

    def test_evaluate_pos_int(self):
        evaluation = self.heaviside.evaluate(193)
        assert evaluation == 1

    def test_evaluate_pos_float(self):
        evaluation = self.heaviside.evaluate(1898.09091822038)
        assert evaluation == 1

    def test_boundary(self):
        evaluation = self.heaviside.evaluate(0)
        assert evaluation == 1

    def test_boundary_inf(self):
        """Expect to break for infinity testing comparison"""
        value_error_raised = False
        try:
            self.heaviside.evaluate(math.inf)
        except ValueError:
            value_error_raised = True
        assert value_error_raised

    def test_boundary_minus_inf(self):
        """Expect to work for -infinity since we do a comparison x >= self.breakpoints[i]"""
        evaluation = self.heaviside.evaluate(-math.inf)
        assert evaluation == 0
