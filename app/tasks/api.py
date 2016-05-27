from flask import request, abort, make_response, jsonify
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
        return Task.query.all()

    def post(self):
        json_data = request.get_json()
        form = TaskForm(csrf_enabled=False, data=json_data)
        if form.validate():
            task = Task.from_form_data(form)
            db.session.add(task)
            db.session.commit()
            return task.id
        else:
            invalid_fields = ""
            for field in form:
                if not field.validate(form):
                    invalid_fields += field.name
            abort(400)


@api.resource('/api/1.0/tasks/<int:task_id>')
class TaskApi(Resource):

    @marshal_with(task_get_json_field)
    def get(self, task_id):
        return Task.query.get(task_id)

    def put(self, task_id):
        task = Task.query.get(task_id)
        if task:
            json_data = request.get_json()
            form = TaskForm(csrf_enabled=False, data=json_data)
            if form.validate():
                form.populate_obj(task)
                db.session.commit()
                return task.id
            else:
                abort(400)
        abort(404)

    def delete(self, task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return task.id
        abort(404)

