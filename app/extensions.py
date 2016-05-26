from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_wtf import CsrfProtect

login_manager = LoginManager()
bcrypt = Bcrypt()
csrf_protect = CsrfProtect()
api = Api()


def init_extensions(app):

    # password encryption
    bcrypt.init_app(app)

    # flask-login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # csrf protection
    csrf_protect.init_app(app)

    # api
    api.decorators = [csrf_protect.exempt]
    api.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    from .auth.models import User
    return User.query.filter(User.id == user_id).one()




