![Build](https://github.com/RobertoPrevato/PythonCLI/workflows/Build/badge.svg)

# Python CLI project template
Python project template for CLI using [click](https://click.palletsprojects.com).

* [pytest](https://docs.pytest.org/en/latest/)
* [flake8](https://pypi.org/project/flake8/)
* [black](https://github.com/psf/black) ⚫
* [mypy](http://mypy-lang.org)
* [GitHub build workflow](https://help.github.com/en/actions/building-and-testing-code-with-continuous-integration/about-continuous-integration)
* [Makefile](https://www.gnu.org/software/make/manual/make.html)
* [setup.py starter file](https://docs.python.org/3/distutils/setupscript.html)
* [click](https://click.palletsprojects.com)
* [VS Code project code-workspace](https://code.visualstudio.com)

## Getting started

```
# create Python virtual environment
python -m venv venv

# activate environment (Linux):
source venv/bin/activate

# activate environment (Windows):
venv\Scripts\activate

# install dependencies
pip install -r requirements.txt
```

## Install in development mode
To test the CLI during development, install it in edit mode:

```
pip install -e .
```

Then, use the CLI with:

```
foo
```

## Makefile

```
# run tests:
make test

# run tests and write test coverage output
mate testcov
```

Manual releases:

```
# install dependencies for twine (once)
make prepforbuild

# create distribution package
make artifacts

# upload to the test pypi
make testrelease

# upload to pypi
make release
```

## Formatting with black
```
black .
```
