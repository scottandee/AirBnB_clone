#!/usr/bin/python3
"""This contains unittests for the FileStorage class"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
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
        all_objs = storage.all()
        len1 = len(all_objs)
        model1 = BaseModel()
        model2 = BaseModel()
        model3 = BaseModel()
        len2 = len(all_objs)
        key1 = f"{type(model1).__name__}.{model1.id}"
        key2 = f"{type(model2).__name__}.{model2.id}"
        key3 = f"{type(model3).__name__}.{model3.id}"
        all_objs = storage.all()
        self.assertTrue(key1 in all_objs)
        self.assertTrue(key2 in all_objs)
        self.assertTrue(key3 in all_objs)
        self.assertEqual(len1 + 3, len2)


class TestNew(unittest.TestCase):
    """This tests the new() instance method of the FileStorage Class"""

    def test_new_instance_in_objects(self):
        """This tests that the new() method properly adds an instance
        to the __objects dictionary"""
        all_objs = storage.all()
        len1 = len(all_objs)
        model1 = BaseModel()
        my_user = User()
        len2 = len(all_objs)
        all_objs_values = all_objs.values()
        self.assertTrue(model1 in all_objs_values)
        self.assertTrue(my_user in all_objs_values)
        self.assertEqual(len2 - len1, 2)

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

    def test_type_in_which_json_file_is_stored(self):
        """This tests that the json file is stored as a list"""
        model = BaseModel()
        model.save()
        with open("file.json", "r") as f:
            string = f.read()
        self.assertTrue(type(string) is str)
        objs_json = json.loads(string)
        self.assertTrue(type(objs_json) is dict)

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

    def test_city_convert_to_json(self):
        """This tests that the save() method properly converts the __objects
        file to JSON"""
        my_city = City()
        my_city.first_name = "Betty"
        my_city.state_id = "2983u93"
        my_city.name = "Comrade"
        my_city.password = "root"
        my_city.save()
        key = f"{type(my_city).__name__}.{my_city.id}"
        with open("file.json", "r") as f:
            string = f.read()
        objs_json = json.loads(string)
        self.assertTrue(key in objs_json)

    def test_state_convert_to_json(self):
        """This tests that the save() method properly converts the __objects
        file to JSON"""
        my_state = State()
        my_state.name = "Comrade"
        my_state.save()
        key = f"{type(my_state).__name__}.{my_state.id}"
        with open("file.json", "r") as f:
            string = f.read()
        objs_json = json.loads(string)
        self.assertTrue(key in objs_json)

    def test_amenity_convert_to_json(self):
        """This tests that the save() method properly converts the __objects
        file to JSON"""
        my_amenity = Amenity()
        my_amenity.name = "Comrade"
        my_amenity.save()
        key = f"{type(my_amenity).__name__}.{my_amenity.id}"
        with open("file.json", "r") as f:
            string = f.read()
        objs_json = json.loads(string)
        self.assertTrue(key in objs_json)

    def test_review_convert_to_json(self):
        """This tests that the save() method properly converts the __objects
        file to JSON"""
        my_review = Review()
        my_review.name = "Comrade"
        my_review.save()
        key = f"{type(my_review).__name__}.{my_review.id}"
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
            self.assertTrue(type(all_objs[key]) in [User, BaseModel, Review,
                                                    Place, City, Amenity,
                                                    State])
