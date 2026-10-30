import re
import sys

PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
PACKAGE_NAME = "{{ cookiecutter.package_name }}"
PYTHON_VERSION = "{{ cookiecutter.python_version }}"

SLUG_REGEX = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")
PACKAGE_REGEX = re.compile(r"^[a-z][a-z0-9_]*$")
SUPPORTED_PYTHON_VERSIONS = ("3.10", "3.11", "3.12", "3.13")

if not SLUG_REGEX.match(PROJECT_SLUG):
    sys.exit(
        f"ERROR: project_slug '{PROJECT_SLUG}' is invalid. Use lowercase letters, "
        "digits and single hyphens, starting with a letter (e.g. 'my-project')."
    )

if not PACKAGE_REGEX.match(PACKAGE_NAME):
    sys.exit(
        f"ERROR: package_name '{PACKAGE_NAME}' is invalid. Use a Python identifier "
        "starting with a lowercase letter (e.g. 'my_project')."
    )

if PYTHON_VERSION not in SUPPORTED_PYTHON_VERSIONS:
    sys.exit(
        f"ERROR: python_version '{PYTHON_VERSION}' is not supported. "
        f"Choose one of: {', '.join(SUPPORTED_PYTHON_VERSIONS)}."
    )
