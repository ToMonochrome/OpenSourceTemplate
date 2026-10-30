"""Render the template and run the generated project's own test suite.

This proves end-to-end that a freshly scaffolded project installs with uv and
passes its tests. Skipped automatically when uv is unavailable (e.g. restricted
CI sandboxes).
"""

import shutil
import subprocess
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter

REPO_ROOT = Path(__file__).resolve().parent.parent

pytestmark = pytest.mark.skipif(
    shutil.which("uv") is None, reason="uv is not installed"
)


def test_generated_project_passes_its_own_tests(tmp_path):
    project = Path(
        cookiecutter(
            str(REPO_ROOT),
            no_input=True,
            extra_context={
                "project_name": "Dogfood Project",
                "project_slug": "dogfood-project",
                "package_name": "dogfood_project",
                "project_description": "Rendered copy of the template.",
                "author_name": "CI",
                "author_email": "ci@example.com",
                "github_username": "ci-bot",
                "version": "0.1.0",
                "python_version": "3.12",
                "license": "MIT",
                "use_github_actions": "yes",
            },
            output_dir=str(tmp_path),
        )
    )
    subprocess.run(["uv", "sync"], cwd=project, check=True)
    result = subprocess.run(
        ["uv", "run", "pytest", "-v"],
        cwd=project,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "3 passed" in result.stdout
