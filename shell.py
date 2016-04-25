#!/usr/bin/env python3
import os

os.environ['PYTHONINSPECT'] = 'True'

from app.database import init_db, db_session
from app.planner.models import Task
from datetime import datetime

init_db()


print("use: get_tasks() and add_task(name, priority)")


def get_tasks():
    tasks = Task.query.all()
    return tasks


def add_task(name, priority):
    task = Task(name, datetime.utcnow().date(), priority)
    db_session.add(task)
    db_session.commit()
    return task

