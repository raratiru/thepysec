#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : setup.py
#
#       Creation Date : Fri 28 Dec 2018 03:17:42 PM EET
#
#       Last Modified : Sat 26 Oct 2019 09:47:24 PM EEST (21:47)
#
# ==============================================================================

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
    url="https://github.com/raratiru/thepysec",
    author="Raratiru",
    author_email="welcome@rara.gr",
    license="gpl-3.0",
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
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
