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
#from rituals.acts.documentation import namespace as _docs


@task(help={
    'browse': "Open slides in a new browser tab",
})
def watchdog(ctx, browse=False):
    """Start live-reload watchdog."""
    # TODO: Actually start watchdog
    index_url = '_html/index.html'

    # Open in browser?
    if browse:
        webbrowser.open_new_tab(index_url)


namespace = Collection.from_module(sys.modules[__name__], name='')
#namespace.add_collection(_docs)
