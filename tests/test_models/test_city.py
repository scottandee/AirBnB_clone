#!/usr/bin/python3
"""This contains unittests for the City class"""


import unittest
from models.city import City
from models import storage
from datetime import datetime


class TestCityIsSubclassOfBaseModel(unittest.TestCase):
    """This tests that the City class is actually a subclass
    of the BaseModel class"""

    def city_is_subclass(self):
        city = City()
        self.assertTrue(issubclass(City, BaseModel))


class TestCityInstantiation(unittest.TestCase):
    """This tests the behaviour of the __init__ method
    on the city class"""

    def test_city_id_is_unique(self):
        """Tests that id attribute is unique for each instance
        of city()"""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_city_created_is_instance_datetime(self):
        """Tests that created_at attribute is a datetime object"""
        city = City()
        self.assertIsInstance(city.created_at, datetime)

    def test_city_updated_is_instance_datetime(self):
        """Tests that updated_at attribute is a datetime object"""
        city = City()
        self.assertIsInstance(city.updated_at, datetime)

    def test_city_updated_is_same_with_created(self):
        """Tests that created_at and updated_at are
        the same at instantiation"""
        city = City()
        diff = city.updated_at - city.created_at
        self.assertEqual(diff.seconds, 0)
        self.assertLess(diff.microseconds, 50)

    def test_city_kwargs_not_added_to_dictionary(self):
        """Tests that City instances created with kwargs are not
        added to FileStorage.__objects"""
        city_json = {'my_number': 89, 'name': 'My First City',
                     'updated_at': '2017-09-28T21:05:54.119572',
                     'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                     'created_at': '2017-09-28T21:05:54.119427'}
        new_city = City(**city_json)
        key = f"{type(new_city).__name__}.{new_city.id}"
        all_objs = storage.all()
        self.assertFalse(key in all_objs)

    def test_city_new_instance_added_to_dictionary(self):
        """Tests that City instances created without kwargs
        are added to FileStorage.__objects"""
        city = City()
        key = f"{type(city).__name__}.{city.id}"
        all_objs = storage.all()
        self.assertTrue(key in all_objs)


class TestAssigningCityClassAttributes(unittest.TestCase):
    """This unittests that the class attrbutes are assigned correctly"""

    def test_assigning_city_state_id(self):
        """This tests assigning a city_id to city class"""
        city = City()
        city.state_id = "9bf17966-b092-4996-bd33-26a5353cccb4"
        self.assertEqual(getattr(city, "state_id"),
                         "9bf17966-b092-4996-bd33-26a5353cccb4")
        self.assertEqual(getattr(City, "state_id"), "")
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(City, "state_id"))

    def test_assigning_name(self):
        """This tests assigning an text to city class"""
        city = City()
        city.name = "Palm houses"
        self.assertEqual(getattr(city, "name"), "Palm houses")
        self.assertEqual(getattr(City, "name"), "")
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(City, "name"))


class TestCitySaveMethod(unittest.TestCase):
    """This tests the save instance method"""

    def test_updated_at_different_from_created_at(self):
        """Tests that updated_at attribute is different from created_at
        attribute after calling save() method"""
        city = City()
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)

    def test_city_updated_is_instance_datetime(self):
        """Tests that new updated_at attribute is a datetime object"""
        city = City()
        city.save()
        self.assertIsInstance(city.created_at, datetime)

    def test_city_save_contains_updated(self):
        """This tests that the new updated_at time
        is saved into __objects when save() is called"""
        city = City()
        city.name = "My_First_City"
        city.my_number = 89
        city.save()
        key = f"{type(city).__name__}.{city.id}"
        all_objs = storage.all()
        obj = all_objs[key]
        self.assertEqual(city.updated_at, obj.updated_at)


class TestCityToDictMethod(unittest.TestCase):
    """This tests the to_dict() instance method"""

    def setUp(self):
        """Setup for to_dict() Test Class"""
        self.city = City()

    def test_city_undercore_class_is_present(self):
        """Tests that __class__ is a key in dictionary created by
        to_dict method"""
        dictionary = self.city.to_dict()
        self.assertEqual(dictionary['__class__'], type(self.city).__name__)

    def test_city_dates_in_isoformat(self):
        """Tests that dates in to_dict() dictionary are in ISO format"""
        created_time = self.city.created_at
        updated_time = self.city.updated_at
        dictionary = self.city.to_dict()
        self.assertEqual(dictionary['created_at'], created_time.isoformat())
        self.assertEqual(dictionary['updated_at'], updated_time.isoformat())

    def test_city_declared_instance_attributes(self):
        """This tests the to_dict() instance method"""
        self.city.name = "Jane"
        self.city.number = 60
        self.city.state_id = "562638236"
        self.city.text = "Georgia"

        dictionary = self.city.to_dict()
        self.assertEqual(dictionary['name'], self.city.name)
        self.assertEqual(dictionary['number'], self.city.number)
        self.assertEqual(dictionary['state_id'], self.city.state_id)
        self.assertEqual(dictionary['name'], self.city.name)

    def test_city_dates_equal_after_to_dict_call(self):
        """This tests the to_dict() instance method"""
        created_time = self.city.created_at
        updated_time = self.city.updated_at
        dictionary = self.city.to_dict()
        self.assertEqual(datetime.fromisoformat(dictionary['created_at']),
                         created_time)
        self.assertEqual(datetime.fromisoformat(dictionary['created_at']),
                         created_time)

    def test_city_id_is_equal_after_dict_call(self):
        """This tests the to_dict() instance method"""
        id_before_call = self.city.id
        dictionary = self.city.to_dict()
        self.assertEqual(id_before_call, dictionary['id'])

    def test_city_format_after_call(self):
        """This tests the to_dict() instance method"""
        dic = self.city.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)
        self.assertEqual(type(dic['id']), str)


