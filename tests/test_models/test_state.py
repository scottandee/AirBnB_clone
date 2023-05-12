#!/usr/bin/python3
"""This contains unittests for the State class"""


import unittest
from models.state import State
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestStateInstantiation(unittest.TestCase):
    """This tests the behaviour of the __init__ method
    on the State class"""

    def test_state_is_subclass_of_basemodel(self):
        """Tests that the State class is a subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_id_is_unique(self):
        """Tests that id attribute is unique for each instance
        of State()"""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_state_created_is_instance_datetime(self):
        """Tests that created_at attribute is a datetime object"""
        state = State()
        self.assertIsInstance(state.created_at, datetime)

    def test_state_updated_is_instance_datetime(self):
        """Tests that updated_at attribute is a datetime object"""
        state = State()
        self.assertIsInstance(state.updated_at, datetime)

    def test_state_updated_is_same_with_created(self):
        """Tests that created_at and updated_at are
the same at instantiation"""
        state = State()
        diff = state.updated_at - state.created_at
        self.assertEqual(diff.seconds, 0)
        self.assertLess(diff.microseconds, 15)

    def test_state_kwargs_not_added_to_dictionary(self):
        """Tests that State instances created with kwargs are not
        added to FileStorage.__objects"""
        state_json = {'my_number': 89, 'name': 'My First State',
                      'updated_at': '2017-09-28T21:05:54.119572',
                      'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                      'created_at': '2017-09-28T21:05:54.119427'}
        new_state = State(**state_json)
        key = f"{State.__name__}.{new_state.id}"
        all_objs = storage.all()
        self.assertFalse(key in all_objs)

    def test_state_new_instance_added_to_dictionary(self):
        """Tests that State instances created without kwargs
        are added to FileStorage.__objects"""
        state = State()
        key = f"{State.__name__}.{state.id}"
        all_objs = storage.all()
        self.assertTrue(key in all_objs)


class TestStateClassAttributes(unittest.TestCase):
    """This unittests that the class attributes exist"""

    def test_name_exists(self):
        """This tests that State and its instance has an attribute
        called name"""
        state1 = State()
        self.assertTrue(hasattr(state1, "name"))
        self.assertTrue(hasattr(State, "name"))


class TestDefaultStateClassAttributes(unittest.TestCase):
    """This unittests that the class attributes have the
 correct default values"""

    def test_default_name(self):
        """This tests the type of default name is string"""
        state1 = State()
        self.assertTrue(type(state1.name) is str)
        self.assertTrue(type(State.name) is str)


class TestAssigningStateClassAttributes(unittest.TestCase):
    """This unittests that the class attributes are assigned correctly"""

    def test_assigning_name(self):
        """Assigns name"""
        state1 = State()
        state1.name = "Maryland"
        self.assertEqual(getattr(state1, "name"), "Maryland")


class TestStateSaveMethod(unittest.TestCase):
    """This tests the save instance method"""

    def test_updated_at_different_from_created_at(self):
        """Tests that updated_at attribute is different from created_at
        attribute after calling save() method"""
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_state_updated_is_instance_datetime(self):
        """Tests that new updated_at attribute is a datetime object"""
        state = State()
        state.save()
        self.assertIsInstance(state.created_at, datetime)

    def test_state_save_contains_updated(self):
        """This tests that the new updated_at time
        is saved into __objects when save() is called"""
        state = State()
        state.name = "Maryland"
        state.save()
        key = f"{State.__name__}.{state.id}"
        all_objs = storage.all()
        obj = all_objs[key]
        self.assertEqual(state.updated_at, obj.updated_at)


class TestStateToDictMethod(unittest.TestCase):
    """This tests the to_dict() instance method"""

    def setUp(self):
        """Setup for to_dict() Test Class"""
        self.state = State()

    def test_state_undercore_class_is_present(self):
        """Tests that __class__ is a key in dictionary created by
