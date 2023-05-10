#!/usr/bin/python3
"""
This module contains the definition of the City
class that inherits from the BaseModel class
"""


from models.base_model import BaseModel


class City(BaseModel):
    """This is the City class that is a subclass of the
    BaseModel Class"""

    state_id = ""
    name = ""
