import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))+os.path.sep
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + PROJECT_DIR + "sqlite.db"


class Config(object):
    SECRET_KEY = "default_secret_key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + PROJECT_DIR + "sqlite.db"
    DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + PROJECT_DIR + "test.db"
    DEBUG = False
    TESTING = True

