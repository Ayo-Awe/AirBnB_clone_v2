#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, Column, Integer, String, Float, Table
from sqlalchemy.orm import relationship
import os

association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey(
                              'places.id'), primary_key=True),
                          Column('amenity_id', String(60), ForeignKey(
                              'amenities.id'), primary_key=True)
                          )


class Place(BaseModel, Base):
    """ A place to stay """
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
    reviews = relationship("Review", backref="place",
                           cascade="all, delete, delete-orphan")
    amenities = relationship("Amenity",
                             secondary=association_table, viewonly=False)

    if os.environ.get("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            from models import storage, review
            # Get all reviews from storage
            cities = storage.all(review.Review)

            # Filter where place_id matches self.id
            matches = list(filter(lambda x: x.place_id ==
                                  self.id, cities.values()))

            return matches

        @property
        def amenities(self):
            from models import storage, amenity

            if self.amenity_ids is None:
                self.amenity_ids = []

            # Get all reviews from storage
            amenities = storage.all(amenity.Amenity)

            # Filter where place_id matches self.id
            matches = list(
                filter(lambda x: x.id in self.amenity_ids, amenities.values()))
            return matches

        @amenities.setter
        def amenities(self, value):
            if value is None:
                return

            if value.__class__.__name__ != "Amenity":
                return

            if self.amenity_ids is None:
                self.amenity_ids = []

            self.amenity_ids.append(value)
