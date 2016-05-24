from datetime import datetime
from app.database import db
from flask_login import UserMixin
from sqlalchemy import String, DateTime, Integer, Binary
from sqlalchemy.ext.hybrid import hybrid_property
from ..extensions import bcrypt


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String(64), nullable=False)
    last_name = db.Column(String(64), nullable=False)
    user_name = db.Column(String(64), nullable=False, unique=True)
    email = db.Column(String(64), nullable=False, unique=True)
    tasks = db.relationship('Task', backref='user')
    posts = db.relationship('Post', backref='user')
    virtues = db.relationship('Virtue', backref='user')
    _password = db.Column(Binary(60))
    date_created = db.Column(DateTime, nullable=False)

    def __init__(self, first_name, last_name, user_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.password = password
        self.date_created = datetime.utcnow()

    def __repr__(self):
        return '{} ({} {})'.format(self.user_name, self.first_name, self.last_name)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext.encode('utf-8'))

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)


