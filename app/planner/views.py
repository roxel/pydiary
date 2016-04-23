from flask import Blueprint, render_template

planner = Blueprint('planner', __name__, url_prefix='/planner')

@planner.route('/')
def show_index():
    return render_template("planner/index.html")
