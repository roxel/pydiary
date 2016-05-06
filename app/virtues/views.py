# coding: utf-8

from flask import Blueprint, render_template, abort, redirect, url_for, request, make_response
from .forms import VirtueForm
from .models import Virtue
from ..database import db

virtues = Blueprint('virtues', __name__, url_prefix='/virtues')


@virtues.route('/')
def show_virtues():
    virtues = Virtue.query.all()
    return render_template("virtues/index.html", virtues=virtues)


@virtues.route('/add', methods=['GET', 'POST'])
def add_virtue():
    form = VirtueForm(request.form)
    if request.method == "POST" and form.validate():
        virtue = Virtue(title=form.title.data,
                        subtitle=form.subtitle.data,
                        description=form.description.data,
                        icon_path=form.icon_path.data,
                        illustration_path=form.illustration_path.data)
        db.session.add(virtue)
        db.session.commit()
        return redirect(url_for('virtues.show_virtues'))
    else:
        return render_template('virtues/form.html',
                               form=form,
                               submit_string="Add")


@virtues.route('/show/<virtue_id>', methods=['GET'])
def show_virtue(virtue_id=None):
    if not virtue_id:
        return redirect(url_for('virtues.show_virtues'))
    virtue = Virtue.query.get(virtue_id)
    if virtue:
        return render_template('virtues/show.html', virtue=virtue)
    return abort(404)


@virtues.route('/edit/<int:virtue_id>', methods=['GET', 'POST'])
def edit_virtue(virtue_id=None):
    if not virtue_id:
        return redirect(url_for('virtues.show_virtues'))
    virtue = Virtue.query.get(virtue_id)
    if virtue:
        if request.method == 'POST':
            form = VirtueForm(request.form)
            if request.method == 'POST' and form.validate():
                form.populate_obj(virtue)
                db.session.commit()
            return redirect(url_for('virtues.show_virtues'))
        else:
            form = VirtueForm(obj=virtue)
        return render_template('virtues/form.html', form=form, submit_string="Save", virtue_id=virtue_id)
    return abort(404)


@virtues.route('/delete/<int:virtue_id>', methods=['POST'])
def delete_virtue(virtue_id):
    virtue = Virtue.query.filter(Virtue.id == virtue_id).one()
    if virtue:
        db.session.delete(virtue)
        db.session.commit()
        return redirect(url_for('virtues.show_virtues'))
    else:
        abort(404)












