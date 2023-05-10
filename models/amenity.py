#!/usr/bin/python3
"""
This module contains the definition of the Amenity
class that inherits from the BaseModel class
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """This is the Amenity class that is a subclass of the
    BaseModel Class"""

    name = ""
