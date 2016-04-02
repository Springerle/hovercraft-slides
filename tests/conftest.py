# -*- coding: utf-8 -*-
# pylint: disable=
""" py.test dynamic configuration.

    For details needed to understand these tests, refer to:
        https://pytest.org/
        http://pythontesting.net/start-here/
"""
from __future__ import absolute_import, unicode_literals

import os
import shutil
import logging
import subprocess

import pytest


TEST_FOLDER = 'present-with-hovercraft-slides'


# Globally available fixtures
@pytest.fixture(scope='session')
def project():
    """ Materialize cookiecutter template (once).

        The fixture contains the abspath of the created workdir.
    """
    if os.path.exists(TEST_FOLDER):
        shutil.rmtree(TEST_FOLDER)
    subprocess.check_call(['cookiecutter', '--no-input', '.'])

    return os.path.abspath(TEST_FOLDER)


@pytest.fixture(scope='session')
def logger():
    """Test logger instance as a fixture."""
    logging.basicConfig(level=logging.DEBUG)
    return logging.getLogger('tests')
