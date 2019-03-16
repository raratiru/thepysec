#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : setup.py
#
#       Creation Date : Fri 28 Dec 2018 03:17:42 PM EET
#
#       Last Modified : Sat 16 Mar 2019 04:09:14 PM EET (16:09)
#
# ==============================================================================

from os import path
from setuptools import setup, find_packages

version = __import__('thepysec').get_version()


def read(fname):
    with open(path.join(path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='thepysec',
    version=version,
    python_requires='>=3.6',
    description='Python secretaries you call at will, for instant py-relief.',
    long_description=read('README.rst'),
    url='https://github.com/raratiru/thepyspec',
    author='Raratiru',
    author_email='welcome@rara.gr',
    license='gpl-3.0',
    packages=find_packages(exclude=('tests', 'docs')),
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov'],
    extras_require={
        'dev': ['pytest', 'pytest-cov', 'ipdb'],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
