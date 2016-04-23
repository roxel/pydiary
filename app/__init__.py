#!/usr/bin/env python3
from flask import Flask

from .planner import planner

BLUEPRINTS = (
    planner,
)


def register_blueprints(app):
    for b in BLUEPRINTS:
        app.register_blueprint(b)
    return app


def configure_general(app):
    @app.route("/")
    def show_index():
        return "this is index page", 200


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    configure_general(app)
    app.config.from_object('config')
    return app


app = create_app()