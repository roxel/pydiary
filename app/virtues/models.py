import markdown
from app.database import db
from markupsafe import Markup
from sqlalchemy import Integer, String, Date, DateTime, Text


class Virtue(db.Model):
    __tablename__ = 'virtues'
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(200), nullable=False)
    subtitle = db.Column(Text, nullable=False)
    description = db.Column(Text)
    user_id = db.Column(Integer, db.ForeignKey('users.id'))
    icon_path = db.Column(String(750), nullable=False)
    illustration_path = db.Column(String(750), nullable=False)
    commitments = db.relationship('Commitment', backref='virtue')

    def __init__(self, title, subtitle, description, icon_path, illustration_path):
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.icon_path = icon_path
        self.illustration_path = illustration_path

    def __repr__(self):
        return '<Virtue {}>'.format(self.title)

    def is_chosen_by_user(self, user_id, timestamp):
        return True

    @property
    def formatted_description(self):
        return Markup(markdown.markdown(self.description))

    @property
    def formatted_subtitle(self):
        return Markup(markdown.markdown(self.subtitle))


class Commitment(db.Model):
    __tablename__ = 'commitments'
    id = db.Column(Integer, primary_key=True)
    virtue_id = db.Column(Integer, db.ForeignKey('virtues.id'))
    user_id = db.Column(Integer, db.ForeignKey('users.id'))
    time_started = db.Column(DateTime, nullable=False)

    def __init__(self, virtue_id, user_id, time_started):
        self.user_id = user_id
        self.virtue_id = virtue_id
        self.time_started = time_started

