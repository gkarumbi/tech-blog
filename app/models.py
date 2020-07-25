from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader

def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    
    __tablename__= 'users'

    
    #Columns
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    blog_id = db.relationship('Blog', backref='user', lazy='dynamic')
    comment_id = db.relationship('Comment', backref='user', lazy='dynamic')

    @property

    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash= generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    
    def __repr__(self):
        return f'User{self.username}'

class Quote:
    '''
    Class to define our Quote objects
    '''
    def __init__(self,author,id,quote,url):
        self.author = author
        self.id = id
        self.quote = quote
        self.url = url

class Blog(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    blog = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.now(tz=None))
    comment_id = db.relationship('comment', backref='blog', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_blog(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_blog(cls, id):
        blogs = Blog.query.order_by(Blog.posted.desc()).all()
        return blogs

    @classmethod
    def delete_blog(self, blog_id):
        comments = Comment.query.filter_by(blog_id=blog_id).delete()
        blog = Blog.query.filter_by(id=blog_id).delete()
        db.session.commit()

    @classmethod
    def edit_blog(self, blog_id):

        blog = Comment.query.filter_by(id=blog_id).edit()

        db.session.commit()


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)

    comments = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.now(tz=None))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls, id):
        reviews = Comment.query.filter_by(blog_id=id).all()
        return comments

    @classmethod
    def delete_comment(self, comment_id):

        comment = Comment.query.filter_by(id=comment_id).delete()

        db.session.commit()