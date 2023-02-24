from src.PiecewiseConstantFunction import PiecewiseConstantFunction
import math


class TestHeaviside:
    breakpoints = [-math.inf, 0, math.inf]
    values = [0, 1]

    def test_init(self):
        try:
            heaviside = PiecewiseConstantFunction(self.breakpoints, self.values)
        except Exception:
            assert False
        assert True

    def test_evaluate_neg_int(self):
        heaviside = PiecewiseConstantFunction(self.breakpoints, self.values)
        evaluation = heaviside.evaluate(-10)
        assert evaluation == 0

    def test_evaluate_neg_float(self):
        heaviside = PiecewiseConstantFunction(self.breakpoints, self.values)
        evaluation = heaviside.evaluate(-math.pi)
        assert evaluation == 0

    def test_evaluate_pos_int(self):
        heaviside = PiecewiseConstantFunction(self.breakpoints, self.values)
        evaluation = heaviside.evaluate(193)
        assert evaluation == 1

    def test_evaluate_pos_float(self):
        heaviside = PiecewiseConstantFunction(self.breakpoints, self.values)
        evaluation = heaviside.evaluate(1898.09091822038)
        assert evaluation == 1
