#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    if os.environ.get("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            from models import storage, city
            # Get all cities from storage
            cities = storage.all(city.City)

            # Filter where state_id matches self.id
            matches = list(filter(lambda x: x.state_id ==
                                  self.id, cities.values()))

            return matches
