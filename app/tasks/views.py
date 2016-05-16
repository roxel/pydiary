from flask import Blueprint, render_template, request, redirect, url_for, abort
from .forms import TaskForm
from .models import Task
from ..database import db
from app.helpers import get_date_from_date_string, RegexConverter


tasks = Blueprint('tasks', __name__, url_prefix='/tasks')


@tasks.route('/')
def show_index():
    tasks = Task.query.order_by(Task.date.desc()).all()
    return render_template("tasks/index.html", tasks=tasks)


@tasks.route('/add', methods=['GET', 'POST'])
def add_task():
    form = TaskForm(request.form)
    if request.method == "POST" and form.validate():
        task = Task.from_form_data(form)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('tasks.show_index'))
    else:
        return render_template('tasks/form.html',
                               form=form,
                               submit_string="Add")


@tasks.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id=None):
    if not task_id:
        return redirect(url_for('tasks.show_index'))
    task = Task.query.get(task_id)
    if task:
        if request.method == 'POST':
            form = TaskForm(request.form)
            if request.method == 'POST' and form.validate():
                form.populate_obj(task)
                db.session.commit()
            return redirect(url_for('tasks.show_index'))
        else:
            form = TaskForm(obj=task)
        return render_template('tasks/form.html', form=form, submit_string="Save", task_id=task_id)
    return abort(404)


@tasks.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.filter(Task.id == task_id).one()
    if task:
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('tasks.show_index'))
    else:
        abort(404)