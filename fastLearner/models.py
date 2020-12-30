from .extensions import db
import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(20),nullable=False,server_default='dhl_345@qq.com')
    password = db.Column(db.String(32),nullable=False)
    posts= db.relationship('Post',back_populates='user')
    
    def __repr__(self):
        return '<User %r>' % self.username

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True,nullable=False)
    posts = db.relationship('Post', back_populates='category')
    
    def __repr__(self):
        return '<Category %r>' % self.name

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40),nullable=False)
    body = db.Column(db.String(320), nullable=False)
    create_time = db.Column(db.String(20), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='posts')
    category=db.relationship('Category',back_populates='posts')
    comments=db.relationship('Comment',back_populates='post')
    def __repr__(self):
        return '<Post %r>' % self.title

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(320),nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post',back_populates='comments')

    def __repr__(self):
        return '<Comment %r>' % self.body
