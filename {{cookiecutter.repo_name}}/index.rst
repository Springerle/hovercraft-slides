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

- Show example `Hovercraft`_ slides
- Present built-in styling options


----

:class: bullet-star

Bullet Styles
=============

- Bullet points cause *PowerPoint Poisoning*
- … but we use them anyway

- Styling top-level bullets

  - use ``:class: bullet-STYLE`` on the slide
  - ``bullet-checkmark``, ``bullet-arrow``, ``bullet-hand``, or ``bullet-star``


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


.. _`Hovercraft`: http://hovercraft.readthedocs.org/
