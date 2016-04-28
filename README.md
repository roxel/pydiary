Planner
-------
Simple Flask application for managing tasks. 

Overview
-------

* tested on Python 3.4.3
* uses Sqlite and SQLAlchemy for database access
* front-end is based on Bootstrap 3 and jQuery using fonts from https://www.google.com/fonts

Installation
-------

To install required flask extension simply run:

    $ pip install -r requirements.txt
    
To start application:

    $ python run.py
    
The application will be available on `http://localhost:8080/`.
    
You can also use included Makefile to prepare environment: `make prepare`. 
And to run the application along with installing extensions use default target: `make`

Testing
-------

All tests are inside `/test` directory and can be run by:

    $ python -m unittest discover
    
or through `make test`

Current version: 1.0
-------
