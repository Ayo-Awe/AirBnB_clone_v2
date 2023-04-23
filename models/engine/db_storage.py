#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """This class manages storage of hbnb models in the database"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        """Constructor class"""
        from models.base_model import Base
        user = os.environ.get("HBNB_MYSQL_USER")
        pwd = os.environ.get("HBNB_MYSQL_PWD")
        host = os.environ.get("HBNB_MYSQL_HOST")
        db = os.environ.get("HBNB_MYSQL_DB")
        env = os.environ.get("HBNB_ENV")

        __class__.__engine = create_engine(
            f"mysql+mysqldb://{user}:{pwd}@{host}:3306/{db}",
            pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(bind=__class__.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        session = __class__.__session()
        from models import classes

        data = {}

        if cls is None:
            for _class in classes.values():
                objs = session.query(_class).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    data[key] = obj
            return data

        objs = session.query(cls).all()
        for obj in objs:
            print()
            key = f"{obj.__class__.__name__}.{obj.id}"
            data[key] = obj
        return data

    def new(self, obj):
        """Adds new object to session"""
        session = __class__.__session()
        session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        session = __class__.__session()
        session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        engine = __class__.__engine
        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=engine, expire_on_commit=False)
        __class__.__session = scoped_session(session_factory)

    def delete(self, obj=None):
        """Deletes an object from the list of
        objects in filestorage"""

        if obj is not None:
            session = __class__.__session()
            session.delete(obj)

    def close(self):
        """Close database connection and end current session
        """
        self.__session.remove()
