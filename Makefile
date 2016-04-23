.PHONY: install

all: install run

prepare:
	pip install virtualenv
	virtualenv venv
	source venv/bin/activate
	make all

run:
	python run.py

install:
	pip install -r requirements.txt
