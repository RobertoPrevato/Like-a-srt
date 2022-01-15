.PHONY: release test


artifacts: test
	python setup.py sdist bdist_wheel


prepforbuild:
	pip install --upgrade twine setuptools wheel


testrelease:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*


release:
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*


testcov:
	pytest --cov-report html --cov=likeasrt tests/


test:
	flake8 && pytest -v -W ignore


lint: check-flake8 check-isort check-black

format:
	@flake8 . 2>&1
	@isort . 2>&1
	@black . 2>&1

check-flake8:
	@echo "$(BOLD)Checking flake8$(RESET)"
	@flake8 . 2>&1


check-isort:
	@echo "$(BOLD)Checking isort$(RESET)"
	@isort --check-only . 2>&1


check-black:  ## Run the black tool in check mode only (won't modify files)
	@echo "$(BOLD)Checking black$(RESET)"
	@black --check . 2>&1
