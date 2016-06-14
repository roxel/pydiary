from datetime import datetime

import markdown
from app.database import db
from markupsafe import Markup
from sqlalchemy import Integer, String, Date, DateTime, Text
from sqlalchemy.ext.hybrid import hybrid_property


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(100), nullable=False)
    content = db.Column(Text, nullable=False)
    date = db.Column(Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_created = db.Column(DateTime, nullable=False)

    def __init__(self, title, content, date=None, date_created=None):
        self.title = title
        self.content = content
        self.date = date or datetime.utcnow()
        self.date_created = date_created or datetime.utcnow()

    def __repr__(self):
        return '<Post {} (created: {})>'.format(self.title, self.date_created)

    def get_file(self):
        return str(self.date), "%s\r\n\r\n%s" % (self.title, self.content)

    @staticmethod
    def from_form_data(form):
        """
        Creates new Task object from given Flask-WTF Form.
        :param form: Flask-WTF Form instance
        :return: new Task object
        """
        return Post(title=form.title.data,
                    content=form.content.data,
                    date=form.date.data)

    @property
    def formatted_content(self):
        return Markup(markdown.markdown(self.content))

    @hybrid_property
    def date_time(self):
        """
        Creates datetime object from given date field and midnight ending this date

        :return: datetime object equivalent to this date
        """
        return datetime.combine(self.date, datetime.max.time())


