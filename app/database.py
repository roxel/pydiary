from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(database, app):
    database.init_app(app)
