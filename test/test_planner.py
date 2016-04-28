# import Flask
import unittest
import os
from flask.ext.testing import TestCase
from app import create_app
import config
from app.database import db_session, db, Base
from app.planner.models import Task
from datetime import datetime


class PlannerTest(TestCase):

    def create_app(self):
        app = create_app('config.TestConfig')
        return app

    def tearDown(self):
        db.reflect()
        db.drop_all()
        db_session.remove()

    def test_server_running(self):
        planner_response = self.client.get("/planner/")
        self.assert200(planner_response)
        index_response = self.client.get("/")
        self.assert_redirects(index_response, '/planner')

    def test_can_save_tasks(self):
        response = self.client.get("/planner/")
        assert "no tasks to show" in str(response.data)
        task = Task(name="task1", priority=0, done=False, date=datetime.utcnow().date())
        db_session.add(task)
        db_session.commit()
        assert task in db_session
        response = self.client.get("/planner/")
        assert "no tasks to show" not in str(response.data)
        task = Task.query.filter(Task.name=="task1").first()
        db_session.delete(task)
        db_session.commit()
        response = self.client.get("/planner/")
        assert "no tasks to show" in str(response.data)


if __name__ == '__main__':
  unittest.main()