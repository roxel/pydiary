from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_wtf import CsrfProtect

login_manager = LoginManager()
bcrypt = Bcrypt()
api = Api()
csrf_protect = CsrfProtect()


def init_extensions(app):

    # password encryption
    bcrypt.init_app(app)

    # flask-login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # api
    api.init_app(app)

    # csrf protection
    csrf_protect.init_app(app)
    from .tasks.api import TaskApi, TaskListApi
    csrf_protect.exempt(TaskApi)
    csrf_protect.exempt(TaskListApi)


@login_manager.user_loader
def load_user(user_id):
    from .auth.models import User
    return User.query.filter(User.id == user_id).one()




