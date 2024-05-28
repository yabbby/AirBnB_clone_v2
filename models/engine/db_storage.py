#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""


from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in database"""

    __engine = None
    __session: Session = None

    def __init__(self):
        """Constructor for DBStorage"""
        USER = getenv("HBNB_MYSQL_USER")
        PWD = getenv("HBNB_MYSQL_PWD")
        HOST = getenv("HBNB_MYSQL_HOST")
        DB = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            f"mysql+mysqldb://{USER}:{PWD}@{HOST}/{DB}", pool_pre_ping=True
        )

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Grabs all instances of cls in database"""
        return_dict = {}

        if cls is None:
            for obj in [User, State, City, Amenity, Place, Review]:
                for result in self.__session.query(obj).all():
                    key = f"{result.__class__.__name__}.{result.id}"
                    return_dict[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = f"{obj.__class__.__name__}.{obj.id}"
                return_dict[key] = obj

        return return_dict

    def new(self, obj):
        """Add object to current dataase session"""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """Commit all changes in database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and the databases session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close database session"""
        self.close()
