from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_restful import Api

login_manager = LoginManager()
bcrypt = Bcrypt()
api = Api()


def init_extensions(app):

    # password encryption
    bcrypt.init_app(app)

    # flask-login
    login_manager.init_app(app)
    login_manager.login_view = "sign_in"

    # api
    api.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    from .auth.models import User
    return User.query.filter(User.id == user_id).one()




