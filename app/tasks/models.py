from app.database import db
from sqlalchemy import Integer, String, DateTime, Boolean, Date
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(200), nullable=False)
    date = db.Column(Date, nullable=False)
    done = db.Column(Boolean)
    priority = db.Column(Integer, nullable=False)
    date_created = db.Column(DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    def __init__(self, name, date, done=False, priority=0):
        self.name = name
        self.date = date
        self.done = done
        self.priority = priority
        self.date_created = datetime.utcnow()

    def __repr__(self):
        return '<Task {}: {}>'.format(self.id, self.name)

    @staticmethod
    def from_form_data(form):
        return Task(name=form.name.data,
                    date=form.date.data,
                    done=form.done.data,
                    priority=form.priority.data)

    @hybrid_property
    def date_time(self):
        return datetime.combine(self.date, datetime.max.time())
