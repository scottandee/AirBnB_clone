#!/usr/bin/python3
"""
This module contains the definition of the User
class that inherits from the BaseModel class
"""


from models.base_model import BaseModel


class User(BaseModel):
    """This is the User class that is a subclass of the
    BaseModel Class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