to_dict method"""
        dictionary = self.state.to_dict()
        self.assertTrue("__class__" in dictionary)
        self.assertEqual(dictionary['__class__'], type(self.state).__name__)

    def test_state_dates_in_isoformat(self):
        """Tests that dates in to_dict() dictionary are in ISO format"""
        created_time = self.state.created_at
        updated_time = self.state.updated_at
        dictionary = self.state.to_dict()
        self.assertEqual(dictionary['created_at'], created_time.isoformat())
        self.assertEqual(dictionary['updated_at'], updated_time.isoformat())

    def test_state_declared_instance_attributes(self):
        """This tests the to_dict() instance method"""
        self.state.name = "Maryland"

        dictionary = self.state.to_dict()
        self.assertEqual(dictionary['name'], self.state.name)

    def test_state_dates_equal_after_to_dict_call(self):
        """This tests the to_dict() instance method"""
        created_time = self.state.created_at
        updated_time = self.state.updated_at
        dictionary = self.state.to_dict()
        self.assertEqual(datetime.fromisoformat(dictionary['created_at']),
                         created_time)
        self.assertEqual(datetime.fromisoformat(dictionary['updated_at']),
                         updated_time)

    def test_state_id_is_equal_after_dict_call(self):
        """This tests the to_dict() instance method"""
        id_before_call = self.state.id
        dictionary = self.state.to_dict()
        self.assertEqual(id_before_call, dictionary['id'])

    def test_state_format_after_call(self):
        """This tests the to_dict() instance method"""
        dic = self.state.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)
        self.assertEqual(type(dic['id']), str)


class TestStateDisplayWhenPrinted(unittest.TestCase):
    """This contains the unuttests for the __str__ methods"""

    def test_display(self):
        """Tests the output of the __str__() method"""
        state = State()
        output = state.__str__()
        self.assertEqual(output, f"[{State.__name__}] ({state.id}) \
{state.__dict__}")


class TestStateInstantionWithKwargs(unittest.TestCase):
    """This contains the unittests for the __init__ method
    with the newly added kwargs parameter"""

    def test_state_kwargs_is_None(self):
        """This tests when kwargs is None"""
        state = State(None)
        output = state.__str__()
        self.assertEqual(output, f"[{State.__name__}] ({state.id}) \
{state.__dict__}")

    def test_state_kwargs_regular(self):
        """This tests when kwargs is assigned"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88",
               "created_at": "2017-09-28T21:11:42.848279",
               "updated_at": "2017-09-28T21:11:42.848291",
               "name": "Maryland", "__class__": "State"}
        state = State(**dic)
        output = state.__str__()
        self.assertEqual(output, f"[{State.__name__}] ({state.id}) \
{state.__dict__}")

    def test_State_kwargs_regular_with_args_present(self):
        """This tests when kwargs is assigned with args also present"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88",
               "created_at": "2017-09-28T21:11:42.848279",
               "updated_at": "2017-09-28T21:11:42.848291",
               "name": "Maryland", "__class__": "State"}
        state = State(45, "string", **dic)
        output = state.__str__()
        self.assertEqual(output, f"[{State.__name__}] ({state.id}) \
{state.__dict__}")

    def test_State_kwargs_with_declared_attrs(self):
        """This tests when kwargs is assigned"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88",
               "created_at": "2017-09-28T21:11:42.848279",
               "updated_at": "2017-09-28T21:11:42.848291",
               "name": "Maryland", "__class__": "State"}
        state = State(**dic)
        output = state.__str__()
        self.assertEqual(output, f"[{State.__name__}] ({state.id}) \
{state.__dict__}")

    def test_State_kwargs_with_declared_attrs_and_args(self):
        """This tests when kwargs is assigned with args also present"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88",
               "created_at": "2017-09-28T21:11:42.848279",
               "updated_at": "2017-09-28T21:11:42.848291",
               "name": "Maryland", "__class__": "State"}
        state = State(45, "string", **dic)
        output = state.__str__()
        self.assertEqual(output, f"[{State.__name__}] ({state.id}) \
{state.__dict__}")

    def test_State_create_not_same_object(self):
        """Tests that instance created with kwargs is not the same
        object"""
        state1 = State()
        dic = state1.to_dict()
        state2 = State(**dic)
        self.assertFalse(state1 is state2)

    def test_State_kwargs_created_is_instance_datetime(self):
        """This tests that the State class created is an
 instance of datetime"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88",
               "created_at": "2017-09-28T21:11:42.848279",
               "updated_at": "2017-09-28T21:11:42.848291",
               "name": "Maryland", "__class__": "State"}
        state = State(**dic)
        self.assertIsInstance(state.created_at, datetime)

    def test_State_underscore_class_is_not_instance_attr(self):
        """This tests thet the underscore class is not an instance attribute"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88",
               "created_at": "2017-09-28T21:11:42.848279",
               "updated_at": "2017-09-28T21:11:42.848291",
               "name": "Maryland", "__class__": "State"}
        state = State()
        dic = state.__dict__
        with self.assertRaises(KeyError):
            dic['__class__']
