from src.PiecewiseFunctions.PiecewiseConstantFunction import PiecewiseConstantFunction


def main():
    piecewise_fn = PiecewiseConstantFunction(
        breakpoints=[-100.00, -50, 10, 20, 31.0], values=[30, 20, 10, -10]
    )
    piecewise_fn.draw(x_min=-100, x_max=30, num_points=1000)


if __name__ == "__main__":
    main()
