from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    """
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    password = Column(String(20), unique=True)

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password

