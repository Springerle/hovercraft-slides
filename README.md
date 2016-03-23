# hovercraft-slides

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

The demo slides rendered from
[reStructuredText](https://raw.githubusercontent.com/Springerle/hovercraft-slides/master/%7B%7Bcookiecutter.repo_name%7D%7D/index.rst)
look like this:

![Demo slide thumbnails](https://raw.githubusercontent.com/Springerle/hovercraft-slides/master/assets/slides.jpg)


## Usage

### Quick Test of the Default Slides

To directly view the demo slides that come with this template, execute these commands:

```sh
git clone "https://github.com/Springerle/hovercraft-slides.git"
cd hovercraft-slides
. .env --yes && invoke test
```

After a while, a browser tab should open with the rendered presentation.


### Create Your Own Slide Set

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


### Add Your Own Logo

The logo that appears on the right of slide titles is in the ``img/title-logo.png`` file.
Keep it roughly the same height at ``72px`` – if your logo is not square, you should
increase the ``padding-right`` value of ``80px`` for ``h1`` accordingly (in the
first section of ``css/default.css``).
