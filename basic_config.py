import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))+os.path.sep
DATABASE_ADDRESS = 'sqlite:///' + PROJECT_DIR + "sqlite.db"
SECRET_KEY = "default_secret_key"
DEBUG = False