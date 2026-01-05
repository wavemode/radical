test:
	uv run python -m unittest discover -s src

lint:
	uv run ruff check --fix --unsafe-fixes src

format:
	uv run ruff format src

.PHONY: test lint format
