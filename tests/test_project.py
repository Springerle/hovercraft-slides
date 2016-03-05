# *- coding: utf-8 -*-
# pylint: disable=missing-docstring, bad-continuation
""" Test the template.
"""
from __future__ import absolute_import, unicode_literals

import io
import os


def test_project_basedir_was_created(project):
    assert os.path.exists(project), "Project was created"
    assert os.path.isdir(project), "Project base directory was created"


def test_readme_has_github_url_and_newline_at_end(project):
    with io.open(project + '/README.rst', encoding='utf-8') as handle:
        readme = handle.read()

    # TODO: cookiecutter needs a --no-rc option, so we'll always get 'jschmoe'
    assert any("https://github.com/{}/{}".format(i, os.path.basename(project)) in readme
        for i in ('jschmoe', 'jhermann')), "README contains repo URL"
    assert readme.endswith('\n'), "README has the newline at end of file"
