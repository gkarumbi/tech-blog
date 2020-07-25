from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):

    title = StringField('Blog Title', validators=[Required()])
    
    blog = TextAreaField('Blog')

    submit = SubmitField('Submit')



class CommentForm(FlaskForm):

    review = TextAreaField('Add Comments')

    submit = SubmitField('Submit')