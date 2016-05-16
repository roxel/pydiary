from app.database import db
from sqlalchemy import Integer, String, Date, DateTime, Text


class Virtue(db.Model):
    __tablename__ = 'virtues'
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(200), nullable=False)
    subtitle = db.Column(Text, nullable=False)
    description = db.Column(Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    icon_path = db.Column(String(750), nullable=False)
    illustration_path = db.Column(String(750), nullable=False)

    def __init__(self, title, subtitle, description, icon_path, illustration_path):
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.icon_path = icon_path
        self.illustration_path = illustration_path

    def __repr__(self):
        return '<Virtue {}>'.format(self.title)


