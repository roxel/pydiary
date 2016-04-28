from flask import Blueprint, render_template, request, redirect, url_for, abort
from .forms import TaskForm
from .models import Task
from sqlalchemy import desc
from app.database import db_session
from app.helpers import get_date_from_date_string, RegexConverter, redirect_url

planner = Blueprint('planner', __name__, url_prefix='/planner')


@planner.route('/')
def show_index():
    tasks = Task.query.order_by(Task.date.desc()).all()
    return render_template("planner/index.html", tasks=tasks)


@planner.route('/date')
@planner.route('/date/<regex("[0-9]{4}-[0-9]{2}-[0-9]{2}"):date_string>')
def show_tasks_by_date(date_string=None):
    if not date_string:
        date_string = request.args['date']
    try:
        date = get_date_from_date_string(date_string)
    except ValueError:
        return render_template("layout/custom_error_page.html", problem="Incorrect date",
                               message="We can't show tasks from this day because the date requested is incorrect.")
    tasks = Task.query.filter(Task.date == date).all()
    return render_template("planner/date_index.html", tasks=tasks, date_string=date_string)


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


@planner.route('/date/<regex("[0-9]{4}-[0-9]{2}-[0-9]{2}"):date_string>/add', methods=['GET', 'POST'])
def add_task_by_date(date_string):
    form = TaskForm(request.form)
    if request.method == "POST" and form.validate():
        task = Task(name=form.name.data,
                    date=form.date.data,
                    priority=form.priority.data)
        db_session.add(task)
        db_session.commit()
        return redirect(url_for('planner.show_tasks_by_date', date_string=date_string))
    else:
        form.date.data = get_date_from_date_string(date_string)
        return render_template('planner/form.html',
                               form=form,
                               submit_string="Add")


@planner.route('/edit/<int:task_id>', methods=['GET', 'POST'])
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
            return redirect(url_for('planner.show_index'))
        else:
            form = TaskForm(obj=task)
        return render_template('planner/form.html', form=form, submit_string="Save", task_id=task_id)
    return abort(404)


@planner.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.filter(Task.id == task_id).first()
    if task:
        db_session.delete(task)
        db_session.commit()
        return redirect(url_for('planner.show_index'))
    else:
        abort(404)