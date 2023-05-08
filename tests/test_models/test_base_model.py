#!/usr/bin/python3
"""This contains unittests for the base model class"""


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestInstantiation(unittest.TestCase):
    """This tests the behaviour of the __init__ method
    """

    def test_id_is_unique(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model2.id, model1.id)
    def test_created_is_instance_datetime(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
    def test_updated_is_instance_datetime(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
    def test_updated_is_same_with_created(self):
        model = BaseModel()
        diff = model.updated_at - model.created_at
        self.assertEqual(diff.seconds, 0)
        self.assertLess(diff.microseconds, 10)

class TestSaveMethod(unittest.TestCase):
    """This tests the save instance method"""

    def test_updated_at_different_from_created_at(self):
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.created_at, model.updated_at)

    def test_updated_is_instance_datetime(self):
        model = BaseModel()
        model.save()
        self.assertIsInstance(model.created_at, datetime)

class TestToDictMethod(unittest.TestCase):
    """This tests the to_dict() instance method"""

    def setUp(self):
        self.model = BaseModel()

    def test_undercore_class_is_present(self):
        dictionary = self.model.to_dict()
        self.assertEqual(dictionary['__class__'], type(self.model).__name__)

    def test_dates_in_isoformat(self):
        created_time = self.model.created_at
        updated_time = self.model.updated_at
        dictionary = self.model.to_dict()
        self.assertEqual(dictionary['created_at'], created_time.isoformat())
        self.assertEqual(dictionary['updated_at'], updated_time.isoformat())

    def test_declared_intance_attributes(self):
        self.model.name = "Jane"
        self.model.number = 60
        dictionary = self.model.to_dict()
        self.assertEqual(dictionary['name'], self.model.name)
        self.assertEqual(dictionary['number'], self.model.number)

    def test_dates_equal_after_to_dict_call(self):
        created_time = self.model.created_at
        updated_time = self.model.updated_at
        dictionary = self.model.to_dict()
        self.assertEqual(datetime.fromisoformat(dictionary['created_at']), created_time)
        self.assertEqual(datetime.fromisoformat(dictionary['created_at']), created_time)

    def test_id_is_equal_after_dict_call(self):
        id_before_call = self.model.id
        dictionary = self.model.to_dict()
        self.assertEqual(id_before_call, dictionary['id'])

    def test_format_after_call(self):
        dic = self.model.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)
        self.assertEqual(type(dic['id']), str)

class TestDisplayWhenPrinted(unittest.TestCase):
    """This contains the unuttests for the __str__ methods"""
    
    def test_display(self):
        model = BaseModel()
        output = model.__str__()
        self.assertEqual(output, f"[{type(model).__name__}] ({model.id}) \
{model.__dict__}")

class TestInstantionWithKwargs(unittest.TestCase):
    """This contains the unittests for the __init__ method 
    with the newly added kwargs parameter"""

    def test_kwargs_is_None(self):
        model = BaseModel(None)
        output = model.__str__()
        self.assertEqual(output, f"[{type(model).__name__}] ({model.id}) \
{model.__dict__}")

    def test_kwargs_regular(self):
        dic = {'__class__': 'BaseModel','updated_at':'2017-09-28T21:05:54.1195\
72', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T2\
1:05:54.119427'}
        model = BaseModel(**dic)
        output = model.__str__()
        self.assertEqual(output, f"[{type(model).__name__}] ({model.id}) \
{model.__dict__}")

    def test_kwargs_regular_with_args_present(self):
        dic = {'__class__': 'BaseModel','updated_at':'2017-09-28T21:05:54.1195\
72', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T2\
1:05:54.119427'}
        model = BaseModel(45, "string", **dic)
        output = model.__str__()
        self.assertEqual(output, f"[{type(model).__name__}] ({model.id}) \
{model.__dict__}")


    def test_kwargs_with_declared_attrs(self):
        dic = {'my_number': 89, 'name': 'My First Model', '__class__': 'BaseMo\
del','updated_at':'2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a7\
5-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
        model = BaseModel(**dic)
        output = model.__str__()
        self.assertEqual(output, f"[{type(model).__name__}] ({model.id}) \
{model.__dict__}")

    def test_kwargs_with_declared_attrs_and_args(self):
        dic = {'my_number': 89, 'name': 'My First Model', '__class__': 'BaseMo\
del','updated_at':'2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a7\
5-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
        model = BaseModel(45, "string", **dic)
        output = model.__str__()
        self.assertEqual(output, f"[{type(model).__name__}] ({model.id}) \
{model.__dict__}")

    def test_create_not_same_object(self):
        model1 = BaseModel()
        dic = model1.to_dict()
        model2 = BaseModel(**dic)
        self.assertFalse(model1 is model2)

    def test_kwargs_created_is_instance_datetime(self):
        dic = {'__class__': 'BaseModel','updated_at':'2017-09-28T21:05:54.1195\
72', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T2\
1:05:54.119427'}
        model = BaseModel(**dic)
        self.assertIsInstance(model.created_at, datetime)

    def test_underscore_class_is_not_instance_attr(self):
        dic = {'__class__': 'BaseModel','updated_at':'2017-09-28T21:05:54.1195\
72', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T2\
1:05:54.119427'}
        model = BaseModel()
        dic = model.__dict__
        with self.assertRaises(KeyError):
            dic[__class__]
