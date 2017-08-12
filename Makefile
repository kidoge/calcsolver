test:
	nosetests

lint: lint_calcsolver lint_tests

lint_calcsolver:
	@echo "\n***** Linting calcsolver directory *****\n"
	@if [ -z "${VERBOSE}" ]; then \
		pylint3 calcsolver/*.py | tail -n 4; \
	else \
		pylint3 calcsolver/*.py; \
	fi

lint_tests:
	@echo "\n***** Linting tests directory *****\n"
	@if [ -z "${VERBOSE}" ]; then \
		pylint3 --disable=import-error,missing-docstring tests/*.py | tail -n 4; \
	else \
		pylint3 --disable=import-error,missing-docstring tests/*.py; \
	fi
