{% macro section(title, level='=') -%}
{{ title }}
{% for _ in title %}{{ level }}{% endfor %}
{%- endmacro -%}
{{ section(cookiecutter.project_name) }}

Introduction
------------

This is a project for a slide deck, which uses `reStructuredText`_
markup to create `impress.js`_ presentations via the Python3 tool `Hovercraft!`_.


Installation
------------

To create a working directory for this project, call these commands::

    git clone "{{ cookiecutter.github_url }}.git"
    cd "{{ cookiecutter.repo_name }}"
    . .env --yes
    invoke view

Python3 and ``pyvenv`` must be available for this to work.


Usage
-----

You can call the following tasks via ``invoke``.

======= =====================================================================
Task    Description
======= =====================================================================
clean   Perform house-keeping.
html    Build HTML tree.
pdf     Build PDF slide show.
thumbs  Create slide show thumbnails.
view    Start live-reload watchdog.
======= =====================================================================

Note that ``invoke view`` starts a watchdog process that will react to any
changes in ``*.rst`` files by rendering and reloading the open browser tab (*live reload*).

The ``pdf`` task needs `deck2pdf`_ installed, and ``thumbs`` additionally requires *ImageMagick*
(usually available via your operating system's packages).


.. _`deck2pdf`: https://github.com/melix/deck2pdf
.. _`impress.js`: https://github.com/impress/impress.js
.. _`reStructuredText`: http://docutils.sourceforge.net/rst.html
.. _`Hovercraft!`: https://hovercraft.readthedocs.org/
