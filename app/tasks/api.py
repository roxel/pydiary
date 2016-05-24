from flask import request, abort
from flask_restful import Resource, fields, marshal_with
from ..extensions import api, csrf_protect
from ..database import db
from .models import Task
from .forms import TaskForm


task_get_json_field = {
    "id": fields.Integer,
    "name": fields.String,
    "date_time": fields.DateTime,
    "done": fields.Boolean,
    "priority": fields.Integer,
    "date_created": fields.DateTime,
    "user": fields.String
}

task_post_json_field = {
    "name": fields.String,
    "date_time": fields.DateTime,
    "done": fields.Boolean,
    "priority": fields.Integer
}


@api.resource('/api/1.0/tasks/', endpoint='tasks')
class TaskListApi(Resource):

    @marshal_with(task_get_json_field)
    def get(self):
        print("processing get")
        return Task.query.all()

    @marshal_with(task_post_json_field)
    def post(self):
        print("processing post")
        # json_data = request.get_json()
        # form = TaskForm(data=json_data)
        # print(form.date)
        # print(form.name)
        # print(form.priority)
        # if form.validate():
        #     task = Task.from_form_data(form)
        #     db.session.add(task)
        #     db.session.commit()
        # else:
        #     return abort(400)
        return 200


@api.resource('/api/1.0/tasks/<int:user_id>')
class TaskApi(Resource):

    @marshal_with(task_get_json_field)
    def get(self, user_id):
        return Task.query.get(user_id)



