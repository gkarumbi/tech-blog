from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):

    comment = TextAreaField('Add Comments')

    submit = SubmitField('Submit')
