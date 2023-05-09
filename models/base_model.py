#!/usr/bin/python3
"""
BaseModel Class
This module contains the definition of the BaseModel Class
that defines all common attributes/methods for other classes
"""

from datetime import datetime
import uuid
from models import storage


class BaseModel(object):
    """Defines the class BaseModel that will serve as parent class"""

    def __init__(self, *args, **kwargs):
        """creates a new instance of BaseModel"""

        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""

        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance"""

        # A shallow copy has to be created in order to preserve
        # the original self.__dict__ that will be used in creating
        # the __str__() method

        dic = self.__dict__.copy()
        dic['updated_at'] = self.updated_at.isoformat()
        dic['created_at'] = self.created_at.isoformat()
        dic['__class__'] = type(self).__name__
        return dic

    def __str__(self):
        """returns a string representation of BaseModel instance"""

        # RE: comment in line 44
        # Remember, the return of the string value does not require
        # __class__ and the datetime in isoformat. This is the reason why
        # we have to preserve the self.__dict__

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
