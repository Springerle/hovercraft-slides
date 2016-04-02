# *- coding: utf-8 -*-
# pylint: disable=locally-disabled, bad-continuation
# pylint: disable=wildcard-import, unused-import, unused-wildcard-import
# pylint: disable=superfluous-parens, redefined-builtin
""" Project automation for Invoke.
"""

import os
import sys
import shlex
import shutil
import subprocess

from rituals.easy import task, Collection, pushd
from rituals.util import antglob, notify
from rituals.acts.documentation import namespace as _docs

ROOT_FOLDER = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(ROOT_FOLDER, "tests"))
from conftest import TEST_FOLDER


@task(help=dict(
    venv="Include an existing virtualenv (in '.venv')",
    extra="Any extra patterns, space-separated and possibly quoted",
))
def clean(ctx, venv=False, extra=''):
    """Perform house-keeping."""
    notify.banner("Cleaning up project files")

    # Stop any left-over watchdog
    if os.path.exists(TEST_FOLDER):
        ctx.run("cd {} && . .env && inv view --kill".format(TEST_FOLDER))

    # Add patterns based on given parameters
    venv_dirs = ['.venv']
    patterns = [TEST_FOLDER + '/', 'pip-selfcheck.json', '**/*~']
    if venv:
        patterns.extend([i + '/' for i in venv_dirs])
    if extra:
        patterns.extend(shlex.split(extra))

    # Build fileset
    patterns = [antglob.includes(i) for i in patterns]
    if not venv:
        # Do not scan venv dirs when not cleaning them
        patterns.extend([antglob.excludes(i + '/') for i in venv_dirs])
    fileset = antglob.FileSet('.', patterns)

    # Iterate over matches and remove them
    for name in fileset:
        notify.info('rm {0}'.format(name))
        if name.endswith('/'):
            shutil.rmtree(name)
        else:
            os.unlink(name)


@task(pre=[clean])
def test(ctx):
    """Perform integration tests."""
    ctx.run("py.test")
    with pushd(TEST_FOLDER):
        assert os.path.exists('README.rst'), "README is created"
        ctx.run(". .env --yes")

    # Start preview in a clean shell environment
    subprocess.call('''bash -l -c "cd '{}/{}' && . .env && invoke view"'''
                    .format(os.getcwd(), TEST_FOLDER), shell=True)


namespace = Collection.from_module(sys.modules[__name__], name='')
namespace.add_collection(_docs)
