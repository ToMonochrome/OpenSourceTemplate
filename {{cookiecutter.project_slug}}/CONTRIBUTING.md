# Contributing to {{ cookiecutter.project_name }}

Thanks for your interest in contributing!

## Workflow

1. Fork the repository and create a feature branch from `main`.
2. Set up your environment: `make sync`
3. Make your changes, with tests in `tests/`.
4. Run `make check` — lint and tests must pass.
5. Open a pull request describing what and why.

## Code style

- Formatting and linting are enforced by `ruff` (`make lint`, `make format`).
- All CI checks run on every pull request and must pass before merge.

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).
