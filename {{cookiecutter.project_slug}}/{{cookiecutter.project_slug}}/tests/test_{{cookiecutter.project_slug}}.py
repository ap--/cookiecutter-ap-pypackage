import pytest

from {{cookiecutter.project_slug}}.{{cookiecutter.project_slug}} import complicated_calculation


def test_complicated_calculation():
    assert complicated_calculation() == "Hello World!"
