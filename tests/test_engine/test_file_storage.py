#!/usr/bin/python3
"""This contains unittests for the FileStorage class"""


import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
from datetime import datetime
import json
import os


class TestClassAttributes(unittest.TestCase):
    """This tests the attributes of the FileStorage Class"""

    def test_objects_is_dict(self):
        """This tests that __objects class attribute
        is a dictionary"""
        all_objs = storage.all()
        self.assertEqual(type(all_objs), dict)


class TestAll(unittest.TestCase):
    """This tests the all() instance method of the FileStorage Class"""

    def test_all_return_type(self):
        """This tests that the all() method returns a dictionary"""
        all_objs = storage.all()
        self.assertEqual(type(all_objs), dict)

    def test_all_return_instances(self):
        """This tests that the all() method returns a dictionary
        complete with all instances added"""
        model1 = BaseModel()
        model2 = BaseModel()
        model3 = BaseModel()
        key1 = f"{type(model1).__name__}.{model1.id}"
        key2 = f"{type(model2).__name__}.{model2.id}"
        key3 = f"{type(model3).__name__}.{model3.id}"
        all_objs = storage.all()
        self.assertTrue(key1 in all_objs)
        self.assertTrue(key2 in all_objs)
        self.assertTrue(key3 in all_objs)


class TestNew(unittest.TestCase):
    """This tests the new() instance method of the FileStorage Class"""

    def test_new_instance_in_objects(self):
        """This tests that the new() method properly adds an instance
        to the __objects dictionary"""
        model1 = BaseModel()
        my_user = User()
        all_objs = storage.all()
        all_objs_values = all_objs.values()
        self.assertTrue(model1 in all_objs_values)
        self.assertTrue(my_user in all_objs_values)

    def test_key_format(self):
        """This tests that the key created in the new()
        method is the proper format"""
        model1 = BaseModel()
        user = User()
        key1 = f"{type(model1).__name__}.{model1.id}"
        key2 = f"{type(user).__name__}.{user.id}"
        all_objs = storage.all()
        test_key1 = {i for i in all_objs if all_objs[i] == model1}
        test_key2 = {i for i in all_objs if all_objs[i] == user}
        self.assertTrue(key1 in test_key1)
        self.assertTrue(key2 in test_key2)


class TestSave(unittest.TestCase):
    """This tests the save() instance method of the FileStorage Class"""

    def test_json_file_exists(self):
        """This tests that the save() method creates a JSON file"""
        model = BaseModel()
        model.name = "My_First_Model"
        model.my_number = 89
        model.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_base_convert_to_json(self):
        """This tests that the save() method properly converts the __objects
        file to JSON"""
        model = BaseModel()
        model.name = "My_First_Model"
        model.my_number = 89
        model.save()
        key = f"{type(model).__name__}.{model.id}"
        with open("file.json", "r") as f:
            string = f.read()
        objs_json = json.loads(string)
        self.assertTrue(key in objs_json)

    def test_user_convert_to_json(self):
        """This tests that the save() method properly converts the __objects
        file to JSON"""
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()
        key = f"{type(my_user).__name__}.{my_user.id}"
        with open("file.json", "r") as f:
            string = f.read()
        objs_json = json.loads(string)
        self.assertTrue(key in objs_json)


class TestReload(unittest.TestCase):
    """This tests the reload() instance method of the FileStorage Class"""

    def test_json_conversion_to_dict(self):
        """This tests that the JSON file is properly converted back
        to the __objects dictionary when reload() is called"""
        model = BaseModel()
        model.name = "My_First_Model"
        model.my_number = 89
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()
        model.save()
        all_objs = storage.all()
        self.assertTrue(type(all_objs) is dict)
        for key in all_objs.keys():
            self.assertTrue(type(all_objs[key]) in [User, BaseModel])
            
