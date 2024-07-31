#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

# from models import HBNB_STORAGE, storage
import models
from models.base_model import Base, BaseModel
from models.review import Review

if models.HBNB_STORAGE == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60), ForeignKey(
                              "places.id"), primary_key=True, nullable=False),
                          Column("amenity_id", String(60), ForeignKey(
                              "amenities.id"), primary_key=True,
                              nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    if models.HBNB_STORAGE == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship(
            "Review", back_populates="place", cascade="all, delete")
        amenities = relationship(
            "Amenity", secondary=place_amenity,
            back_populates="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            review_list = []
            for obj in models.storage.all(Review).values():
                if obj.place_id == self.id:
                    review_list.append(obj)

            return review_list

        @property
        def amenities(self):
            from models.amenity import Amenity
            amenity_list = []
            for obj in models.storage.all(Amenity).values():
                if obj.id in self.amenity_ids:
                    amenity_list.append(obj)

            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            from models.amenity import Amenity
            if not isinstance(obj, Amenity):
                return
            self.amenity_ids.append(obj.id)
