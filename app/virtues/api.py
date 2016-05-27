from flask_restful import Resource, fields, marshal_with
from ..extensions import api
from .models import Virtue

virtue_get_json_field = {
    "id": fields.Integer,
    "title": fields.String,
    "content": fields.String,
    "date_time": fields.DateTime,
    "user": fields.String,
    "date_created": fields.DateTime,
}


@api.resource('/api/1.0/virtues/', endpoint='virtues')
class VirtueListApi(Resource):

    @marshal_with(virtue_get_json_field)
    def get(self):
        return Virtue.query.all()


@api.resource('/api/1.0/virtues/<int:virtue_id>')
class VirtueApi(Resource):

    @marshal_with(virtue_get_json_field)
    def get(self, virtue_id):
        return Virtue.query.get(virtue_id)
