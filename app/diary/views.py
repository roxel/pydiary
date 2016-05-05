# coding: utf-8

from flask import Blueprint, render_template, abort, redirect, url_for, request, make_response
from jinja2 import TemplateNotFound
from .forms import PostForm
from .models import Post
from ..database import db

diary = Blueprint('diary', __name__, url_prefix='/diary')


@diary.route('/')
def show_posts():
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template("diary/index.html", posts=posts)


@diary.route('/add', methods=['GET', 'POST'])
def add_post():
    form = PostForm(request.form)
    if request.method == "POST" and form.validate():
        post = Post(title=form.title.data,
                    content=form.content.data,
                    date=form.date.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('diary.show_posts'))
    else:
        return render_template('diary/form.html',
                               form=form,
                               submit_string="Add")


@diary.route('/show/<post_id>', methods=['GET'])
def show_post(post_id=None):
    if not post_id:
        return redirect(url_for('diary.show_posts'))
    post = Post.query.get(post_id)
    if post:
        return render_template('diary/show.html', post=post)
    return abort(404)


@diary.route('/download/<post_id>', methods=['GET'])
def download_post(post_id=None):
    if not post_id:
        return redirect(url_for('diary.show_posts'))
    post = Post.query.get(post_id)
    if post:
        filename, content = post.get_file()
        print(content)
        print(filename)
        response = make_response(content)
        response.headers["Content-Disposition"] = "attachment; filename=%s.txt" % filename
        return response
    return abort(404)


@diary.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id=None):
    if not post_id:
        return redirect(url_for('diary.show_posts'))
    post = Post.query.get(post_id)
    if post:
        if request.method == 'POST':
            form = Post(request.form)
            if request.method == 'POST' and form.validate():
                form.populate_obj(post)
                db.session.commit()
            return redirect(url_for('diary.show_posts'))
        else:
            form = PostForm(obj=post)
        return render_template('diary/form.html', form=form, submit_string="Save", post_id=post_id)
    return abort(404)


@diary.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    task = Post.query.filter(Post.id == post_id).one()
    if task:
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('diary.show_posts'))
    else:
        abort(404)












