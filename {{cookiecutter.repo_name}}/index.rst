{% macro section(title, level='=') -%}
{{ title }}
{% for _ in title %}{{ level }}{% endfor %}
{%- endmacro -%}
:title: {{ cookiecutter.project_name }}
:author: {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
:description: Copyright (c) {{ cookiecutter.year }}
:keywords: slides, impress.js
:auto-console: false
:skip-help: true
:css: css/default.css

----

:class: bullet-hand

{{ section(cookiecutter.project_name) }}

**{{ cookiecutter.full_name }} <{{ cookiecutter.email }}>**

Agenda
------

- Show example `Hovercraft!`_ slides
- Present built-in styling options


----

:class: bullet-star

Bullet Styles
=============

- Bullet points cause *PowerPoint Poisoning*
- … but we use them anyway

.. break

- Styling top-level bullets

  - use ``:class: bullet-STYLE`` on the slide
  - ``bullet-checkmark``, ``bullet-arrow``, ``bullet-hand``, or ``bullet-star``

.. break

- To add spacing between bullets, add a *reStructuredText* comment:

    ::

        .. break


----

Centered Images
===============

(leave out the title for image-only slides)

.. image:: img/python-powered.png
   :width: 720px
   :class: centered


----

Floating Images
===============

.. image:: img/python-powered.png
   :width: 480px
   :class: float-right

- Eye-candy can sweeten bullet points
- Use ``:class: float-right`` on an image
- The image floats to the right of any content following it


----

Code Blocks
===========

.. code-block:: python
    :class: small

    @task(help={
        'browse': "Open slides in a new browser tab",
    })
    def html(ctx, browse=False):
        """Build HTML tree."""
        index_file = '_html/index.html'
        ctx.run("hovercraft -t simple --skip-notes index.rst {}"
                .format(os.path.dirname(index_file)))

        # Open in browser?
        if browse:
            webbrowser.open_new_tab(index_file)


----

:class: bullet-arrow

Credits
=======

.. image:: img/python-powered.png
   :width: 240px
   :class: float-right

- Powered by `Hovercraft!`_

.. break

- Hovercraft! logo – https://github.com/regebro/hovercraft/
- Python logo – https://www.python.org/community/logos/

.. _`Hovercraft!`: http://hovercraft.readthedocs.org/
