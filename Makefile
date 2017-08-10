test:
	nosetests

lint:
	pylint3 calcsolver/*.py

lint_tests:
	pylint3 --disable=import-error,missing-docstring tests/*.py
