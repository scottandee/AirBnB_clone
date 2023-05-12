#!/usr/bin/python3
"""This contains unittests for the User class"""


import unittest
from models.user import User
from models import storage
from datetime import datetime


class TestUserIsSubclassOfBaseModel(unittest.TestCase):
    """This tests that the User class is actually a subclass
    of the BaseModel class"""
    def city_is_subclass(self):
        User = User()
        self.assertTrue(issubclass(User, BaseModel))

class TestUserInstantiation(unittest.TestCase):
    """This tests the behaviour of the __init__ method
    on the user class"""

    def test_user_id_is_unique(self):
        """Tests that id attribute is unique for each instance
        of user()"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_user_created_is_instance_datetime(self):
        """Tests that created_at attribute is a datetime object"""
        user = User()
        self.assertIsInstance(user.created_at, datetime)

    def test_user_updated_is_instance_datetime(self):
        """Tests that updated_at attribute is a datetime object"""
        user = User()
        self.assertIsInstance(user.updated_at, datetime)

    def test_user_updated_is_same_with_created(self):
        """Tests that created_at and updated_at are
        the same at instantiation"""
        user = User()
        diff = user.updated_at - user.created_at
        self.assertEqual(diff.seconds, 0)
        self.assertLess(diff.microseconds, 50)
    def test_user_kwargs_not_added_to_dictionary(self):
        """Tests that User instances created with kwargs are not
        added to FileStorage.__objects"""
        user_json = {'my_number': 89, 'name': 'My First User',
                      'updated_at': '2017-09-28T21:05:54.119572',
                      'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                      'created_at': '2017-09-28T21:05:54.119427'}
        new_user = User(**user_json)
        key = f"{type(new_user).__name__}.{new_user.id}"
        all_objs = storage.all()
        self.assertFalse(key in all_objs)

    def test_user_new_instance_added_to_dictionary(self):
        """Tests that User instances created without kwargs
        are added to FileStorage.__objects"""
        user = User()
        key = f"{type(user).__name__}.{user.id}"
        all_objs = storage.all()
        self.assertTrue(key in all_objs)

class TestAssigningUserClassAttributes(unittest.TestCase):
    """This unittests that the class attrbutes are assigned correctly"""
    
    def test_assigning_email(self):
        """This tests assigning an email to user class"""
        user = User()
        user.email = "airbnb@yahoo.com"
        self.assertEqual(getattr(user, "email"), "airbnb@yahoo.com")
        self.assertEqual(getattr(User, "email"), "")
        self.assertTrue(hasattr(user, "email"))

    def test_assigning_password(self):
        """This tests assigning a password to user class"""
        user = User()
        user.password = "tambul"
        self.assertEqual(getattr(user, "password"), "tambul")
        self.assertEqual(getattr(User, "password"), "")
        self.assertTrue(hasattr(user, "password"))

    def test_assigning_last_name(self):
        """This tests assigning an last name to user class"""
        user = User()
        user.last_name = "Jackson"
        self.assertEqual(getattr(user, "last_name"), "Jackson")
        self.assertEqual(getattr(User, "last_name"), "")
        self.assertTrue(hasattr(user, "last_name"))

    def test_assigning_first_name(self):
        """This tests assigning a first name to user class"""
        user = User()
        user.first_name = "Jones"
        self.assertEqual(getattr(user, "first_name"), "Jones")
        self.assertEqual(getattr(User, "first_name"), "")
        self.assertTrue(hasattr(user, "first_name"))
  
class TestUserSaveMethod(unittest.TestCase):
    """This tests the save instance method"""

    def test_updated_at_different_from_created_at(self):
        """Tests that updated_at attribute is different from created_at
        attribute after calling save() method"""
        user = User()
        user.save()
        self.assertNotEqual(user.created_at, user.updated_at)

    def test_user_updated_is_instance_datetime(self):
        """Tests that new updated_at attribute is a datetime object"""
        user = User()
        user.save()
        self.assertIsInstance(user.created_at, datetime)

    def test_user_save_contains_updated(self):
        """This tests that the new updated_at time
        is saved into __objects when save() is called"""
        user = User()
        user.name = "My_First_User"
        user.my_number = 89
        user.save()
        key = f"{type(user).__name__}.{user.id}"
        all_objs = storage.all()
        obj = all_objs[key]
        self.assertEqual(user.updated_at, obj.updated_at)

class TestUserToDictMethod(unittest.TestCase):
    """This tests the to_dict() instance method"""

    def setUp(self):
        """Setup for to_dict() Test Class"""
        self.user = User()

    def test_user_undercore_class_is_present(self):
        """Tests that __class__ is a key in dictionary created by
