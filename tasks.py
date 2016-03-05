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

from rituals.easy import task, Collection, pushd
from rituals.util import antglob, notify
from rituals.acts.documentation import namespace as _docs


@task(help=dict(
    venv="Include an existing virtualenv (in '.venv')",
    extra="Any extra patterns, space-separated and possibly quoted",
))
def clean(ctx, venv=False, extra=''):
    """Perform house-keeping."""
    notify.banner("Cleaning up project files")

    # Add patterns based on given parameters
    venv_dirs = ['.venv']
    patterns = ['hovercraft-presentation-slides/', 'pip-selfcheck.json', '**/*~']
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
    with pushd('hovercraft-presentation-slides'):
        assert os.path.exists('README.rst'), "README is created"


namespace = Collection.from_module(sys.modules[__name__], name='')
namespace.add_collection(_docs)
