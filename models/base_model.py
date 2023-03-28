#!/usr/bin/python3
""" BaseModel for AirBnB Clone Project. """
""" Importing necessary modules. """
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime

# using sqlalchemy base model.
Base = declarative_base()


class BaseModel:
    """
	    This is the BaseModel where all the
	    variables and method defined and other classes
        will inherit from.
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """ Instantiates a new model """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%datetime%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%datetime%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """ Returns a string representation of the instance """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """ Updates updated_at with current time when instance is changed """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """
			Delete the object in the storage.
		"""
        return models.storage.delete(self)

    def to_dict(self):
        """
			returns a dictionary containing all keys/values of __dict__ of the instance.
		"""
        dic = {}
        dic["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dic[key] = value.isoformat()
            elif key == "_sa_instance_state":
                pass
            else:
                dic[key] = value
        return dic