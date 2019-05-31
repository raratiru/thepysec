#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : thepysec/john/tests/test_version.py
#
#       Creation Date : Sun 30 Dec 2018 05:32:03 PM EET
#
#       Last Modified : Sat 16 Mar 2019 04:07:54 PM EET (16:07)
#
# ==============================================================================

import re
import pytest
from thepysec import VERSION
from thepysec.john.version import (
    get_complete_version,
    get_docs_version,
    get_git_changeset,
    get_version,
    get_version_tuple,
)
from unittest import mock


def test_version():
    VERSION = (0, 0, 0, "dev", 0)
    with pytest.raises(AssertionError):
        get_version(VERSION)


def test_development():
    ver_tuple = (1, 4, 0, "alpha", 0)
    # This will return a different result when it's run within or outside
    # of a git clone: 1.4.devYYYYMMDDHHMMSS or 1.4.
    ver_string = get_version(ver_tuple)
    assert re.match(r"1\.4(\.dev[0-9]+)?", ver_string)


@pytest.mark.parametrize(
    "ver_tuple, ver_string",
    [
        ((1, 4, 0, "alpha", 1), "1.4a1"),
        ((1, 4, 0, "beta", 1), "1.4b1"),
        ((1, 4, 0, "rc", 1), "1.4rc1"),
        ((1, 4, 0, "final", 0), "1.4"),
        ((1, 4, 1, "rc", 2), "1.4.1rc2"),
        ((1, 4, 1, "final", 0), "1.4.1"),
    ],
)
def test_releases(ver_tuple, ver_string):
    assert get_version(ver_tuple) == ver_string


@pytest.mark.parametrize(
    "ver_tuple, ver_string",
    [(("1.2.3"), (1, 2, 3)), (("1.2.3b2"), (1, 2, 3)), (("1.2.3b2.dev0"), (1, 2, 3))],
)
def test_get_version_tuple(ver_tuple, ver_string):
    assert get_version_tuple(ver_tuple) == ver_string


def test_complete_version():
    assert get_complete_version((0, 0, 0, "alpha", 0)) == (0, 0, 0, "alpha", 0)
    assert get_complete_version() == VERSION


def test_docs_dev():
    assert get_docs_version((0, 0, 0, "alpha", 0)) == "dev"


def test_docs_prod():
    assert get_docs_version((2, 3, 0, "final", 0)) == "2.3"


@mock.patch("thepysec.john.version.subprocess.Popen")
def test_git_changeset_is_none(mock_popen):
    process_mock = mock.Mock()
    attrs = {"communicate.return_value": (str(), "error")}  # Set the result to ''
    process_mock.configure_mock(**attrs)
    mock_popen.return_value = process_mock
    get_git_changeset.cache_clear()  # Clear cache to call mock
    result = get_git_changeset()
    assert result is None
    ver_tuple = (1, 4, 0, "alpha", 0)
    ver_string = get_version(ver_tuple)
    assert ver_string == "1.4"
