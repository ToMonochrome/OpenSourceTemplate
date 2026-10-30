.PHONY: help install sync test lint format check template-test clean

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

install: ## Check that uv is installed
	@command -v uv >/dev/null 2>&1 || { echo "uv is required: https://docs.astral.sh/uv/"; exit 1; }

sync: install ## Create the venv and install all dependencies
	uv sync

test: sync ## Run the template test suite
	uv run pytest -v

template-test: sync ## Render the template and run the generated project's tests (dogfood)
	uv run pytest -v tests/test_dogfood.py

lint: sync ## Lint with ruff
	uv run ruff check .
	uv run ruff format --check .

format: sync ## Auto-format with ruff
	uv run ruff check --fix .
	uv run ruff format .

check: lint test ## Run lint and tests

clean: ## Remove build/test artifacts
	rm -rf .venv dist build *.egg-info .pytest_cache .ruff_cache htmlcov .coverage uv.lock
