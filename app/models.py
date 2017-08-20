<<<<<<< HEAD
from hashlib import md5
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1
=======
# -*- coding:utf-8 -*-
from app import db
from hashlib import md5
>>>>>>> e23ef868c1dc12df73fec87ef01c2e9b9fb62e81

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
<<<<<<< HEAD
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname = nickname).first() == None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname = new_nickname).first() == None:
                break
            version += 1
        return new_nickname
        
=======
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
    # ...
    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)

>>>>>>> e23ef868c1dc12df73fec87ef01c2e9b9fb62e81
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
<<<<<<< HEAD
        return unicode(self.id)

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)
        
    def __repr__(self):
        return '<User %r>' % (self.nickname)    
        
=======
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)

>>>>>>> e23ef868c1dc12df73fec87ef01c2e9b9fb62e81
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
<<<<<<< HEAD
        return '<Post %r>' % (self.body)
=======
        return '<Post %r>' % (self.body)
>>>>>>> e23ef868c1dc12df73fec87ef01c2e9b9fb62e81
