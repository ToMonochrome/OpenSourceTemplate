# OpenSourceStructure

A [cookiecutter](https://cookiecutter.readthedocs.io/) starter template that shows
how to run a new open source Python project: **uv** for dependency management,
**Make** for everyday commands, and **GitHub Actions** for continuous integration.

## Create a new project from this template

```bash
# Interactive prompts
cookiecutter gh:ToMonochrome/OpenSourceStructure

# Or non-interactively
cookiecutter gh:ToMonochrome/OpenSourceStructure \
  project_name="Cookie Bakery" \
  github_username="your-username" \
  author_name="Your Name" \
  author_email="you@example.com" \
  license=MIT
```

This renders a complete project in a new directory:

```
cookie-bakery/
├── .github/workflows/ci.yml   # GitHub Actions: test matrix + lint
├── src/cookie_bakery/          # import package (src layout)
├── tests/                      # pytest suite
├── Makefile                    # make sync / test / lint / check
├── pyproject.toml              # uv-managed project metadata
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE                     # rendered from your license choice
└── README.md
```

Then get to work:

```bash
cd cookie-bakery
make check   # uv sync + ruff + pytest
```

## Template options

| Option | Choices / example | Default |
| --- | --- | --- |
| `project_name` | `Cookie Bakery` | `My Open Source Project` |
| `project_slug` | derived from name, e.g. `cookie-bakery` | — |
| `package_name` | derived from slug, e.g. `cookie_bakery` | — |
| `python_version` | `3.10`, `3.11`, `3.12`, `3.13` | `3.12` |
| `license` | `MIT`, `Apache-2.0`, `BSD-3-Clause`, `GPL-3.0-only`, `Proprietary` | `MIT` |
| `use_github_actions` | `yes`, `no` | `yes` |
| `github_username`, `author_name`, `author_email`, `version` | free text | — |

The generated CI tests every Python version from your chosen minimum up to 3.13.

## Developing this template

This repository is itself managed with uv and Make:

```bash
make sync            # install dev dependencies (cookiecutter, pytest, ruff)
make test            # render the template in tests and assert the output
make template-test   # dogfood: render the template and run the generated tests
make check           # lint + tests
```

CI (`.github/workflows/ci.yml`) runs the same checks on every push and pull
request, plus a dogfood job that scaffolds a project from the template and runs
its test suite.

## License

[MIT](LICENSE)
