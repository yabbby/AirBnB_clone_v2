#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import declarative_base

from models import HBNB_STORAGE

if HBNB_STORAGE == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.save()
        else:
            if "updated_at" in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                kwargs["updated_at"] = datetime.now()

            if "created_at" in kwargs:
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                kwargs["created_at"] = datetime.now()

            if "__class__" in kwargs:
                del kwargs['__class__']

            if "id" not in kwargs:
                kwargs["id"] = str(uuid.uuid4())

            self.__dict__.update(kwargs)
            self.save()

    def __str__(self):
        """Returns a string representation of the instance"""
        dict_representation = self.to_dict()
        cls = dict_representation["__class__"]

        if "__class__" in dict_representation:
            dict_representation.pop("__class__")

        return '[{}] ({}) {}'.format(cls, self.id, dict_representation)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        """Deletes the current instance"""
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if "_sa_instance_state" in dictionary:
            dictionary.pop("_sa_instance_state")

        return dictionary
