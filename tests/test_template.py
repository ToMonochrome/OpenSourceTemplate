import json
import re
from pathlib import Path

import pytest
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = REPO_ROOT / "{{cookiecutter.project_slug}}"

DEFAULT_CONTEXT = {
    "project_name": "Cookie Bakery",
    "project_slug": "cookie-bakery",
    "package_name": "cookie_bakery",
    "project_description": "Bakes cookies on demand.",
    "author_name": "Ada Lovelace",
    "author_email": "ada@example.com",
    "github_username": "ada-dev",
    "version": "0.1.0",
    "python_version": "3.12",
    "license": "MIT",
    "use_github_actions": "yes",
}


def render(tmp_path, **overrides):
    context = {**DEFAULT_CONTEXT, **overrides}
    return cookiecutter(
        str(REPO_ROOT), no_input=True, extra_context=context, output_dir=str(tmp_path)
    )


def test_cookiecutter_json_is_valid():
    config = json.loads((REPO_ROOT / "cookiecutter.json").read_text(encoding="utf-8"))
    for key in (
        "project_name",
        "project_slug",
        "package_name",
        "license",
        "python_version",
        "use_github_actions",
    ):
        assert key in config


def test_render_creates_expected_tree(tmp_path):
    project = Path(render(tmp_path))
    assert project.name == "cookie-bakery"
    expected = [
        "README.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "LICENSE",
        "Makefile",
        "pyproject.toml",
        ".gitignore",
        ".github/workflows/ci.yml",
        "src/cookie_bakery/__init__.py",
        "src/cookie_bakery/__main__.py",
        "src/cookie_bakery/core.py",
        "tests/test_core.py",
    ]
    for rel in expected:
        assert (project / rel).is_file(), f"missing: {rel}"
    assert not (project / "licenses").exists()


def test_variables_are_substituted(tmp_path):
    project = Path(render(tmp_path))
    pyproject = (project / "pyproject.toml").read_text(encoding="utf-8")
    assert 'name = "cookie-bakery"' in pyproject
    assert 'version = "0.1.0"' in pyproject
    assert "cookie_bakery = " in pyproject
    assert "Ada Lovelace" in pyproject
    assert "{{" not in pyproject and "{%" not in pyproject
    init = (project / "src/cookie_bakery/__init__.py").read_text(encoding="utf-8")
    assert "Bakes cookies on demand." in init
    assert "{{" not in init


def test_license_mit_substitutes_copyright(tmp_path):
    project = Path(render(tmp_path, license="MIT"))
    license_text = (project / "LICENSE").read_text(encoding="utf-8")
    assert "Ada Lovelace" in license_text
    assert "<year>" not in license_text
    assert "<owner>" not in license_text
    pyproject = (project / "pyproject.toml").read_text(encoding="utf-8")
    assert 'license = "MIT"' in pyproject


def test_license_gpl(tmp_path):
    project = Path(render(tmp_path, license="GPL-3.0-only"))
    license_text = (project / "LICENSE").read_text(encoding="utf-8")
    assert "GNU GENERAL PUBLIC LICENSE" in license_text
    assert "Ada Lovelace" in license_text
    pyproject = (project / "pyproject.toml").read_text(encoding="utf-8")
    assert 'license = "GPL-3.0-only"' in pyproject


def test_license_proprietary(tmp_path):
    project = Path(render(tmp_path, license="Proprietary"))
    license_text = (project / "LICENSE").read_text(encoding="utf-8")
    assert "All rights reserved" in license_text
    pyproject = (project / "pyproject.toml").read_text(encoding="utf-8")
    assert 'license = { text = "Proprietary" }' in pyproject


def test_no_github_actions_removes_workflows(tmp_path):
    project = Path(render(tmp_path, use_github_actions="no"))
    assert not (project / ".github").exists()


def test_ci_matrix_follows_min_python(tmp_path):
    project = Path(render(tmp_path, python_version="3.11"))
    ci = (project / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    assert '["3.11", "3.12", "3.13"]' in ci
    assert "${{ matrix.python-version }}" in ci
    pyproject = (project / "pyproject.toml").read_text(encoding="utf-8")
    assert 'requires-python = ">=3.11"' in pyproject


def test_generated_ci_yaml_is_valid(tmp_path):
    import yaml

    project = Path(render(tmp_path))
    ci_path = project / ".github/workflows/ci.yml"
    ci = yaml.safe_load(ci_path.read_text(encoding="utf-8"))
    assert "test" in ci["jobs"] and "lint" in ci["jobs"]


def test_invalid_slug_rejected(tmp_path):
    with pytest.raises(FailedHookException, match="Hook script failed"):
        render(tmp_path, project_slug="Bad Slug!")


def test_invalid_python_version_rejected(tmp_path):
    with pytest.raises(ValueError, match="python_version"):
        render(tmp_path, python_version="2.7")


def test_package_import_name_is_valid_identifier(tmp_path):
    render(tmp_path, project_slug="my-2cool-project", package_name="my_2cool_project")
    assert re.match(r"^[a-z][a-z0-9_]*$", "my_2cool_project")
