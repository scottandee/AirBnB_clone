#!/usr/bin/python3
"""This contains unittests for the Place class"""


import unittest
from models.place import Place
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestPlaceInstantiation(unittest.TestCase):
    """This tests the behaviour of the __init__ method
    on the Place class"""

    def test_place_is_subclass_of_basemodel(self):
        """Tests that the Place class is a subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_id_is_unique(self):
        """Tests that id attribute is unique for each instance
        of Place()"""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_place_created_is_instance_datetime(self):
        """Tests that created_at attribute is a datetime object"""
        place = Place()
        self.assertIsInstance(place.created_at, datetime)

    def test_place_updated_is_instance_datetime(self):
        """Tests that updated_at attribute is a datetime object"""
        place = Place()
        self.assertIsInstance(place.updated_at, datetime)

    def test_place_updated_is_same_with_created(self):
        """Tests that created_at and updated_at are
the same at instantiation"""
        place = Place()
        diff = place.updated_at - place.created_at
        self.assertEqual(diff.seconds, 0)

    def test_place_kwargs_not_added_to_dictionary(self):
        """Tests that Place instances created with kwargs are not
        added to FileStorage.__objects"""
        place_json = {'my_number': 89, 'name': 'My First place',
                      'updated_at': '2017-09-28T21:05:54.119572',
                      'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                      'created_at': '2017-09-28T21:05:54.119427'}
        new_place = Place(**place_json)
        key = f"{Place.__name__}.{new_place.id}"
        all_objs = storage.all()
        self.assertFalse(key in all_objs)

    def test_place_new_instance_added_to_dictionary(self):
        """Tests that Place instances created without kwargs
        are added to FileStorage.__objects"""
        place = Place()
        key = f"{Place.__name__}.{place.id}"
        all_objs = storage.all()
        self.assertTrue(key in all_objs)


class TestPlaceClassAttributes(unittest.TestCase):
    """This unittests that the class attributes exist"""

    def test_city_id_exists(self):
        """This tests that Place and its instance has an attribute
        called city_id"""
        place1 = Place()
        self.assertTrue(hasattr(place1, "city_id"))
        self.assertTrue(hasattr(Place, "city_id"))

    def test_user_id_exists(self):
        """This tests that Place and its instance has an attribute
        called user_id"""
        place1 = Place()
        self.assertTrue(hasattr(place1, "user_id"))
        self.assertTrue(hasattr(Place, "user_id"))

    def test_name_exists(self):
        """This tests that Place and its instance has an attribute
        called name"""
        place1 = Place()
        self.assertTrue(hasattr(place1, "name"))
        self.assertTrue(hasattr(Place, "name"))

    def test_description_exists(self):
        """This tests that Place and its instance has an attribute
        called description"""
        place1 = Place()
        self.assertTrue(hasattr(place1, "description"))
        self.assertTrue(hasattr(Place, "description"))

    def test_number_rooms_exists(self):
        """This tests that Place and its instance has an attribute
        called number_rooms"""
        place1 = Place()
        self.assertTrue(hasattr(place1, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_rooms"))

    def test_number_bathrooms_exists(self):
        """This tests that Place and its instance has an attribute
        called number_bathrooms"""
        place1 = Place()
        self.assertTrue(hasattr(place1, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))

    def test_max_guest_exists(self):
        """This tests that Place and its instance has an attribute
        called max_guest"""
        place1 = Place()
        self.assertTrue(hasattr(place1, "max_guest"))
        self.assertTrue(hasattr(Place, "max_guest"))

    def test_price_by_night_exists(self):
        """This tests that Place and its instance has an attribute
        called price_by_night"""
        place1 = Place()
        self.assertTrue(hasattr(place1, "price_by_night"))
        self.assertTrue(hasattr(Place, "price_by_night"))

    def test_latitude_exists(self):
        """This tests that Place and its instance has an attribute
        called latitude"""
        place1 = Place()
        self.assertTrue(hasattr(place1, "latitude"))
        self.assertTrue(hasattr(Place, "latitude"))

    def test_longitude_exists(self):
        """This tests that Place and its instance has an attribute
        called longitude"""
        place1 = Place()
        self.assertTrue(hasattr(place1, "longitude"))
        self.assertTrue(hasattr(Place, "longitude"))

    def test_amenity_ids_exists(self):
        """This tests that Place and its instance has an attribute
        called amenity_ids"""
        place1 = Place()
        self.assertTrue(hasattr(place1, "amenity_ids"))
        self.assertTrue(hasattr(Place, "amenity_ids"))


class TestDefaultPlaceClassAttributes(unittest.TestCase):
    """This unittests that the class attributes have the
 correct default values"""

    def test_default_city_id(self):
        """This tests the type of default city_id is string"""
        place1 = Place()
        self.assertTrue(type(place1.city_id) is str)
        self.assertTrue(type(Place.city_id) is str)

    def test_default_user_id(self):
        """This tests the type of default user_id is string"""
        place1 = Place()
        self.assertTrue(type(place1.user_id) is str)
        self.assertTrue(type(Place.user_id) is str)

    def test_default_name(self):
        """This tests the type of default name is string"""
        place1 = Place()
        self.assertTrue(type(place1.name) is str)
        self.assertTrue(type(Place.name) is str)

    def test_default_description(self):
        """This tests the type of default description is string"""
        place1 = Place()
        self.assertTrue(type(place1.description) is str)
        self.assertTrue(type(Place.description) is str)

    def test_default_number_rooms(self):
        """This tests the type of default number_rooms is int"""
        place1 = Place()
        self.assertTrue(type(place1.number_rooms) is int)
        self.assertTrue(type(Place.number_rooms) is int)

    def test_default_number_bathrooms(self):
        """This tests the type of default number_bathrooms is int"""
        place1 = Place()
        self.assertTrue(type(place1.number_bathrooms) is int)
        self.assertTrue(type(Place.number_bathrooms) is int)

    def test_default_max_guest(self):
        """This tests the type of default max_guest is int"""
        place1 = Place()
        self.assertTrue(type(place1.max_guest) is int)
        self.assertTrue(type(Place.max_guest) is int)

    def test_default_price_by_night(self):
        """This tests the type of default price_by_night is int"""
        place1 = Place()
        self.assertTrue(type(place1.price_by_night) is int)
        self.assertTrue(type(Place.price_by_night) is int)

    def test_default_latitude(self):
        """This tests the type of default latitude is float"""
        place1 = Place()
        self.assertTrue(type(place1.latitude) is float)
        self.assertTrue(type(Place.latitude) is float)

    def test_default_longitude(self):
        """This tests the type of default longitude is float"""
        place1 = Place()
        self.assertTrue(type(place1.longitude) is float)
        self.assertTrue(type(Place.longitude) is float)

    def test_default_amenity_ids(self):
        """This tests the type of default amenity_ids is string"""
        place1 = Place()
        self.assertTrue(type(place1.amenity_ids) is list)
        self.assertTrue(type(Place.amenity_ids) is list)


class TestAssigningPlaceClassAttributes(unittest.TestCase):
    """This unittests that the class attributes are assigned correctly"""

    def test_assigning_city_id(self):
        """Assigns city_id"""
        place1 = Place()
        place1.city_id = "15d31173-85b7-46db-80b6-4b4ab822a03e"
        self.assertEqual(getattr(place1, "city_id"),
                         "15d31173-85b7-46db-80b6-4b4ab822a03e")

    def test_assigning_user_id(self):
        """Assigns user_id"""
        place1 = Place()
        place1.user_id = "15d31173-85b7-46db-80b6-4b4ab822a03e"
        self.assertEqual(getattr(place1, "user_id"),
                         "15d31173-85b7-46db-80b6-4b4ab822a03e")

    def test_assigning_name(self):
        """Assigns name"""
        place1 = Place()
        place1.name = "Washington Heights"
        self.assertEqual(getattr(place1, "name"), "Washington Heights")

    def test_assigning_description(self):
        """Assigns description"""
        place1 = Place()
        place1.description = "Serene, quite, kid-friendly"
        self.assertEqual(getattr(place1, "description"),
                         "Serene, quite, kid-friendly")

    def test_assigning_number_rooms(self):
        """Assigns number_rooms"""
        place1 = Place()
        place1.number_rooms = 3
        self.assertEqual(getattr(place1, "number_rooms"), 3)

    def test_assigning_number_bathrooms(self):
        """Assigns number_bathrooms"""
        place1 = Place()
        place1.number_bathrooms = 3
        self.assertEqual(getattr(place1, "number_bathrooms"), 3)

    def test_assigning_max_guest(self):
        """Assigns max_guest"""
        place1 = Place()
        place1.max_guest = 2
        self.assertEqual(getattr(place1, "max_guest"), 2)

    def test_assigning_price_by_night(self):
        """Assigns price_by_night"""
        place1 = Place()
        place1.price_by_night = 100
        self.assertEqual(getattr(place1, "price_by_night"), 100)

    def test_assigning_latitude(self):
        """Assigns latitude"""
        place1 = Place()
        place1.latitude = 5.8
        self.assertEqual(getattr(place1, "latitude"), 5.8)

    def test_assigning_longitude(self):
        """Assigns longitude"""
        place1 = Place()
        place1.longitude = 5.8
        self.assertEqual(getattr(place1, "longitude"), 5.8)

    def test_assigning_amenity_ids(self):
        """Assigns amenity_ids"""
        place1 = Place()
        place1.amenity_ids = ["15d31173-85b7-46db-80b6-4b4ab822a03e",
                              "15d31173-85b7-46db-80b6-4b4ab822a03e"]
        self.assertEqual(getattr(place1, "amenity_ids"),
                         ["15d31173-85b7-46db-80b6-4b4ab822a03e",
                          "15d31173-85b7-46db-80b6-4b4ab822a03e"])


class TestPlaceSaveMethod(unittest.TestCase):
    """This tests the save instance method"""

    def test_updated_at_different_from_created_at(self):
        """Tests that updated_at attribute is different from created_at
        attribute after calling save() method"""
        place = Place()
        place.save()
        self.assertNotEqual(place.created_at, place.updated_at)

    def test_place_updated_is_instance_datetime(self):
        """Tests that new updated_at attribute is a datetime object"""
        place = Place()
        place.save()
        self.assertIsInstance(place.created_at, datetime)

    def test_place_save_contains_updated(self):
        """This tests that the new updated_at time
        is saved into __objects when save() is called"""
        place = Place()
        place.name = "My_First_place"
        place.max_guest = 2
        place.save()
        key = f"{Place.__name__}.{place.id}"
        all_objs = storage.all()
        obj = all_objs[key]
        self.assertEqual(place.updated_at, obj.updated_at)


class TestplaceToDictMethod(unittest.TestCase):
    """This tests the to_dict() instance method"""

    def setUp(self):
        """Setup for to_dict() Test Class"""
        self.place = Place()

    def test_place_undercore_class_is_present(self):
        """Tests that __class__ is a key in dictionary created by
