from flask import Blueprint

planner = Blueprint('planner', __name__, url_prefix='/planner')

@planner.route('/')
def show_index():
    return "this is planner page", 200