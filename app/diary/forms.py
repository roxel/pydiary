#!/usr/bin/python
# coding: utf-8
from wtforms import Form, StringField, TextAreaField, DateField
from wtforms.validators import InputRequired, Length


class PostForm(Form):
    title = StringField("Title", validators=[InputRequired(), Length(min=0, max=100)])
    content = TextAreaField("Content", validators=[InputRequired()])
    date = DateField('Date', validators=[InputRequired()])