to_dict method"""
        dictionary = self.place.to_dict()
        self.assertTrue("__class__" in dictionary)
        self.assertEqual(dictionary['__class__'], type(self.place).__name__)

    def test_place_dates_in_isoformat(self):
        """Tests that dates in to_dict() dictionary are in ISO format"""
        created_time = self.place.created_at
        updated_time = self.place.updated_at
        dictionary = self.place.to_dict()
        self.assertEqual(dictionary['created_at'], created_time.isoformat())
        self.assertEqual(dictionary['updated_at'], updated_time.isoformat())

    def test_place_declared_instance_attributes(self):
        """This tests the to_dict() instance method"""
        self.place.name = "Washington Heights"
        self.place.number_rooms = 4

        dictionary = self.place.to_dict()
        self.assertEqual(dictionary['name'], self.place.name)
        self.assertEqual(dictionary['number_rooms'], self.place.number_rooms)

    def test_place_dates_equal_after_to_dict_call(self):
        """This tests the to_dict() instance method"""
        created_time = self.place.created_at
        updated_time = self.place.updated_at
        dictionary = self.place.to_dict()
        self.assertEqual(datetime.fromisoformat(dictionary['created_at']),
                         created_time)
        self.assertEqual(datetime.fromisoformat(dictionary['updated_at']),
                         updated_time)

    def test_place_id_is_equal_after_dict_call(self):
        """This tests the to_dict() instance method"""
        id_before_call = self.place.id
        dictionary = self.place.to_dict()
        self.assertEqual(id_before_call, dictionary['id'])

    def test_place_format_after_call(self):
        """This tests the to_dict() instance method"""
        dic = self.place.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)
        self.assertEqual(type(dic['id']), str)


class TestplaceDisplayWhenPrinted(unittest.TestCase):
    """This contains the unuttests for the __str__ methods"""

    def test_display(self):
        """Tests the output of the __str__() method"""
        place = Place()
        output = place.__str__()
        self.assertEqual(output, f"[{Place.__name__}] ({place.id}) \
{place.__dict__}")


class TestplaceInstantionWithKwargs(unittest.TestCase):
    """This contains the unittests for the __init__ method
    with the newly added kwargs parameter"""

    def test_place_kwargs_is_None(self):
        """This tests when kwargs is None"""
        place = Place(None)
        output = place.__str__()
        self.assertEqual(output, f"[{Place.__name__}] ({place.id}) \
{place.__dict__}")

    def test_place_kwargs_regular(self):
        """This tests when kwargs is assigned"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88",
               "created_at": "2017-09-28T21:11:42.848279",
               "updated_at": "2017-09-28T21:11:42.848291",
               "number_rooms": 1, "name": "Washington Heights",
               "__class__": "Place"}
        place = Place(**dic)
        output = place.__str__()
        self.assertEqual(output, f"[{Place.__name__}] ({place.id}) \
{place.__dict__}")

    def test_place_kwargs_regular_with_args_present(self):
        """This tests when kwargs is assigned with args also present"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88",
               "created_at": "2017-09-28T21:11:42.848279",
               "updated_at": "2017-09-28T21:11:42.848291",
               "number_rooms": 1, "name": "Washington Heights",
               "__class__": "Place"}
        place = Place(45, "string", **dic)
        output = place.__str__()
        self.assertEqual(output, f"[{Place.__name__}] ({place.id}) \
{place.__dict__}")

    def test_place_kwargs_with_declared_attrs(self):
        """This tests when kwargs is assigned"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88",
               "created_at": "2017-09-28T21:11:42.848279",
               "updated_at": "2017-09-28T21:11:42.848291",
               "number_rooms": 1, "name": "Washington Heights",
               "__class__": "Place"}
        place = Place(**dic)
        output = place.__str__()
        self.assertEqual(output, f"[{Place.__name__}] ({place.id}) \
{place.__dict__}")

    def test_place_kwargs_with_declared_attrs_and_args(self):
        """This tests when kwargs is assigned with args also present"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88",
               "created_at": "2017-09-28T21:11:42.848279",
               "updated_at": "2017-09-28T21:11:42.848291",
               "number_rooms": 1, "name": "Washington Heights",
               "__class__": "Place"}
        place = Place(45, "string", **dic)
        output = place.__str__()
        self.assertEqual(output, f"[{Place.__name__}] ({place.id}) \
{place.__dict__}")

    def test_place_create_not_same_object(self):
        """Tests that instance created with kwargs is not the same
        object"""
        place1 = Place()
        dic = place1.to_dict()
        place2 = Place(**dic)
        self.assertFalse(place1 is place2)

    def test_place_kwargs_created_is_instance_datetime(self):
        """This tests that the place class created is an
 instance of datetime"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88",
               "created_at": "2017-09-28T21:11:42.848279",
               "updated_at": "2017-09-28T21:11:42.848291",
               "number_rooms": 1, "name": "Washington Heights",
               "__class__": "Place"}
        place = Place(**dic)
        self.assertIsInstance(place.created_at, datetime)

    def test_place_underscore_class_is_not_instance_attr(self):
        """This tests thet the underscore class is not an instance attribute"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88",
               "created_at": "2017-09-28T21:11:42.848279",
               "updated_at": "2017-09-28T21:11:42.848291",
               "number_rooms": 1, "name": "Washington Heights",
               "__class__": "Place"}
        place = Place()
        dic = place.__dict__
        with self.assertRaises(KeyError):
            dic['__class__']
