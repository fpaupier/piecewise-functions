from PiecewiseFunctions.PiecewiseLinearFunction import PiecewiseLinearFunction
import math


class TestNominalPLF:
    breakpoints = [-math.inf, 0, math.inf]
    slopes = [2, 3]
    intercepts = [3, 12]
    plf = PiecewiseLinearFunction(breakpoints, slopes, intercepts)

    def test_evaluate_neg_nt(self):
        evaluation = self.plf.evaluate(-10)
        assert evaluation == 2 * (-10) + 3
