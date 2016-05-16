from datetime import datetime
from app.database import db
from sqlalchemy import Integer, String, Date, DateTime, Text


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(Integer, primary_key=True)
    # user = Column
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


