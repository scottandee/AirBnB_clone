#!/usr/bin/python3
"""
This module contains the definition of the Review
class that inherits from the BaseModel class
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """This is the Review class that is a subclass of the
    BaseModel Class"""

    place_id = ""
    user_id = ""
    text = ""
