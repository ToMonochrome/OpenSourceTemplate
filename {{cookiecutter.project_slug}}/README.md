# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Getting started

This project uses [uv](https://docs.astral.sh/uv/) for dependency and environment
management. The fastest way to get going is with `make`:

```bash
make sync   # create .venv and install all dependencies
make test   # run the test suite
make lint   # ruff lint + format check
make check  # lint + tests
```

Or with uv directly:

```bash
uv sync
uv run pytest
uv run {{ cookiecutter.package_name }} Ada
```

## Development

- Tests live in `tests/` and run with `pytest`.
- Code is linted and formatted with `ruff` (`make format` to auto-fix).
- Continuous integration runs in GitHub Actions on every push and pull request
  (see `.github/workflows/ci.yml`).

## License

Licensed under the {{ cookiecutter.license }} license. See [LICENSE](LICENSE).
