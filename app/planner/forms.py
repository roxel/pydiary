from wtforms import Form, StringField, DateField, RadioField, BooleanField, validators


class TaskForm(Form):
    name = StringField('Name', [validators.InputRequired()])
    date = DateField('Date', [validators.InputRequired()])
    done = BooleanField('Done')
    priority = RadioField('Priority', coerce=int,
                          choices=[(-1, 'unimportant'),
                                   (0, 'standard'),
                                   (1, 'important')])

