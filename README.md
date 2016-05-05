Planner
-------
Web application for keeping personal diary and self-improvement written with Flask and SQLAlchemy.



Overview
-------

* tested on Python 3.4.3
* uses SQLAlchemy for database access
* front-end is based on Bootstrap 3 and jQuery using fonts from https://www.google.com/fonts

Installation
-------

Using virtualenv is recommended. To setup application locally:

```shell
git clone https://github.com/roxel/pydiary.git
pip install virtualenv
virtualenv venv
source venv/bin/activate
```    

To install required flask extensions simply run:

    $ pip install -r requirements.txt
    
Application uses Flask-Migrate (based on Alembic) to manage database migrations. 
Itself it does not create any database or tables. You can use following command to let Flask-Migrate do it for you:

    $ python manage.py db upgrade
    
To start application:

    $ python run.py
    
The application will be available on `http://127.0.0.1:8080/`.
You can use different port by setting environment variable PYDIARY_PORT, e.g.:

    $ export PYDIARY_PORT=8333

Testing
-------

All tests are located inside `/test` directory and can be run by:

    $ python -m unittest discover
    
Remember to install all extensions first. There is no need to create database prior to testing as it is created in TestCase create_app method. 

Authors
-------

* Piotr Roksela
* Hubert Zajma

Current version: 1.01
-------
