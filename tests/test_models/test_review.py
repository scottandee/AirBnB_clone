#!/usr/bin/python3
"""This contains unittests for the Review class"""


import unittest
from models.review import Review
from models import storage
from datetime import datetime


class TestReviewIsSubclassOfBaseModel(unittest.TestCase):
    """This tests that the Rview class is actually a subclass
    of the BaseModel class"""

    def review_is_subclass(self):
        review = Review()
        self.assertTrue(issubclass(Review, BaseModel))


class TestReviewInstantiation(unittest.TestCase):
    """This tests the behaviour of the __init__ method
    on the review class"""

    def test_review_id_is_unique(self):
        """Tests that id attribute is unique for each instance
        of review()"""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_review_created_is_instance_datetime(self):
        """Tests that created_at attribute is a datetime object"""
        review = Review()
        self.assertIsInstance(review.created_at, datetime)

    def test_review_updated_is_instance_datetime(self):
        """Tests that updated_at attribute is a datetime object"""
        review = Review()
        self.assertIsInstance(review.updated_at, datetime)

    def test_review_updated_is_same_with_created(self):
        """Tests that created_at and updated_at are
        the same at instantiation"""
        review = Review()
        diff = review.updated_at - review.created_at
        self.assertEqual(diff.seconds, 0)
        self.assertLess(diff.microseconds, 50)

    def test_review_kwargs_not_added_to_dictionary(self):
        """Tests that Review instances created with kwargs are not
        added to FileStorage.__objects"""
        review_json = {'my_number': 89, 'name': 'My First Review',
                       'updated_at': '2017-09-28T21:05:54.119572',
                       'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                       'created_at': '2017-09-28T21:05:54.119427'}
        new_review = Review(**review_json)
        key = f"{type(new_review).__name__}.{new_review.id}"
        all_objs = storage.all()
        self.assertFalse(key in all_objs)

    def test_review_new_instance_added_to_dictionary(self):
        """Tests that Review instances created without kwargs
        are added to FileStorage.__objects"""
        review = Review()
        key = f"{type(review).__name__}.{review.id}"
        all_objs = storage.all()
        self.assertTrue(key in all_objs)


class TestAssigningReviewClassAttributes(unittest.TestCase):
    """This unittests that the class attrbutes are assigned correctly"""

    def test_assigning_place_id(self):
        """This tests assigning a place_id to review class"""
        review = Review()
        review.place_id = "1105648"
        self.assertEqual(getattr(review, "place_id"), "1105648")
        self.assertEqual(getattr(Review, "place_id"), "")
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(Review, "place_id"))

    def test_assigning_user_id(self):
        """This tests assigning a user_id to review class"""
        review = Review()
        review.user_id = "9bf17966-b092-4996-bd33-26a5353cccb4"
        self.assertEqual(getattr(review, "user_id"),
                         "9bf17966-b092-4996-bd33-26a5353cccb4")
        self.assertEqual(getattr(Review, "user_id"), "")
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(Review, "user_id"))

    def test_assigning_text(self):
        """This tests assigning an text to review class"""
        review = Review()
        review.text = "Palm houses"
        self.assertEqual(getattr(review, "text"), "Palm houses")
        self.assertEqual(getattr(Review, "text"), "")
        self.assertTrue(hasattr(review, "text"))
        self.assertTrue(hasattr(Review, "text"))


class TestReviewSaveMethod(unittest.TestCase):
    """This tests the save instance method"""

    def test_updated_at_different_from_created_at(self):
        """Tests that updated_at attribute is different from created_at
        attribute after calling save() method"""
        review = Review()
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)

    def test_review_updated_is_instance_datetime(self):
        """Tests that new updated_at attribute is a datetime object"""
        review = Review()
        review.save()
        self.assertIsInstance(review.created_at, datetime)

    def test_review_save_contains_updated(self):
        """This tests that the new updated_at time
        is saved into __objects when save() is called"""
        review = Review()
        review.name = "My_First_Review"
        review.my_number = 89
        review.save()
        key = f"{type(review).__name__}.{review.id}"
        all_objs = storage.all()
        obj = all_objs[key]
        self.assertEqual(review.updated_at, obj.updated_at)


