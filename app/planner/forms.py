from wtforms import Form, StringField, DateField, RadioField, validators


class TaskForm(Form):
    name = StringField('Name', [validators.InputRequired()])
    date = DateField('Date', [validators.InputRequired()])
    priority = RadioField('Priority', coerce=int,
                          choices=[(-1, 'unimportant'),
                                   (0, 'standard'),
                                   (1, 'important')])

