#!/usr/bin/python3
"""This contains unittests for the Amenity class"""


import unittest
from models.amenity import Amenity
from models import storage
from datetime import datetime


class TestAmenityIsSubclassOfBaseModel(unittest.TestCase):
    """This tests that the Amenity class is actually a subclass
    of the BaseModel class"""
    def amenity_is_subclass(self):
        amenity = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))

class TestAmenityInstantiation(unittest.TestCase):
    """This tests the behaviour of the __init__ method
    on the amenity class"""

    def test_amenity_id_is_unique(self):
        """Tests that id attribute is unique for each instance
        of amenity()"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_amenity_created_is_instance_datetime(self):
        """Tests that created_at attribute is a datetime object"""
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)

    def test_amenity_updated_is_instance_datetime(self):
        """Tests that updated_at attribute is a datetime object"""
        amenity = Amenity()
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_amenity_updated_is_same_with_created(self):
        """Tests that created_at and updated_at are
        the same at instantiation"""
        amenity = Amenity()
        diff = amenity.updated_at - amenity.created_at
        self.assertEqual(diff.seconds, 0)
        self.assertLess(diff.microseconds, 50)
    def test_amenity_kwargs_not_added_to_dictionary(self):
        """Tests that Amenity instances created with kwargs are not
        added to FileStorage.__objects"""
        amenity_json = {'my_number': 89, 'name': 'My First Amenity',
                      'updated_at': '2017-09-28T21:05:54.119572',
                      'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                      'created_at': '2017-09-28T21:05:54.119427'}
        new_amenity = Amenity(**amenity_json)
        key = f"{type(new_amenity).__name__}.{new_amenity.id}"
        all_objs = storage.all()
        self.assertFalse(key in all_objs)

    def test_amenity_new_instance_added_to_dictionary(self):
        """Tests that Amenity instances created without kwargs
        are added to FileStorage.__objects"""
        amenity = Amenity()
        key = f"{type(amenity).__name__}.{amenity.id}"
        all_objs = storage.all()
        self.assertTrue(key in all_objs)    

class TestAssigningAmenityClassAttributes(unittest.TestCase):
    """This unittests that the class attrbutes are assigned correctly"""
    
    def test_assigning_name(self):
        """This tests assigning an text to amenity class"""
        amenity = Amenity()
        amenity.name = "Pool"
        self.assertEqual(getattr(amenity, "name"), "Pool")
        self.assertEqual(getattr(Amenity, "name"), "")
        self.assertTrue(hasattr(amenity, "name"))
        self.assertTrue(hasattr(Amenity, "name"))

class TestAmenitySaveMethod(unittest.TestCase):
    """This tests the save instance method"""

    def test_updated_at_different_from_created_at(self):
        """Tests that updated_at attribute is different from created_at
        attribute after calling save() method"""
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

    def test_amenity_updated_is_instance_datetime(self):
        """Tests that new updated_at attribute is a datetime object"""
        amenity = Amenity()
        amenity.save()
        self.assertIsInstance(amenity.created_at, datetime)

    def test_amenity_save_contains_updated(self):
        """This tests that the new updated_at time
        is saved into __objects when save() is called"""
        amenity = Amenity()
        amenity.name = "My_First_Amenity"
        amenity.my_number = 89
        amenity.save()
        amenity.name = "Electricity"
        key = f"{type(amenity).__name__}.{amenity.id}"
        all_objs = storage.all()
        obj = all_objs[key]
        self.assertEqual(amenity.updated_at, obj.updated_at)

class TestAmenityToDictMethod(unittest.TestCase):
    """This tests the to_dict() instance method"""

    def setUp(self):
        """Setup for to_dict() Test Class"""
        self.amenity = Amenity()

    def test_amenity_undercore_class_is_present(self):
        """Tests that __class__ is a key in dictionary created by
        to_dict method"""
        dictionary = self.amenity.to_dict()
        self.assertEqual(dictionary['__class__'], type(self.amenity).__name__)

    def test_amenity_dates_in_isoformat(self):
        """Tests that dates in to_dict() dictionary are in ISO format"""
        created_time = self.amenity.created_at
        updated_time = self.amenity.updated_at
        dictionary = self.amenity.to_dict()
        self.assertEqual(dictionary['created_at'], created_time.isoformat())
        self.assertEqual(dictionary['updated_at'], updated_time.isoformat())

    def test_amenity_declared_instance_attributes(self):
        """This tests the to_dict() instance method"""
        self.amenity.name = "Hot Water"
        self.amenity.number = 60
        self.amenity.text = "Georgia"

        dictionary = self.amenity.to_dict()
        self.assertEqual(dictionary['name'], self.amenity.name)
        self.assertEqual(dictionary['number'], self.amenity.number)
        self.assertEqual(dictionary['text'], self.amenity.text)

    def test_amenity_dates_equal_after_to_dict_call(self):
        """This tests the to_dict() instance method"""
        created_time = self.amenity.created_at
        updated_time = self.amenity.updated_at
        dictionary = self.amenity.to_dict()
        self.assertEqual(datetime.fromisoformat(dictionary['created_at']),
                         created_time)
        self.assertEqual(datetime.fromisoformat(dictionary['created_at']),
                         created_time)

    def test_amenity_id_is_equal_after_dict_call(self):
        """This tests the to_dict() instance method"""
        id_before_call = self.amenity.id
        dictionary = self.amenity.to_dict()
        self.assertEqual(id_before_call, dictionary['id'])

    def test_amenity_format_after_call(self):
        """This tests the to_dict() instance method"""
        dic = self.amenity.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)
        self.assertEqual(type(dic['id']), str)


class TestAmenityDisplayWhenPrinted(unittest.TestCase):
    """This contains the unuttests for the __str__ methods"""

    def test_amenity_display(self):
        """Tests the output of the __str__() method"""
        amenity = Amenity()
        output = amenity.__str__()
        self.assertEqual(output, f"[{type(amenity).__name__}] ({amenity.id}) \
{amenity.__dict__}")

    def test_amenity_display_with_class_attributes(self):
        """Tests the output of the __str__() method
        with class attributes initialized"""
        amenity = Amenity()
        name = "Wifi"
        output = amenity.__str__()
        self.assertEqual(output, f"[{type(amenity).__name__}] ({amenity.id}) \
{amenity.__dict__}")


class TestAmenityInstantionWithKwargs(unittest.TestCase):
    """This contains the unittests for the __init__ method
    with the newly added kwargs parameter"""

    def test_amenity_kwargs_is_None(self):
        """This tests when kwargs is None"""
        amenity = Amenity(None)
        output = amenity.__str__()
        self.assertEqual(output, f"[{type(amenity).__name__}] ({amenity.id}) \
{amenity.__dict__}")

    def test_amenity_kwargs_regular(self):
        """This tests when kwargs is assigned"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279", "updated_at": 
               "2017-09-28T21:11:42.848291", "name": "Wifi", 
               "__class__": "Amenity",}
        amenity = Amenity(**dic)
        output = amenity.__str__()
        self.assertEqual(output, f"[{type(amenity).__name__}] ({amenity.id}) \
{amenity.__dict__}")

    def test_amenity_kwargs_regular_with_args_present(self):
        """This tests when kwargs is assigned with args also present"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279", "updated_at": 
               "2017-09-28T21:11:42.848291", "name": "Wifi", 
               "__class__": "Amenity"}
        amenity = Amenity(45, "string", **dic)
        output = amenity.__str__()
        self.assertEqual(output, f"[{type(amenity).__name__}] ({amenity.id}) \
{amenity.__dict__}")

    def test_amenity_kwargs_with_declared_attrs(self):
        """This tests when kwargs is assigned"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279", "updated_at": 
               "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com", 
               "first_name": "Betty", "__class__": "Amenity","last_name": "Bar"
               , "password": "root", "name": "Wifi", "state_id": 8938182,
               "name": "Bagre"}
        amenity = Amenity(**dic)
        output = amenity.__str__()
        self.assertEqual(output, f"[{type(amenity).__name__}] ({amenity.id}) \
{amenity.__dict__}")

    def test_amenity_kwargs_with_declared_attrs_and_args(self):
        """This tests when kwargs is assigned with args also present"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279", "updated_at": 
               "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com", 
               "first_name": "Betty", "__class__": "Amenity","last_name": "Bar"
               , "password": "root", "name": "Wifi", "state_id": "98337"}
        amenity = Amenity(45, "string", **dic)
        output = amenity.__str__()
        self.assertEqual(output, f"[{type(amenity).__name__}] ({amenity.id}) \
{amenity.__dict__}")

    def test_amenity_create_not_same_object(self):
        """Tests that instance created with kwargs is not the same
        object"""
        amenity1 = Amenity()
        dic = amenity1.to_dict()
        amenity2 = Amenity(**dic)
        self.assertFalse(amenity1 is amenity2)

    def test_amenity_kwargs_created_is_instance_datetime(self):
        """This tests that the amenity class created is an instance of datetime"""
        dic = {'__class__': 'Amenity', 'updated_at': '2017-09-28T21:05:54.119572',
        'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': 
        '2017-09-28T21:05:54.119427'}
        amenity = Amenity(**dic)
        self.assertIsInstance(amenity.created_at, datetime)

    def test_amenity_underscore_class_is_not_instance_attr(self):
        """This tests thet the underscore class is not an instance attribute"""
        dic = {'__class__': 'Amenity', 'updated_at': '2017-09-28T21:05:54.119572',
               'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': 
               '2017-09-28T21:05:54.119427'}
        amenity = Amenity()
        dic = amenity.__dict__
        with self.assertRaises(KeyError):
            dic['__class__']
