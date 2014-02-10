# Ravenskeep Characters

A Django database for creating, viewing, editing and printing LARP characters.

## Overview

The database is built in Django, a Python-built web framework. The database is hosted in PostgreSQL. Everything is currently hosted on Heroku, a cloudhosting company.

## Getting Started

First, some links to help you get started, they will explain some environment settings. What is virtualenv? What is pip? Why use this complicated way of setting up the database?

* To get started in Django development, take a look at the [Django tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/).

* To learn how to do Django development 'the right way' (i.e. using Git, virtualenv and South), see [this blog post](http://www.jeffknupp.com/blog/2012/02/09/starting-a-django-project-the-right-way/).

* For a quick primer on Python, pip and virtualenv on Windows using PowerShell, look at [this page](http://www.tylerbutler.com/2012/05/how-to-install-python-pip-and-virtualenv-on-windows-with-powershell/)

Now, the install instructions. Note that much of this is explained in the links above, although these instructions should not be difficult to understand without reading the links:

1. Create a Github account. The code is hosted at [https://github.com/rogiervanhetschip/Ravenskeep-Characters](https://github.com/rogiervanhetschip/Ravenskeep-Characters)
2. Install Git, at least version 1.8.1.2.
3. Install virtualenv (to host all software in a virtual machine, which should keep your OS clean), PostgreSQL (the database), Git (version control, at least version 1.8.1.2) and a Git GUI if you so require (Git itself is command-line only).
4. Either fork the code, via instructions found at https://help.github.com/articles/fork-a-repo, or e-mail me to get added to the project as a developer.
5. Download the code.
6. Create the virtual environment by entering `virtualenv env` in a command line, in the directory where you put the code. A directory `env` is created, containing scripts.
7. Start your virtual environment: `source env/bin/activate`
8. Install the necessary software in the virtual environment: `pip install -r requirements.txt`, again done in a command line from the source code root directory.
9. Set a local variable: `export LOCAL_DEV=true`. This variable will allow the environment to recognize it should use your local database. For specifics, see ravenskeepChars/settings.py.
10. The database has not been set up. To create all tables, run `python manage.py syncdb`. This will allow you to create an admin account. At the end there will be a warning, `chars` is not yet set up.
11. To set up your chars tables: `python runserver.py migrate chars`. The database will be set up as described in the chars/migrations directory. Django database migration tool South will take care of this.
12. Start your server, using `python manage.py runserver`
13. Point your browser at http://localhost:8000!

To start development at a later time, execute steps 7, 9, 12 and 13.

