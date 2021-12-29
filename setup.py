#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from setuptools import setup, find_packages

version = __import__("thepysec").get_version()


def read(fname):
    with open(path.join(path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name="thepysec",
    version=version,
    python_requires=">=3.6",
    description="Python secretaries you call at will, for instant py-relief.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/raratiru/thepysec",
    author="Raratiru",
    author_email="info@musicaloffering.gr",
    license="BSD 3-Clause License",
    packages=find_packages(exclude=("tests", "docs")),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov", "psycopg2-binary"],
    extras_require={"dev": ["pytest", "pytest-cov", "ipdb", "psycopg2-binary"]},
    install_requires=["unidecode"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
