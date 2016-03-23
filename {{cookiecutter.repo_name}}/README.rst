{{ cookiecutter.project_name }}
===============================

 |Travis CI|  |GitHub Issues|  |License|


Introduction
------------

Usage
-----

Installation
------------

*{{ cookiecutter.project_name }}* can be used…

As an author, to create a working directory for this project, call these commands::

    git clone "{{ cookiecutter.github_url }}.git"
    cd "{{ cookiecutter.repo_name }}"
    . .env --yes --develop
    invoke watchdog -b

Python3 and ``pyvenv`` must be available for this to work.


.. |Travis CI| image:: https://api.travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
.. |GitHub Issues| image:: https://img.shields.io/github/issues/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
    :target: {{ cookiecutter.github_url }}/issues
.. |License| image:: https://img.shields.io/pypi/l/{{ cookiecutter.repo_name }}.svg
    :target: {{ cookiecutter.github_url }}/blob/master/LICENSE
