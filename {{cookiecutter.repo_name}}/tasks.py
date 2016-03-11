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
import webbrowser

from rituals.easy import task, Collection, pushd
from rituals.util import antglob, notify
from rituals.acts.basic import help

BASEDIR = os.path.dirname(__file__)


@task(help=dict(
    venv="Include an existing virtualenv (in '.' or in '.venv')",
    extra="Any extra patterns, space-separated and possibly quoted",
))
def clean(_dummy_ctx, venv=False, extra=''):
    """Perform house-keeping."""
    notify.banner("Cleaning up project files")

    # Add patterns based on given parameters
    venv_dirs = ['bin', 'include', 'lib', 'share', 'local', '.venv']
    patterns = ['_html/', 'pip-selfcheck.json']
    excludes = ['.git/', '.hg/', '.svn/']
    if venv:
        patterns.extend([i + '/' for i in venv_dirs])
    if extra:
        patterns.extend(shlex.split(extra))

    # Build fileset
    patterns = [antglob.includes(i) for i in patterns] + [antglob.excludes(i) for i in excludes]
    if not venv:
        # Do not scan venv dirs when not cleaning them
        patterns.extend([antglob.excludes(i + '/') for i in venv_dirs])
    fileset = antglob.FileSet(BASEDIR, patterns)

    # Iterate over matches and remove them
    for name in fileset:
        notify.info('rm {0}'.format(name))
        if name.endswith('/'):
            shutil.rmtree(os.path.join(BASEDIR, name))
        else:
            os.unlink(os.path.join(BASEDIR, name))


@task(help={
    'browse': "Open slides in a new browser tab",
})
def preview(ctx, browse=False):
    """Start live-reload watchdog."""
    # TODO: Actually start watchdog
    index_url = '_html/index.html'

    # Open in browser?
    if browse:
        webbrowser.open_new_tab(index_url)


@task(help={
    'browse': "Open slides in a new browser tab",
})
def html(ctx, browse=False):
    """Build HTML tree."""
    index_url = '_html/index.html'
    ctx.run("hovercraft -t simple --skip-notes index.rst {}".format(os.path.dirname(index_url)))

    # Open in browser?
    if browse:
        webbrowser.open_new_tab(index_url)


namespace = Collection.from_module(sys.modules[__name__], name='')
