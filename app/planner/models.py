from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Date
from datetime import datetime


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    date = Column(Date)
    done = Column(Boolean)
    priority = Column(Integer)
    date_created = Column(DateTime)

    def __init__(self, name, date, done=False, priority=0):
        self.name = name
        self.date = date
        self.done = done
        self.priority = priority
        self.date_created = datetime.utcnow()

    def __repr__(self):
        return '<Task {}: {}>'.format(self.id, self.name)

