from flask import Blueprint, render_template, request, redirect, url_for, abort
from .forms import TaskForm
from .models import Task
from sqlalchemy import desc
from app.database import db_session

planner = Blueprint('planner', __name__, url_prefix='/planner')


@planner.route('/')
def show_index():
    tasks = Task.query.order_by(Task.date.desc()).all()
    return render_template("planner/index.html", tasks=tasks)


@planner.route('/add', methods=['GET', 'POST'])
def add_task():
    form = TaskForm(request.form)
    if request.method == "POST" and form.validate():
        task = Task(name=form.name.data,
                    date=form.date.data,
                    priority=form.priority.data)
        db_session.add(task)
        db_session.commit()
        return redirect(url_for('planner.show_index'))
    else:
        return render_template('planner/form.html',
                               form=form,
                               submit_string="Add")


@planner.route('/edit/<task_id>', methods=['GET', 'POST'])
def edit_task(task_id=None):
    if not task_id:
        return redirect(url_for('planner.show_index'))
    task = Task.query.get(task_id)
    if task:
        if request.method == 'POST':
            form = TaskForm(request.form)
            if request.method == 'POST' and form.validate():
                form.populate_obj(task)
                db_session.commit()
        else:
            form = TaskForm(obj=task)
        return render_template('planner/form.html', form=form, submit_string="Edit")
    return abort(404)