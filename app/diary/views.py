# coding: utf-8

from flask import Blueprint, render_template, abort, redirect, url_for, request, make_response, Markup, flash
from flask_login import login_required, current_user
import markdown
from ..database import db
from ..extensions import csrf_protect
from .forms import PostForm
from .models import Post


diary = Blueprint('diary', __name__, url_prefix='/diary')


@diary.route('/')
@login_required
def show_posts():
    posts = Post.query.filter(Post.user_id == current_user.id).order_by(Post.date.desc())
    return render_template("diary/index.html", posts=posts)


@diary.route('/add', methods=['GET', 'POST'])
@login_required
def add_post():
    form = PostForm(request.form)
    if request.method == "POST" and form.validate():
        post = Post(title=form.title.data,
                    content=form.content.data,
                    date=form.date.data)
        post.user_id = current_user.id
        db.session.add(post)
        db.session.commit()
        flash("You have successfully added new post.")
        return redirect(url_for('diary.show_posts'))
    else:
        return render_template('diary/form.html',
                               form=form,
                               submit_string="Add")


@diary.route('/show/<post_id>', methods=['GET'])
@login_required
def show_post(post_id=None):
    if not post_id:
        return redirect(url_for('diary.show_posts'))
    post = Post.query.get(post_id)
    if post:
        if post.user_id == current_user.id:
            post.content = Markup(markdown.markdown(post.content))
            return render_template('diary/show.html', post=post)
        else:
            return abort(403)
    return abort(404)


@diary.route('/download/<post_id>', methods=['GET'])
@login_required
def download_post(post_id=None):
    if not post_id:
        return redirect(url_for('diary.show_posts'))
    post = Post.query.get(post_id)
    if post:
        if post.user_id == current_user.id:
            filename, content = post.get_file()
            response = make_response(content)
            response.headers["Content-Disposition"] = "attachment; filename=%s.txt" % filename
            return response
        else:
            return abort(403)
    return abort(404)


@diary.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id=None):
    if not post_id:
        return redirect(url_for('diary.show_posts'))
    post = Post.query.get(post_id)
    if post:
        if post.user_id != current_user.id:
            return abort(403)
        if request.method == 'POST':
            form = PostForm(request.form)
            if form.validate():
                form.populate_obj(post)
                db.session.commit()
                flash("You have successfully edited the post.")
            return redirect(url_for('diary.show_post', post_id=post_id))
        else:
            form = PostForm(obj=post)
        return render_template('diary/form.html', form=form, submit_string="Save", post_id=post_id)
    return abort(404)


@csrf_protect.exempt
@diary.route('/delete/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if post:
        if post.user_id == current_user.id:
            db.session.delete(post)
            db.session.commit()
            flash("You have successfully deleted the post.")
            return redirect(url_for('diary.show_posts'))
        else:
            return abort(403)
    return abort(404)












