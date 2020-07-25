from flask import render_template,request,redirect,url_for
from . import main
from ..models import User,Quote,Comment,Blog
from flask_login import login_required, current_user
from ..import db
from ..request import get_quotes
import requests
import urllib.request,json
from .forms import CommentForm


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    welcome_message = 'Welcome to the Home!'
    
    quotes = get_quotes()
    blogs = Blog.get_blog(id)

    return render_template('index.html', welcome_message = welcome_message, quotes = quotes,blogs = blogs )

@main.route('/blog/<int:id>')

def individual_blog(id):

    individual_blog = Blog.query.get(id)

    comments = Comment.get_comment(id)

    if individual_blog is None:
        abort (404)

    return render_template('blog.html', blog=individual_blog, comments=comments)




@main.route('/blog/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):

    blog = Blog.query.filter_by(id=id).first()

    if blog is None:
        abort(404)

    form = CommentForm()

    if form.validate_on_submit():

        comment = form.comment.data

        new_comment = Comment(comment=comment, user_id=current_user.id, blog_id=blog.id)

        new_comment.save_comment()

        return redirect(url_for('.individual_blog', id=blog.id))

    return render_template('new_comment.html', comment_form=form, blog=blog)