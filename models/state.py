#!/usr/bin/python3
"""
This module contains the definition of the State
class that inherits from the BaseModel class
"""


from models.base_model import BaseModel


class State(BaseModel):
    """This is the State class that is a subclass of the
    BaseModel Class"""

    name = ""
