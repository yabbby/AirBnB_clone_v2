#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models import HBNB_STORAGE
from models.base_model import Base, BaseModel


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if HBNB_STORAGE == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship(
            "Place", back_populates="user", cascade="all, delete")
        reviews = relationship(
            "Review", cascade="all, delete", back_populates="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
