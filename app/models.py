from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class pitch(db.Model):
    tablename = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    category = db.Column(db.String)
    comment = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.relationship('Comment', backref='pitch', lazy='dynamic')
    

    def save_post(self):
        db.session.add(self)
        db.session.commit()
    def repr(self):
        return f'Pitch {self.title}'

class Comment(db.Model):
    _tablename_ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitch.id"))
    
    

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()
        return comments

    @classmethod
    def get_comment_author(cls, user_id):
        author = User.query.filter_by(id=user_id).first()

        return author


class User(UserMixin,db.Model):
    _tablename_ = 'users'

    post = db.relationship('Pitch',backref = 'user',lazy = "dynamic")

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    def _repr_(self):
        return f'User {self.username}'
        