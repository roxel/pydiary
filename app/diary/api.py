from flask import request, abort
from flask_restful import Resource, fields, marshal_with
from ..extensions import api
from ..database import db
from .models import Post
from .forms import PostForm

post_get_json_field = {
    "id": fields.Integer,
    "title": fields.String,
    "content": fields.String,
    "date_time": fields.DateTime,
    "user": fields.String,
    "date_created": fields.DateTime,
}


@api.resource('/api/1.0/diary/', endpoint='diary')
class PostListApi(Resource):
    """
    Unparameterized API for listing all Post objects and creating new ones.
    """

    @marshal_with(post_get_json_field)
    def get(self):
        return Post.query.all()

    def post(self):
        """

        :return: ID of newly created Post
        """
        json_data = request.get_json()
        form = PostForm(csrf_enabled=False, data=json_data)
        if form.validate():
            post = Post.from_form_data(form)
            db.session.add(post)
            db.session.commit()
            return post.id
        else:
            invalid_fields = ""
            for field in form:
                if not field.validate(form):
                    invalid_fields += field.name
            abort(400)


@api.resource('/api/1.0/diary/<int:post_id>')
class PostApi(Resource):

    @marshal_with(post_get_json_field)
    def get(self, post_id):
        return Post.query.get(post_id)

    def put(self, post_id):
        post = Post.query.get(post_id)
        if post:
            json_data = request.get_json()
            form = PostForm(csrf_enabled=False, data=json_data)
            if form.validate():
                form.populate_obj(post)
                db.session.commit()
                return post.id
            else:
                abort(400)
        abort(404)

    def delete(self, post_id):
        post = Post.query.get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return post.id
        abort(404)

