from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db_session = db.session
Base = declarative_base()


def init_db(app):
    db.init_app(app)
    with app.app_context():
        Base.metadata.create_all(bind=db.engine)
    Base.query = db_session.query_property()

