from PiecewiseFunctions.PiecewiseLinearFunction import PiecewiseLinearFunction
import math


class TestNominalPLF:
    breakpoints = [-math.inf, 0, 10, 30, 70, math.inf]
    slopes = [2, 3, 7, -3, 1]
    intercepts = [3, 12, -2, 3, 3]
    plf = PiecewiseLinearFunction(breakpoints, slopes, intercepts)

    def test_evaluate_neg_int(self):
        evaluation = self.plf.evaluate(-10)
        assert evaluation == 2 * (-10) + 3

    def test_evaluate_border(self):
        evaluation = self.plf.evaluate(0)
        assert evaluation == 3 * (0) + 12
