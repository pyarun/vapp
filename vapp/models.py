from sqlalchemy import Column, Integer, String
from database import Base
from __init__ import db


class User(db.Model):
    """
    """
    id = Column(Integer, primary_key=True)
    username = Column('username', String(50), unique=True , index=True)
    email = Column('email',String(50),unique=True , index=True)
    password = Column(String(10))
    google_id = Column(String(1000), unique=True)

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.username)