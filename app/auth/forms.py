from flask_wtf import Form
from wtforms import StringField, PasswordField, StringField
from wtforms.validators import InputRequired, DataRequired, Email
from wtforms.fields.html5 import EmailField


class LoginForm(Form):
    user_name = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class RegisterForm(Form):
    first_name = StringField("First name", validators=[InputRequired()])
    last_name = StringField("Last name", validators=[InputRequired()])
    user_name = StringField("Username", validators=[InputRequired()])
    email = EmailField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])

