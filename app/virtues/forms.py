#!/usr/bin/python
# coding: utf-8
from wtforms import Form, StringField, TextAreaField
from wtforms.validators import InputRequired, Length


class VirtueForm(Form):
    title = StringField("Title", validators=[InputRequired(), Length(min=1, max=200)])
    subtitle = TextAreaField("Subtitle", validators=[InputRequired(), Length(min=1, max=750)])
    description = TextAreaField("Description", validators=[InputRequired()])
    icon_path = StringField("Icon image filename", validators=[InputRequired(), Length(min=0, max=750)])
    illustration_path = StringField("Illustration image filename", validators=[InputRequired(), Length(min=0, max=750)])


