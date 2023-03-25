import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250),  nullable=False)
    password = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    properties =  Column(Text (250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    properties =  Column(Text (250), nullable=False)   

class Favorite_character(Base):
    __tablename__ = 'favorite_character'    
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    character_id = Column(Integer,ForeignKey('character.id'), primary_key=True)
    user = relationship('User')
    character = relationship('Character')

class Favorite_planet(Base):
    __tablename__ = 'favorite_planet'     
    user_id = Column(Integer, ForeignKey('user.id'),primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'),primary_key=True)    
    user = relationship('User')
    planet = relationship('Planet')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
