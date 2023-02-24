# Technical assessment - Lambda Automata 

## Mission brief 

**Below is the take-home-project question (preferably Python**; C++ would also be acceptable if you prefer that):

- Design and implement **a class to store and evaluate a piecewise constant function.**
- Provide an evaluation function, i.e., to give its value (or fail) for any possible real number as input.
- Provide a function to get its minimum value and argmin.
- Provide a function to get its maximum value and argmax.
**Bonus points:**
- Provide sufficient correctness tests, using PyTest. Pay special attention to handling corner cases or bad input.
- Provide sufficient timing tests. At which point your functions struggles down ? Under which scenario would the 3 class methods slow down ?
- Provide a Jupyter notebook demonstrating the functionality of your class.
- Repeat for **a piecewise linear function.**

**Reminders:**
1. There is no hard deadline for the question. Take your time and do it at your own pace.
2. Use your own judgement / design, on how to handle failure modes. There is not one correct answer for that design aspect.
3. If possible try to follow as much as possible, what you consider best practices, for providing a working python library.

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

3. Your local dev environment is setup!

## Running the tests

With your virtual environment setup, from the project root directory run `pytest`

## Bibliography

- Piecewise constant function see the [Wolfram Mathworld post](https://mathworld.wolfram.com/PiecewiseConstantFunction.html) on the subject
- Heaviside Step function introduction at [this post](https://mathworld.wolfram.com/HeavisideStepFunction.html)