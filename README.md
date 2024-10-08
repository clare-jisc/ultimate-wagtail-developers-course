## Learn Wagtail - Ultimate Wagtail Developers Course

by Kalob Taulien: https://learnwagtail.com/courses/the-ultimate-wagtail-developers-course/

link to GitHub: https://github.com/KalobTaulien/ultimate-wagtail-developers-course-source-code

use PORT 8003 for `python manage.py runserver 0.0.0.0:8003` cmd for localhost instead of 8000 (avoid clashing with jisc-ac-uk setup)

### Set-up

Set python preferred version in project root directory

- ONLY IF NEEDED (add python version 3.11.4 using `pyenv install 3.11.4` cmd)
- set this project directory to use v3.11.4 with `pyenv local 3.11.4` cmd
  Set up virtual environment in project root directory
- create vitual env using `pyenv virtualenv <venv_name>` cmd
- list all virtual envs with `pyenv virtualenvs` cmd
- start virtual env using `pyenv activate <venv_name>` cmd
- deactivate virtual env using `pyenv deactivate` cmd
  Install Wagtail
- install wagtail into your virtual environment with `pip install wagtail`
- check all ok with `pip show wagtail`

Create a wagtail framework for your website app, with the name you want it to have, in this case `blog`

- create your main app and generate standard wagtail folders in project root
  - first run `wagtail start blog .`
  - now run `pip install -r requirements.txt`
  - now run `./manage.py migrate` to set up database for app `blog` with default wagtail settings
- Note:
  - no `models.py` file exists in the `blog` app, it only exists in the default `home`, `search` apps
  - the `blog/settings` directory has all of the configuration for the `blog` app
- create admin account for wagtail app `blog`
  - run `./manage.py createsuperuser`
    - Username: `admin`
    - Email: can leave blank
    - Password: `PITA-changeme`
    - Password (again): `PITA-changeme`
- now check can login through wagtail UI interface
- run `./manage.py runserver 0.0.0.0:8003`
- in browser go to `localhost:8003/admin` and login

### Upgrade wagtail to latest version

- inside virtual environment can run `pip install wagtail --upgrade`
  - this uninstalls current version and installs newer version
  - to install a specific version run `pip install wagtail==5.2`
- update `requirements.txt` file to reflect new version

### Lessons summary

click to go to [quick links to useful lessons](lessons/link_to_lessons.md#quick-links-to-useful-lessons) file

### Apps created in project

- start project by creating parent app `blog`
  - generates default `home`
  - generates default `search`
- create `images` using `./manage.py startapp images`and activate it in `blog/settings/base.py` `INSTALLED_APPS` array
- create `documents` using `./manage.py startapp documents`and activate it in `blog/settings/base.py` `INSTALLED_APPS` array
- create `blogpages` using `./manage.py startapp blogpages`and activate it in `blog/settings/base.py` `INSTALLED_APPS` array

- for Tailwind CSS create folder `src` and follow instructions in [Integrating Tailwind CSS with Wagtail](https://learnwagtail.com/courses/the-ultimate-wagtail-developers-course/adding-tailwind-css/)

- for Code Formatting:
  - to use Prettier follow instructions [Prettier - install](https://prettier.io/docs/en/install) 
  - to include Tailwind plugin follow [prettier-plugin-tailwindcss](https://github.com/tailwindlabs/prettier-plugin-tailwindcss/blob/main/README.md)
  - modify it to [make VS Code format Django templates properly](https://stackoverflow.com/questions/42170561/how-to-make-vscode-format-django-templates-properly?answertab=modifieddesc#tab-top) ❓

 - or follow [Wagtail admin UI guidelines](https://docs.wagtail.org/en/latest/contributing/ui_guidelines.html#html-guidelines) ❓

 - or Code Linting & Formatting: ✅
  - use [djLint](https://djlint.com/), which needs:
    - pypi package install [djlint](https://pypi.org/project/djlint/)
    - vs code extension [django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django) 
    - vs code extension [djlint](https://marketplace.visualstudio.com/items?itemName=monosans.djlint)

### Links to useful documentation

- [Django documentation - builtin template tags and filters](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/)
- [Wagtail documentation - Jinja2 template tags support](https://docs.wagtail.org/en/stable/reference/jinja2.html#template-tags-functions-filters)
- [Wagtail documentation - How to use images in templates](https://docs.wagtail.org/en/stable/topics/images.html#image-tag)
- [Wagtail documentation - Page model reference fields and methods](https://docs.wagtail.org/en/stable/reference/pages/model_reference.html#page)
- [Wagtail documentation - Private pages, restricting who can view](https://docs.wagtail.org/en/stable/advanced_topics/privacy.html#private-pages)
- [Wagtail Documentation - Wagtail API v2 configuration guide](https://docs.wagtail.org/en/stable/advanced_topics/api/v2/configuration.html#api-v2-configuration)


### List of useful wagtail imports

- `from django.db import models`
- `from django.core.exceptions import ValidationError`
  - used to apply custom validation to fields on a page, set specific rules for content editor to abide by, supports SEO optimisation etc
- `from wagtail.models import Page`
- `from wagtail.admin.panels import FieldPanel, MultiFieldPanel, HelpPanel`
- `from wagtail.api import APIField` 
  - to get access to API view of `/page` endpoint
- `from wagtail.fields import RichTextField`
- `from wagtail.images.models import Image, AbstractImage, AbstractRendition` 
  - create custom fields for image and custom renditions, see app `images/models.py`
- `from wagtail.images import get_image_model`
  - a function() to use with `models.ForeignKey()` to get image instead of `"wagtailimages.Image"`
- `from wagtail.documents import get_document_model`
  - a function() to use with `models.ForeignKey()` to get document instead of `"wagtaildocuments.Document"`
- `from wagtail.images.views.serve import ServeView` 
  - used in a complex url pattern in `blog/urls.py` to handle image requests
- `from rest_framework.fields import Field` 
  - create Serializer classes for each field you want to access in the API view
- `from wagtail.templatetags.wagtailcore_tags import richtext`
  - create a Serializer for richtext field if you want to see link href urls in the API view
