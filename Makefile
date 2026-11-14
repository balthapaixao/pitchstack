.DEFAULT_GOAL := help
.PHONY: help setup lint test

help: ## Show the available targets
	@awk 'BEGIN {FS = ":.*## "} /^[a-zA-Z_-]+:.*## / {printf "  %-8s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: ## Create the virtualenv and install the locked dependencies
	uv sync

lint: ## Run the ruff linter and the formatting check
	uv run ruff check . && uv run ruff format --check .

test: ## Run the test suite
	uv run pytest -q
