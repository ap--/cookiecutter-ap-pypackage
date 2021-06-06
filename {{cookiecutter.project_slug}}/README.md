# {{cookiecutter.project_slug}}

{% set ghusr = cookiecutter.github_username -%}
{%- set ghproj = cookiecutter.project_slug -%}
{%- set ghusrproj = cookiecutter.github_username + "/" + cookiecutter.project_slug -%}
[![PyPI Version](https://img.shields.io/pypi/v/{{ghproj}})](https://pypi.org/project/{{ghproj}}/)
[![Read the Docs](https://img.shields.io/readthedocs/{{ghproj}})](https://{{ghproj}}.readthedocs.io)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/{{ghusr}}/{{ghproj}}/{{ghproj}}?label=tests)](https://github.com/{{ghusr}}/{{ghproj}}/actions)
[![Codecov](https://img.shields.io/codecov/c/github/{{ghusr}}/{{ghproj}})](https://codecov.io/gh/{{ghusr}}/{{ghproj}})
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ghproj}})](https://github.com/{{ghusr}}/{{ghproj}})
[![GitHub issues](https://img.shields.io/github/issues/{{ghusr}}/{{ghproj}})](https://github.com/{{ghusr}}/{{ghproj}}/issues)

{{ cookiecutter.project_short_description }}

## Documentation

You can find `{{cookiecutter.project_slug}}`'s documentation at
[{{cookiecutter.project_slug}}.readthedocs.io](https://{{cookiecutter.project_slug}}.readthedocs.io) :heart:

## Development Installation

1. Install conda and git
2. Clone {{cookiecutter.project_slug}} `git clone https://github.com/{{ghusrproj}}.git`
3. Run `conda env create -f environment.yaml`
4. Activate the environment `conda activate {{cookiecutter.conda_env}}`

Note that in this environment `{{cookiecutter.project_slug}}` is already installed in development mode,
so go ahead and hack.
