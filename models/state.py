#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models import HBNB_STORAGE
from models.base_model import Base, BaseModel


class State(BaseModel, Base):
    """ State class """
    if HBNB_STORAGE == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state",
                              cascade="all, delete")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)

    if HBNB_STORAGE != "db":
        @property
        def cities(self):
            """Getter for the cities attribute"""
            from models import storage
            from models.city import City
            cities = filter(lambda city: city.state_id ==
                            self.id, storage.all(City))
            return list(cities)
