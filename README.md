# Piecewise functions 

A library exposing a class for working with piecewise constant function.

## Contributing
1. Create a virtual environment and activate it
```shell
python3 -m venv .venv
source .venv/bin/acticate
```

2.Install the dependencies
```shell
pip install -r requirements.txt
```

3. Use the [black formatting](https://pypi.org/project/black/) for your contribution 

4. Your local dev environment is setup!

## Running the tests

With your virtual environment setup, from the project root directory run `pytest`

## Building & pushing the library
```bash
# 1. Use hatch to package the library
./build_lib.sh

# 2. Push to your favorite PyPy repo with:
#   (see TestPyPi doc https://packaging.python.org/en/latest/tutorials/packaging-projects/) 
python3 -m twine upload --repository testpypi dist/*

# 3. In your client project, install the desired version by running
pip install -i https://test.pypi.org/simple/ --no-deps piecewise-functions-fp==0.0.4
```

## Bibliography

- Piecewise constant function see the [Wolfram Mathworld post](https://mathworld.wolfram.com/PiecewiseConstantFunction.html) on the subject
- Heaviside Step function introduction at [this post](https://mathworld.wolfram.com/HeavisideStepFunction.html) and [Wikipedia](https://en.wikipedia.org/wiki/Heaviside_step_function)