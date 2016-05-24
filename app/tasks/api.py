from flask import request, abort
from flask_restful import Resource, fields, marshal_with
from ..extensions import api, csrf_protect
from ..database import db
from .models import Task
from .forms import TaskForm


task_json_field = {
    "id": fields.Integer,
    "name": fields.String,
    "date_time": fields.DateTime,
    "done": fields.Boolean,
    "priority": fields.Integer,
    "date_created": fields.DateTime,
    "user": fields.String
}


class TaskApi(Resource):

    @marshal_with(task_json_field)
    def get(self, user_id):
        return Task.query.get(user_id)


class TaskListApi(Resource):

    @marshal_with(task_json_field)
    def get(self):
        print("processing get")
        return Task.query.all()

    @marshal_with(task_json_field)
    @csrf_protect.exempt
    def post(self):
        print("processing post")
        form = TaskForm(data=request.get_json())
        print(form.date)
        print(form.name)
        print(form.priority)
        if form.validate():
            task = Task.from_form_data(form)
            db.session.add(task)
            db.session.commit()
        else:
            return abort(400)
        return 200

api.add_resource(TaskListApi, '/api/1.0/tasks/')
api.add_resource(TaskApi, '/api/1.0/tasks/<int:user_id>')

