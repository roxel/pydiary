# import Flask
import unittest
from flask_testing import TestCase
from app import create_app
from app.database import db
from app.planner.models import Task
from datetime import datetime


class PlannerTest(TestCase):

    def create_app(self):
        app = create_app('config.TestConfig')
        with app.app_context():
            db.create_all()
        return app

    def tearDown(self):
        db.reflect()
        db.drop_all()
        db.session.remove()

    def test_server_running(self):
        planner_response = self.client.get("/planner/")
        self.assert200(planner_response)
        index_response = self.client.get("/")
        self.assert_redirects(index_response, '/planner')

    def test_can_save_tasks(self):
        response = self.client.get("/planner/")
        assert "no tasks to show" in str(response.data)
        task = Task(name="task1", priority=0, done=False, date=datetime.utcnow().date())
        db.session.add(task)
        db.session.commit()
        assert task in db.session
        response = self.client.get("/planner/")
        assert "no tasks to show" not in str(response.data)
        task = Task.query.filter(Task.name == "task1").first()
        db.session.delete(task)
        db.session.commit()
        response = self.client.get("/planner/")
        assert "no tasks to show" in str(response.data)


if __name__ == '__main__':
  unittest.main()