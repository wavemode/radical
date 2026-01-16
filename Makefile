test:
	uv run python -m unittest discover -s src/test

lint:
	uv run ruff check --fix --unsafe-fixes src scripts

format:
	uv run ruff format src scripts

typecheck:
	uv run ty check src scripts

check: lint format typecheck

.PHONY: test lint format typecheck check
