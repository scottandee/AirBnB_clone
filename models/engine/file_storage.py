#!/usr/bin/python3
"""
This script contains the definition of the FileStorage.
This class contains methods for handling and saving
objects and also their coonversion into JSON
"""

import json
import os


class FileStorage(object):
    """This is the FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This returns a dictionary containing all objects"""

        return self.__objects

    def new(self, obj):
        """This sets in __objects the obj with key <obj class name>.id"""

        key = f'{type(obj).__name__}.{obj.id}'
        # Reread instructions on this
        # We're to pass in the obj and not the dictionary of the obj
        # This is to ensure that even after instantiation, and attriutes
        # declared will still be part of it when the save method of
        # storage class is called
        self.__objects[key] = obj

    def save(self):
        """The save method serializes __objects to the JSON
        file (path: __file_path)
        """

        dic_copy = self.__objects.copy()
        for key, value in dic_copy.items():
            dic_copy[key] = value.to_dict()
        all_objs = json.dumps(dic_copy)

        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            f.write(all_objs)

    def reload(self):
        """This method deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist)
        """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, encoding="utf-8") as f:
                json_string = f.read()

            self.__objects = json.loads(json_string)
            to_be_conv_to_obj = self.__objects.copy()

            for key, value in to_be_conv_to_obj.items():
                c_name, ide = key.split(".")
                klass = self.classes(c_name)
                to_be_conv_to_obj[key] = klass(**value)

            self.__objects = to_be_conv_to_obj.copy()

    def classes(self, class_name):
        """This will return the class of the class name that
        is passed"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.amenity import Amenity
        from models.city import City
        from models.review import Review
        from models.place import Place

        all_classes = {'BaseModel': BaseModel, 'User': User,
                       'State': State, 'Amenity': Amenity,
                       'Place': Place, 'Review': Review,
                       'City': City}
        return all_classes[class_name]
