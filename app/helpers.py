from flask import request, url_for
from werkzeug.routing import BaseConverter
from datetime import datetime


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


def get_date_from_date_string(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d').date()


def redirect_url(default='tasks.show_index'):
    return request.args.get('next') or request.referrer or url_for(default)
