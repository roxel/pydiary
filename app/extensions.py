from flask_login import LoginManager
from flask_bcrypt import Bcrypt

login_manager = LoginManager()
bcrypt = Bcrypt()


def init_extensions(app):

    # password encryption
    bcrypt.init_app(app)

    # flask-login
    login_manager.init_app(app)
    login_manager.login_view = "sign_in"


@login_manager.user_loader
def load_user(user_id):
    from .auth.models import User
    return User.query.filter(User.id == user_id).one()




