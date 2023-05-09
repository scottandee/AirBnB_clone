#!/usr/bin/python3
"""This contains unittests for the base model class"""


import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestInstantiation(unittest.TestCase):
    """This tests the behaviour of the __init__ method
    """

    def test_id_is_unique(self):
        """Tests that id attribute is unique for each instance
of BaseModel()"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model2.id, model1.id)

    def test_created_is_instance_datetime(self):
        """Tests that created_at attribute is a datetime object"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_is_instance_datetime(self):
        """Tests that updated_at attribute is a datetime object"""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_updated_is_same_with_created(self):
        """Tests that created_at and updated_at are
the same at instantiation"""
        model = BaseModel()
        diff = model.updated_at - model.created_at
        self.assertEqual(diff.seconds, 0)
        self.assertLess(diff.microseconds, 15)

    def test_kwargs_not_added_to_dictionary(self):
        """Tests that BaseModel instances created with kwargs are not
        added to FileStorage.__objects"""
        model_json = {'my_number': 89, 'name': 'My First Model',
                      'updated_at': '2017-09-28T21:05:54.119572',
                      'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                      'created_at': '2017-09-28T21:05:54.119427'}
        new_model = BaseModel(**model_json)
        key = f"{type(new_model).__name__}.{new_model.id}"
        all_objs = storage.all()
        self.assertFalse(key in all_objs)

    def test_new_instance_added_to_dictionary(self):
        """Tests that BaseModel instances created without kwargs
        are added to FileStorage.__objects"""
        model = BaseModel()
        key = f"{type(model).__name__}.{model.id}"
        all_objs = storage.all()
        self.assertTrue(key in all_objs)


class TestSaveMethod(unittest.TestCase):
    """This tests the save instance method"""

    def test_updated_at_different_from_created_at(self):
        """Tests that updated_at attribute is different from created_at
attribute after calling save() method"""
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.created_at, model.updated_at)

    def test_updated_is_instance_datetime(self):
        """Tests that new updated_at attribute is a datetime object"""
        model = BaseModel()
        model.save()
        self.assertIsInstance(model.created_at, datetime)

    def test_save_contains_updated(self):
        """This tests that the new updated_at time
        is saved into __objects when save() is called"""
        model = BaseModel()
        model.name = "My_First_Model"
        model.my_number = 89
        model.save()
        key = f"{type(model).__name__}.{model.id}"
        all_objs = storage.all()
        obj = all_objs[key]
        self.assertEqual(model.updated_at, obj.updated_at)


class TestToDictMethod(unittest.TestCase):
    """This tests the to_dict() instance method"""

    def setUp(self):
        """Setup for to_dict() Test Class"""
        self.model = BaseModel()

    def test_undercore_class_is_present(self):
        """Tests that __class__ is a key in dictionary created by
to_dict method"""
        dictionary = self.model.to_dict()
        self.assertEqual(dictionary['__class__'], type(self.model).__name__)

    def test_dates_in_isoformat(self):
        """Tests that dates in to_dict() dictionary are in ISO format"""
        created_time = self.model.created_at
        updated_time = self.model.updated_at
        dictionary = self.model.to_dict()
        self.assertEqual(dictionary['created_at'], created_time.isoformat())
        self.assertEqual(dictionary['updated_at'], updated_time.isoformat())

    def test_declared_instance_attributes(self):
        """This tests the to_dict() instance method"""
        self.model.name = "Jane"
        self.model.number = 60
        dictionary = self.model.to_dict()
        self.assertEqual(dictionary['name'], self.model.name)
        self.assertEqual(dictionary['number'], self.model.number)

    def test_dates_equal_after_to_dict_call(self):
        """This tests the to_dict() instance method"""
        created_time = self.model.created_at
        updated_time = self.model.updated_at
        dictionary = self.model.to_dict()
        self.assertEqual(datetime.fromisoformat(dictionary['created_at']),
                         created_time)
        self.assertEqual(datetime.fromisoformat(dictionary['created_at']),
                         created_time)

    def test_id_is_equal_after_dict_call(self):
        """This tests the to_dict() instance method"""
        id_before_call = self.model.id
        dictionary = self.model.to_dict()
        self.assertEqual(id_before_call, dictionary['id'])

    def test_format_after_call(self):
        """This tests the to_dict() instance method"""
        dic = self.model.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)
        self.assertEqual(type(dic['id']), str)


class TestDisplayWhenPrinted(unittest.TestCase):
    """This contains the unuttests for the __str__ methods"""

    def test_display(self):
        """Tests the output of the __str__() method"""
        model = BaseModel()
        output = model.__str__()
        self.assertEqual(output, f"[{type(model).__name__}] ({model.id}) \
{model.__dict__}")


class TestInstantionWithKwargs(unittest.TestCase):
    """This contains the unittests for the __init__ method
    with the newly added kwargs parameter"""

    def test_kwargs_is_None(self):
        """This tests when kwargs is None"""
        model = BaseModel(None)
        output = model.__str__()
        self.assertEqual(output, f"[{type(model).__name__}] ({model.id}) \
{model.__dict__}")

    def test_kwargs_regular(self):
        """This tests when kwargs is assigned"""
        dic = {'__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.11\
9572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28\
T21:05:54.119427'}
        model = BaseModel(**dic)
        output = model.__str__()
        self.assertEqual(output, f"[{type(model).__name__}] ({model.id}) \
{model.__dict__}")

    def test_kwargs_regular_with_args_present(self):
        """This tests when kwargs is assigned with args also present"""
        dic = {'__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.11\
9572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28\
T21:05:54.119427'}
        model = BaseModel(45, "string", **dic)
        output = model.__str__()
        self.assertEqual(output, f"[{type(model).__name__}] ({model.id}) \
{model.__dict__}")

    def test_kwargs_with_declared_attrs(self):
        """This tests when kwargs is assigned"""
        dic = {'my_number': 89, 'name': 'My First Model', '__class__': 'BaseMo\
del', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a\
75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
        model = BaseModel(**dic)
        output = model.__str__()
        self.assertEqual(output, f"[{type(model).__name__}] ({model.id}) \
{model.__dict__}")

    def test_kwargs_with_declared_attrs_and_args(self):
        """This tests when kwargs is assigned with args also present"""
        dic = {'my_number': 89, 'name': 'My First Model', '__class__': 'BaseMo\
del', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a\
75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
        model = BaseModel(45, "string", **dic)
        output = model.__str__()
        self.assertEqual(output, f"[{type(model).__name__}] ({model.id}) \
{model.__dict__}")

    def test_create_not_same_object(self):
        """Tests that instance created with kwargs is not the same
object"""
        model1 = BaseModel()
        dic = model1.to_dict()
        model2 = BaseModel(**dic)
        self.assertFalse(model1 is model2)

    def test_kwargs_created_is_instance_datetime(self):
        dic = {'__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.11\
9572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28\
T21:05:54.119427'}
        model = BaseModel(**dic)
        self.assertIsInstance(model.created_at, datetime)

    def test_underscore_class_is_not_instance_attr(self):
        dic = {'__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.11\
9572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28\
T21:05:54.119427'}
        model = BaseModel()
        dic = model.__dict__
        with self.assertRaises(KeyError):
            dic['__class__']
