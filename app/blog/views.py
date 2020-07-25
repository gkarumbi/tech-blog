from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user
from ..models import User
from .forms import BlogForm
from . import blog
from ..models import Blog, Comment
from .. import db

@blog.route('/blog/new', methods=['GET', 'POST'])
@login_required
def new_blog():

    form = BlogForm()

    if form.validate_on_submit():

        title = form.title.data
        
        blog = form.blog.data

        new_blog = Blog(blog=blog, title=title)

        new_blog.save_blog()

        return redirect(url_for('main.index'))

    return render_template('new_blog.html', blog_form=form)