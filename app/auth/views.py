from flask import Blueprint, render_template, redirect, url_for, request, flash
from .forms import RegisterForm, LoginForm
from .models import User
from ..database import db

from flask_login import login_user, logout_user

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    user_name=form.user_name.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash("you have successfully registered")
        return redirect(url_for('show_index'))
    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.user_name.data).one_or_none()
        if user is not None and user.is_correct_password(form.password.data):
            login_user(user)
            flash("you have successfully logged in")
            return redirect(url_for('show_index'))
        else:
            flash("user_name or password incorrect")
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash("you have successfully logged out")
    return redirect(url_for('show_index'))

