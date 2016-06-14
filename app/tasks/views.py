from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from ..database import db
from ..extensions import csrf_protect
from .forms import TaskForm
from .models import Task
from ..helpers import get_date_from_date_string

tasks = Blueprint('tasks', __name__, url_prefix='/tasks')


@tasks.route('/')
@login_required
def show_index():
    tasks = Task.query.filter(Task.user_id == current_user.id).order_by(Task.date.desc())
    return render_template("tasks/index.html", tasks=tasks)


@tasks.route('/add', methods=['GET', 'POST'])
@login_required
def add_task():
    form = TaskForm(request.form)
    if request.method == "POST" and form.validate():
        task = Task.from_form_data(form)
        task.user_id = current_user.id
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('tasks.show_index'))
    else:
        if 'date' in request.args.keys():
            form.date.data = get_date_from_date_string(request.args['date'])
        return render_template('tasks/form.html',
                               form=form,
                               submit_string="Add")


@tasks.route('/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id=None):
    if not task_id:
        return redirect(url_for('tasks.show_index'))
    task = Task.query.get(task_id)
    if task:
        if task.user_id != current_user.id:
            return abort(403)
        if request.method == 'POST':
            form = TaskForm(request.form)
            if form.validate():
                form.populate_obj(task)
                db.session.commit()
            flash("You have successfully edited the task.")
            return redirect(url_for('tasks.show_index'))
        else:
            form = TaskForm(obj=task)
        return render_template('tasks/form.html', form=form, submit_string="Save", task_id=task_id)
    return abort(404)


@csrf_protect.exempt
@tasks.route('/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()
            flash("You have successfully deleted the task.")
            return redirect(url_for('tasks.show_index'))
        else:
            return abort(403)
    return abort(404)
