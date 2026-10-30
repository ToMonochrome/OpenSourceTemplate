import pytest

from {{ cookiecutter.package_name }} import greet


def test_greet_basic():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_strips_whitespace():
    assert greet("  Grace  ") == "Hello, Grace!"


def test_greet_empty_raises():
    with pytest.raises(ValueError, match="must not be empty"):
        greet("   ")
