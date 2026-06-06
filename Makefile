.PHONY: install dev test lint doctor

install:
	python -m pip install -e .

dev:
	python -m pip install -e ".[dev]"

test:
	python -m pytest tests/ -q

lint:
	python -m ruff check src tests

doctor:
	qgrapho doctor
