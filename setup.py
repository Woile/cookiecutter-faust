#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" setup.py for cookiecutter-faust."""

from setuptools import setup

__version__ = "0.1.0"

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
    name="cookiecutter-faust",
    version=__version__,
    description="A Cookiecutter template for creating Faust projects quickly.",
    long_description=long_description,
    author="Marcos Schroh",
    author_email="schrohm@gmail.com",
    url="",
    download_url="",
    packages=[],
    include_package_data=True,
    license='GPLv3',
    classifiers=[
        "Framework :: Faust :: 1.5.4",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development",
    ],
    keywords=(
        """
        cookiecutter, Python, projects, project templates, faust,
        skeleton, scaffolding, project directory, setup.py
        """
    ),
)
