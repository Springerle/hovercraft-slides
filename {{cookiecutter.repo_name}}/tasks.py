# *- coding: utf-8 -*-
# pylint: disable=locally-disabled, bad-continuation
# pylint: disable=wildcard-import, unused-import, unused-wildcard-import
# pylint: disable=superfluous-parens, redefined-builtin
""" Project automation for Invoke.
"""

import os
import sys
import time
import shlex
import shutil
import subprocess
import webbrowser

from rituals.easy import task, Collection, pushd
from rituals.util import antglob, notify
from rituals.util.which import which, WhichError
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
    'clean': "Start with a clean build area",
    'opts': "Extra flags for Hovercraft",
})
def view(ctx, browse=False, clean=False, opts=''):
    """Start live-reload watchdog."""
    def activity(what=None, i=None):
        "Helper"
        if i is None:
            sys.stdout.write(what + '\n')
        else:
            sys.stdout.write(' {}  Waiting for {}\r'.format(r'\|/-'[i % 4], what or 'something'))
        sys.stdout.flush()

    index_file = '_html/index.html'
    if clean:
        ctx.run("invoke clean")
    elif os.path.exists(index_file):
        os.remove(index_file)

    # Assuming that your browser has a live-reload plugin
    cmd = ('''watchmedo shell-command'''
           ''' --command="hovercraft {opts} index.rst {htmldir}" '''
           ''' --patterns="*.rst"'''
           ''' {basedir} &'''
           .format(opts=opts, htmldir=os.path.dirname(index_file), basedir='.'))
    subprocess.call(cmd, shell=True)

    for i in range(60):
        activity('HTML index file', i)
        if os.path.exists(index_file):
            activity('OK')
            break
        time.sleep(1)
        # trigger first build
        os.utime(os.path.join(BASEDIR, 'README.rst'), None)
    else:
        activity('ERR')

    # Open in browser
    webbrowser.open_new_tab(index_file)


@task(help={
    'browse': "Open slides in a new browser tab",
})
def html(ctx, browse=False):
    """Build HTML tree."""
    index_file = '_html/index.html'
    ctx.run("hovercraft -t simple --skip-notes index.rst {}".format(os.path.dirname(index_file)))

    # Open in browser?
    if browse:
        webbrowser.open_new_tab(index_file)


@task(help={
    'open': "Open the generated PDF",
})
def pdf(ctx, open=False):
    """Build PDF slide show."""
    try:
        which("deck2pdf")
    except WhichError:
        notify.failure("You need to install 'deck2pdf' from https://github.com/melix/deck2pdf")
    ctx.run("invoke html")
    ctx.run("deck2pdf --profile=impressjs _html/index.html slides.pdf")
    if open:
        ctx.run("xdg-open slides.pdf &", pty=False)


@task(help={
    'open': "Open the generated image",
    'width': "Width of a single slide in pixels",
})
def thumbs(ctx, open=False, width=480):
    """Create slide show thumbnails."""
    ctx.run("invoke pdf")
    ctx.run("montage -density 300 slides.pdf -mode Concatenate -tile 2x999 -quality 80 -resize {} slides.jpg".format(width))
    if open:
        ctx.run("xdg-open slides.jpg &", pty=False)


# Add local tasks to root namespace
namespace = Collection.from_module(sys.modules[__name__], name='')
