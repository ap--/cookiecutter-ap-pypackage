# cookiecutter-ap-python-package

:wave: Hello! This is my cookiecutter template for python packages. It's 
going to be a moving target and be adopted to how I like to write python 
packages.

## :warning: :dragon: Here be dragons :dragon: :warning:

This is an early release, made for me to keep track of things. So expect it to
break. If you plan to rely on this package let me know. I will then accommodate
your use case and tag the repo.
If there are any questions open an issue, and I'll do my best to help! 

## ADRs

Currently, I am the only consumer of this cookiecutter. That means of course 
that all the decisions made in here are opinionated. That being said, please 
feel free to open issues or discussions if you think something could be 
improved or if it would be nice if it would be supported.

#### versioning: `setuptools_scm`

Options would have been `setuptools_scm`, `versioneer` and `bumpversion`. I 
prefer `setuptools_scm`. It integrates nicely with the default `setuptools` 
install and it's maintained by pypa, so at least it'll be supported for a 
reasonable timeframe.

#### tests: `pytest`

Tests are run via `pytest`. Could have also gone for plain `unittest` but I 
prefer `pytest`'s fixture model.

#### dependencies/requirements: `setup.cfg pep508` and `conda-devenv`

Two requirements to consider for dependency management. We could only rely 
on `pipenv` to allow creating environments reproducibly, but since most of 
the tooling I create requires loads of binary dependencies, I mainly rely on 
`conda`. More specifically on `conda-devenv` to make everything a bit 
simpler to configure. I still provide dependency requirements in `setup.cfg` 
for direct installation via `pip`.