class TestCityDisplayWhenPrinted(unittest.TestCase):
    """This contains the unuttests for the __str__ methods"""

    def test_city_display(self):
        """Tests the output of the __str__() method"""
        city = City()
        output = city.__str__()
        self.assertEqual(output, f"[{type(city).__name__}] ({city.id}) \
{city.__dict__}")

    def test_city_display_with_class_attributes(self):
        """Tests the output of the __str__() method
        with class attributes initialized"""
        city = City()
        name = "Alaska"
        state_id = "70398-19-1210"
        output = city.__str__()
        self.assertEqual(output, f"[{type(city).__name__}] ({city.id}) \
{city.__dict__}")


class TestCityInstantionWithKwargs(unittest.TestCase):
    """This contains the unittests for the __init__ method
    with the newly added kwargs parameter"""

    def test_city_kwargs_is_None(self):
        """This tests when kwargs is None"""
        city = City(None)
        output = city.__str__()
        self.assertEqual(output, f"[{type(city).__name__}] ({city.id}) \
{city.__dict__}")

    def test_city_kwargs_regular(self):
        """This tests when kwargs is assigned"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279", "updated_at":
               "2017-09-28T21:11:42.848291", "name": "Alaska",
               "__class__": "City", "state_id": "729-28-92",
               "password": "root"}
        city = City(**dic)
        output = city.__str__()
        self.assertEqual(output, f"[{type(city).__name__}] ({city.id}) \
{city.__dict__}")

    def test_city_kwargs_regular_with_args_present(self):
        """This tests when kwargs is assigned with args also present"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279", "updated_at":
               "2017-09-28T21:11:42.848291", "name": "Washington",
               "__class__": "City", "state_id": "738737", "password": "root"}
        city = City(45, "string", **dic)
        output = city.__str__()
        self.assertEqual(output, f"[{type(city).__name__}] ({city.id}) \
{city.__dict__}")

    def test_city_kwargs_with_declared_attrs(self):
        """This tests when kwargs is assigned"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279", "updated_at":
               "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com",
               "first_name": "Betty", "__class__": "City", "last_name": "Bar",
               "password": "root", "name": "Anafi", "state_id": 8938182,
               "name": "Bagre"}
        city = City(**dic)
        output = city.__str__()
        self.assertEqual(output, f"[{type(city).__name__}] ({city.id}) \
{city.__dict__}")

    def test_city_kwargs_with_declared_attrs_and_args(self):
        """This tests when kwargs is assigned with args also present"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279", "updated_at":
               "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com",
               "first_name": "Betty", "__class__": "City", "last_name": "Bar",
               "password": "root", "text": "Anafi", "state_id": "98337"}
        city = City(45, "string", **dic)
        output = city.__str__()
        self.assertEqual(output, f"[{type(city).__name__}] ({city.id}) \
{city.__dict__}")

    def test_city_create_not_same_object(self):
        """Tests that instance created with kwargs is not the same
        object"""
        city1 = City()
        dic = city1.to_dict()
        city2 = City(**dic)
        self.assertFalse(city1 is city2)

    def test_city_kwargs_created_is_instance_datetime(self):
        """This tests that the city class created is an instance of datetime"""
        dic = {'__class__': 'City', 'updated_at': '2017-09-28T21:05:54.119572',
               'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at':
               '2017-09-28T21:05:54.119427'}
        city = City(**dic)
        self.assertIsInstance(city.created_at, datetime)

    def test_city_underscore_class_is_not_instance_attr(self):
        """This tests thet the underscore class is not an instance attribute"""
        dic = {'__class__': 'City', 'updated_at': '2017-09-28T21:05:54.119572',
               'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at':
               '2017-09-28T21:05:54.119427'}
        city = City()
        dic = city.__dict__
        with self.assertRaises(KeyError):
            dic['__class__']
