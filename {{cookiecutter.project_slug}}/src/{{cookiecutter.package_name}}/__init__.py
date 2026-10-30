"""{{ cookiecutter.project_description }}"""

__version__ = "{{ cookiecutter.version }}"

from {{ cookiecutter.package_name }}.core import greet

__all__ = ["__version__", "greet"]