class TestReviewToDictMethod(unittest.TestCase):
    """This tests the to_dict() instance method"""

    def setUp(self):
        """Setup for to_dict() Test Class"""
        self.review = Review()

    def test_review_undercore_class_is_present(self):
        """Tests that __class__ is a key in dictionary created by
        to_dict method"""
        dictionary = self.review.to_dict()
        self.assertEqual(dictionary['__class__'], type(self.review).__name__)

    def test_review_dates_in_isoformat(self):
        """Tests that dates in to_dict() dictionary are in ISO format"""
        created_time = self.review.created_at
        updated_time = self.review.updated_at
        dictionary = self.review.to_dict()
        self.assertEqual(dictionary['created_at'], created_time.isoformat())
        self.assertEqual(dictionary['updated_at'], updated_time.isoformat())

    def test_review_declared_instance_attributes(self):
        """This tests the to_dict() instance method"""
        self.review.name = "Jane"
        self.review.number = 60
        self.review.user_id = "63961471971"
        self.review.place_id = "562638236"
        self.review.text = "Placegos"

        dictionary = self.review.to_dict()
        self.assertEqual(dictionary['name'], self.review.name)
        self.assertEqual(dictionary['number'], self.review.number)
        self.assertEqual(dictionary['place_id'], self.review.place_id)
        self.assertEqual(dictionary['user_id'], self.review.user_id)
        self.assertEqual(dictionary['text'], self.review.text)

    def test_review_dates_equal_after_to_dict_call(self):
        """This tests the to_dict() instance method"""
        created_time = self.review.created_at
        updated_time = self.review.updated_at
        dictionary = self.review.to_dict()
        self.assertEqual(datetime.fromisoformat(dictionary['created_at']),
                         created_time)
        self.assertEqual(datetime.fromisoformat(dictionary['created_at']),
                         created_time)

    def test_review_id_is_equal_after_dict_call(self):
        """This tests the to_dict() instance method"""
        id_before_call = self.review.id
        dictionary = self.review.to_dict()
        self.assertEqual(id_before_call, dictionary['id'])

    def test_review_format_after_call(self):
        """This tests the to_dict() instance method"""
        dic = self.review.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)
        self.assertEqual(type(dic['id']), str)


class TestReviewDisplayWhenPrinted(unittest.TestCase):
    """This contains the unuttests for the __str__ methods"""

    def test_review_display(self):
        """Tests the output of the __str__() method"""
        review = Review()
        output = review.__str__()
        self.assertEqual(output, f"[{type(review).__name__}] ({review.id}) \
{review.__dict__}")

    def test_review_display_with_class_attributes(self):
        """Tests the output of the __str__() method
        with class attributes initialized"""
        review = Review()
        text = "Best experiewnce"
        user_id = "81981830183"
        place_id = "70398-19-1210"
        output = review.__str__()
        self.assertEqual(output, f"[{type(review).__name__}] ({review.id}) \
{review.__dict__}")


class TestReviewInstantionWithKwargs(unittest.TestCase):
    """This contains the unittests for the __init__ method
    with the newly added kwargs parameter"""

    def test_review_kwargs_is_None(self):
        """This tests when kwargs is None"""
        review = Review(None)
        output = review.__str__()
        self.assertEqual(output, f"[{type(review).__name__}] ({review.id}) \
{review.__dict__}")

    def test_review_kwargs_regular(self):
        """This tests when kwargs is assigned"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279", "updated_at":
               "2017-09-28T21:11:42.848291", "place_id": "81393910",
               "text": "Betty", "__class__": "Review",
               "user_id": "729-28-92", "password": "root"}
        review = Review(**dic)
        output = review.__str__()
        self.assertEqual(output, f"[{type(review).__name__}] ({review.id}) \
{review.__dict__}")

    def test_review_kwargs_regular_with_args_present(self):
        """This tests when kwargs is assigned with args also present"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279", "updated_at":
               "2017-09-28T21:11:42.848291", "text": "Aloha Houses",
               "place_id": "8873093", "__class__": "Review",
               "user_id": "738737", "password": "root"}
        review = Review(45, "string", **dic)
        output = review.__str__()
        self.assertEqual(output, f"[{type(review).__name__}] ({review.id}) \
{review.__dict__}")

    def test_review_kwargs_with_declared_attrs(self):
        """This tests when kwargs is assigned"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279", "updated_at":
               "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com",
               "first_name": "Betty", "__class__": "Review",
               "last_name": "Bar", "password": "root", "name": "Anafi",
               "place_id": 8938182, "user_id": "161339", "text": "Bagre"}
        review = Review(**dic)
        output = review.__str__()
        self.assertEqual(output, f"[{type(review).__name__}] ({review.id}) \
{review.__dict__}")

    def test_review_kwargs_with_declared_attrs_and_args(self):
        """This tests when kwargs is assigned with args also present"""
        dic = {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at":
               "2017-09-28T21:11:42.848279",
               "updated_at": "2017-09-28T21:11:42.848291",
               "email": "airbnb@mail.com",
               "first_name": "Betty", "__class__": "Review",
               "last_name": "Bar", "password": "root", "name": "Anafi",
               "place_id": "98337"}
        review = Review(45, "string", **dic)
        output = review.__str__()
        self.assertEqual(output, f"[{type(review).__name__}] ({review.id}) \
{review.__dict__}")

    def test_review_create_not_same_object(self):
        """Tests that instance created with kwargs is not the same
        object"""
        review1 = Review()
        dic = review1.to_dict()
        review2 = Review(**dic)
        self.assertFalse(review1 is review2)

    def test_review_kwargs_created_is_instance_datetime(self):
        """This tests that the review class created is an
        instance of datetime"""
        dic = {'__class__': 'Review',
               'updated_at': '2017-09-28T21:05:54.119572',
               'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at':
               '2017-09-28T21:05:54.119427'}
        review = Review(**dic)
        self.assertIsInstance(review.created_at, datetime)

    def test_review_underscore_class_is_not_instance_attr(self):
        """This tests thet the underscore class is not an
        instance attribute"""
        dic = {'__class__': 'Review',
               'updated_at': '2017-09-28T21:05:54.119572',
               'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at':
               '2017-09-28T21:05:54.119427'}
        review = Review()
        dic = review.__dict__
        with self.assertRaises(KeyError):
            dic['__class__']
