from flask_restful import Resource, reqparse, fields, marshal_with
from ..extensions import api
from .models import Task


task_json_field = {
    "name": fields.String,
    "date_time": fields.DateTime,
    "done": fields.Boolean,
    "priority": fields.Integer,
    "date_created": fields.DateTime,
}


class TaskListApi(Resource):

    @marshal_with(task_json_field)
    def get(self):
        return Task.query.all()

api.add_resource(TaskListApi, '/api/1.0/tasks/')

