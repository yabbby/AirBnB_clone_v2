#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        state = relationship("State", back_populates="cities")
        places = relationship(
            "Place", back_populates="cities", cascade="all, delete")
    else:
        name = ""
        state_id = ""
