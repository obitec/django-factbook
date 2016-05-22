========
FactBook
========

FactBook is a simple Django app to store facts about the world. The initial
focus was to have an app for keeping up-to-date country and currency
information. Future plans extend to forex conversion, street adress look
and measurement conversions.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "factbook" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'fact_book',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^fact_book/', include('fact_book.urls')),

3. Run `python manage.py migrate` to create the fact_book models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/fact_book/ to get an overview.


Development
-----------

1. Clone this repository::

    git clone https://github.com/obitec/django-factbook
    cd django-factbook

1. Create a python virtual environment and activate::

    pyvenv-3.5 venv
    . env/bin/activate

2. Update pip and innstall development dependencies::

    pip install -U pip
    pip install -r tests/requirements.txt

3.  Build the app and documentation::

    invoke build --docs

4. Create a pull request :-)
