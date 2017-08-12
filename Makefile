test:
	nosetests

lint: lint_calcsolver lint_tests

lint_calcsolver:
	@echo "\n***** Linting calcsolver directory *****\n"
	@pylint3 -f colorized -r n calcsolver/*.py
lint_tests:
	@echo "\n***** Linting tests directory *****\n"
	@pylint3 -f colorized -r n --disable=import-error,missing-docstring tests/*.py
