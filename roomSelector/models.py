
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String
from werkzeug import generate_password_hash, check_password_hash

from roomSelector.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    phone = Column(String(20))

    password_hash = Column(String(54))
    #user_type_id = Column(Integer, ForeignKey('parent.id'))
    #room_id = Column(Integer, ForeignKey('parent.id'))

    def __init__(self, **kwargs):
        for attr in kwargs:
            if attr == 'password_hash':
                self.setPassword(kwargs[attr])  # store password as a hash
            else:
                setattr(self, attr, kwargs[attr])  # normal attributes

    def __repr__(self):
        return '<User %r>' % (self.name)
    
    def setPassword(self, password):
        'Hash a given password and store it'
        if isinstance(password, str):
            password = unicode(password)
        self.password_hash = generate_password_hash(password)
        
    def checkPassword(self, password):
        'Check the given password (hash) against the stored hash'
        return check_password_hash(self.password_hash, password)