to_dict method"""
        dictionary = self.user.to_dict()
        self.assertEqual(dictionary['__class__'], type(self.user).__name__)

    def test_user_dates_in_isoformat(self):
        """Tests that dates in to_dict() dictionary are in ISO format"""
        created_time = self.user.created_at
        updated_time = self.user.updated_at
        dictionary = self.user.to_dict()
        self.assertEqual(dictionary['created_at'], created_time.isoformat())
        self.assertEqual(dictionary['updated_at'], updated_time.isoformat())

    def test_user_declared_instance_attributes(self):
        """This tests the to_dict() instance method"""
        self.user.name = "Jane"
        self.user.number = 60
        self.user.password = "baggage"
        self.user.email = "gand@gmail.com"
        self.user.first_name = "Son"
        self.user.last_name = "Min"

        dictionary = self.user.to_dict()
        self.assertEqual(dictionary['name'], self.user.name)
        self.assertEqual(dictionary['number'], self.user.number)
        self.assertEqual(dictionary['first_name'], self.user.first_name)
        self.assertEqual(dictionary['last_name'], self.user.last_name)
        self.assertEqual(dictionary['email'], self.user.email)
        self.assertEqual(dictionary['password'], self.user.password)

    def test_user_dates_equal_after_to_dict_call(self):
        """This tests the to_dict() instance method"""
        created_time = self.user.created_at
        updated_time = self.user.updated_at
        dictionary = self.user.to_dict()
        self.assertEqual(datetime.fromisoformat(dictionary['created_at']),
                         created_time)
        self.assertEqual(datetime.fromisoformat(dictionary['created_at']),
                         created_time)

    def test_user_id_is_equal_after_dict_call(self):
        """This tests the to_dict() instance method"""
        id_before_call = self.user.id
        dictionary = self.user.to_dict()
        self.assertEqual(id_before_call, dictionary['id'])

    def test_user_format_after_call(self):
        """This tests the to_dict() instance method"""
        dic = self.user.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)
        self.assertEqual(type(dic['id']), str)


class TestUserDisplayWhenPrinted(unittest.TestCase):
    """This contains the unuttests for the __str__ methods"""

    def test_user_display(self):
        """Tests the output of the __str__() method"""
        user = User()
        output = user.__str__()
        self.assertEqual(output, f"[{type(user).__name__}] ({user.id}) \
{user.__dict__}")

    def test_user_display_with_class_attributes(self):
        """Tests the output of the __str__() method
        with class attributes initialized"""
        user = User()
        last_name = "John"
        first_name = "Jones"
        email = "john@yahoo.com"
        output = user.__str__()
        self.assertEqual(output, f"[{type(user).__name__}] ({user.id}) \
{user.__dict__}")


class TestUserInstantionWithKwargs(unittest.TestCase):
    """This contains the unittests for the __init__ method
    with the newly added kwargs parameter"""

    def test_user_kwargs_is_None(self):
        """This tests when kwargs is None"""
        user = User(None)
        output = user.__str__()
        self.assertEqual(output, f"[{type(user).__name__}] ({user.id}) \
{user.__dict__}")

    def test_user_kwargs_regular(self):
        """This tests when kwargs is assigned"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279", "updated_at": 
               "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com", 
               "first_name": "Betty", "__class__": "User","last_name": "Bar"
               , "password": "root"}
        user = User(**dic)
        output = user.__str__()
        self.assertEqual(output, f"[{type(user).__name__}] ({user.id}) \
{user.__dict__}")

    def test_user_kwargs_regular_with_args_present(self):
        """This tests when kwargs is assigned with args also present"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279", "updated_at": 
               "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com", 
               "first_name": "Betty", "__class__": "User","last_name": "Bar"
               , "password": "root"}
        user = User(45, "string", **dic)
        output = user.__str__()
        self.assertEqual(output, f"[{type(user).__name__}] ({user.id}) \
{user.__dict__}")

    def test_user_kwargs_with_declared_attrs(self):
        """This tests when kwargs is assigned"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279", "updated_at": 
               "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com", 
               "first_name": "Betty", "__class__": "User","last_name": "Bar"
               , "password": "root", "name": "Anafi"}
        user = User(**dic)
        output = user.__str__()
        self.assertEqual(output, f"[{type(user).__name__}] ({user.id}) \
{user.__dict__}")

    def test_user_kwargs_with_declared_attrs_and_args(self):
        """This tests when kwargs is assigned with args also present"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279", "updated_at": 
               "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com", 
               "first_name": "Betty", "__class__": "User","last_name": "Bar"
               , "password": "root", "name": "Anafi"}
        user = User(45, "string", **dic)
        output = user.__str__()
        self.assertEqual(output, f"[{type(user).__name__}] ({user.id}) \
{user.__dict__}")

    def test_user_create_not_same_object(self):
        """Tests that instance created with kwargs is not the same
        object"""
        user1 = User()
        dic = user1.to_dict()
        user2 = User(**dic)
        self.assertFalse(user1 is user2)

    def test_user_kwargs_created_is_instance_datetime(self):
        """This tests that the user class created is an instance of datetime"""
        dic = {'__class__': 'User', 'updated_at': '2017-09-28T21:05:54.119572',
        'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': 
        '2017-09-28T21:05:54.119427'}
        user = User(**dic)
        self.assertIsInstance(user.created_at, datetime)

    def test_user_underscore_class_is_not_instance_attr(self):
        """This tests thet the underscore class is not an instance attribute"""
        dic = {'__class__': 'User', 'updated_at': '2017-09-28T21:05:54.119572',
               'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': 
               '2017-09-28T21:05:54.119427'}
        user = User()
        dic = user.__dict__
        with self.assertRaises(KeyError):
            dic['__class__']
