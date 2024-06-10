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
  - the `settings` directory has all of the configuration for the `blog` app
- create admin account for wagtail app `blog`
  - run `./manage.py createsuperuser`
    - Username:
    - Email: can leave blank
    - Password:
    - Password (again):
- now check can login through wagtail UI interface
 - run `./manage.py runserver 0.0.0.:8003`
 - in browser go to `localhost:8003/admin` and login (admin, PITA-changeme)

