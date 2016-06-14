from app.database import db
from sqlalchemy import Integer, String, DateTime, Boolean, Date
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime


class Task(db.Model):
    """
    Model for tasks – everything user has to work on.
    All of the tasks are bound by dane before which they must be accomplished although the date isn't fixed.
    """
    __tablename__ = 'tasks'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(200), nullable=False)
    date = db.Column(Date, nullable=False)
    done = db.Column(Boolean)
    # priority: Integer for ordering importance of tasks. The base priority value is 0.
    priority = db.Column(Integer, nullable=False)
    # date_created: saved for future usage
    date_created = db.Column(DateTime, nullable=False)
    # user_id: nullable for testing and API development version compatibility
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
        """
        Creates new Task object from given Flask-WTF Form.
        :param form: Flask-WTF Form instance
        :return: new Task object
        """
        return Task(name=form.name.data,
                    date=form.date.data,
                    done=form.done.data,
                    priority=form.priority.data)

    @hybrid_property
    def date_time(self):
        """
        Creates datetime object from given date field and midnight ending this date

        :return: datetime object equivalent to this date
        """
        return datetime.combine(self.date, datetime.max.time())
