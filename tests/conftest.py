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


# Globally available fixtures
@pytest.fixture(scope='session')
def project():
    """ Materialize cookiecutter template (once).

        The fixture contains the abspath of the created workdir.
    """
    new_workdir = 'hovercraft-presentation-slides'

    if os.path.exists(new_workdir):
        shutil.rmtree(new_workdir)
    subprocess.check_call(['cookiecutter', '--no-input', '.'])

    return os.path.abspath(new_workdir)


@pytest.fixture(scope='session')
def logger():
    """Test logger instance as a fixture."""
    logging.basicConfig(level=logging.DEBUG)
    return logging.getLogger('tests')
