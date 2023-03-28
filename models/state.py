#!/usr/bin/python3
""" State module for AirBnB Clone Project"""
""" Importing necessary modules. """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from models import storage
from os import getenv


class State(BaseModel, Base):
	"""" State Object: inherit from BaseModel and Base (sqlalchemy)"""
	__tablename__ = "states"
	name = Column(String(128), nullable=False)
	cities = relationship("City", backref="state", cascade="all, delete")

	if getenv("HBNB_TYPE_STORAGE") != "db":
		@property
		def cities(self):
			cities_file = [obj for obj in storage.all(City).values()
                	 if obj.state_id == self.id]
			return cities_file