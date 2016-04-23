from wtforms import Form, StringField, DateField, RadioField, validators


class TaskForm(Form):
    name = StringField([validators.InputRequired()])
    date = DateField([validators.Length(min=0, max=100), validators.InputRequired()])
    priority = RadioField(choices=[('unimportant', 'standard', 'important'), (-1, 0, 1)])

