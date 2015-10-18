
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relationship
from werkzeug import generate_password_hash, check_password_hash

from roomSelector.database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    phone = Column(String(20))

    house_points = Column(Integer)

    password_hash = Column(String(54))

    user_type_id = Column(Integer, ForeignKey('user_type.id'))
    user_type = relationship('UserType', backref='user')

    room_id = Column(Integer, ForeignKey('room.id'))
    room = relationship('Room', backref='user')

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


class UserType(Base):
    __tablename__ = 'user_type'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return '<UserType %r>' % (self.name)


class Room(Base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True)
    house_id = Column(Integer, ForeignKey('house.id'))
    house = relationship('House', backref='room')

    def __repr__(self):
        return '<Room %r>' % (self.id)


class House(Base):
    __tablename__ = 'house'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    manager_id = Column(Integer, ForeignKey('user.id'))
    manager = relationship('User', backref='house')

    def __repr__(self):
        return '<House %r>' % (self.name)
