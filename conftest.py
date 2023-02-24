def pytest_configure(config):
    import src.PiecewiseFunctions  # NB this causes `src/PiecewiseFunctions/__init__.py` to run

    # set up any "aliases" (optional...)
    import sys, pathlib

    sys.path.append(str(pathlib.Path(__file__).parent))
    sys.modules["PiecewiseFunctions"] = sys.modules["src.PiecewiseFunctions"]
