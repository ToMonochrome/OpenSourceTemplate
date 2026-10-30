# Contributing

1. Fork and create a feature branch from `main`.
2. `make sync` to set up your environment.
3. Change the template under `{{cookiecutter.project_slug}}/` or the meta
   tests under `tests/`.
4. `make check` must pass (ruff + pytest, including the dogfood test that
   renders the template and runs the generated project's tests).
5. Open a pull request.
