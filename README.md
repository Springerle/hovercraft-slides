# hovercraft-slides

:construction: **In development!** :construction:

A cookiecutter template that creates a
[Hovercraft!](https://hovercraft.readthedocs.org/)
presentation.

 [![Groups](https://img.shields.io/badge/Google_groups-springerle--users-orange.svg)](https://groups.google.com/forum/#!forum/springerle-users)
 [![CC0 licensed](http://img.shields.io/badge/license-CC0-red.svg)](https://raw.githubusercontent.com/Springerle/hovercraft-slides/master/LICENSE)
 [![GitHub Issues](https://img.shields.io/github/issues/Springerle/hovercraft-slides.svg)](https://github.com/Springerle/hovercraft-slides/issues)


## Features

 * Selection of a few standard licences (CC0, …)
 * Default CSS for common styling needs

   * Floating images
   * Image-only slides
   * Styled bullet points


## Usage

To use this template, refer to the
[Cookiecutter documentation](https://cookiecutter.readthedocs.org/en/latest/usage.html)
– it was tested with Cookiecutter 1.4.0.
After you created your new slide project, these commands install all tools and
open a browser tab with the rendered ``index.rst`` slide set:

```sh
. .env --yes
invoke view
```

Note that ``invoke view`` starts a watchdog process that will react to any
changes in ``*.rst`` files by rendering and reloading the open browser tab (*live reload*).

To directly view the demo slides that come with this template, execute these commands:

```sh
git clone "https://github.com/Springerle/hovercraft-slides.git"
cd hovercraft-slides
. .env --yes
invoke test
```
