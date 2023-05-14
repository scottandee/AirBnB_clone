#!/usr/bin/python3
"""
This file contains unittests for console.py, which contains the
entry point of the command interpreter used to manage the objects
created for the AirBnB Clone.
The program console.py contains a single class, HBNBCommand, which
inherits from the Cmd class in Python's cmd module. This class contains
all the methods and attributes required to run the command interpreter.
"""


import unittest
import cmd
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsoleInstantiation(unittest.TestCase):
    """This tests that HBNBCommand is a subclass of Cmd"""

    def test_HBNBCommand_is_subclass_of_Cmd(self):
        """This tests that HBNBCommand is a subclass of Cmd"""
        self.assertTrue(issubclass(HBNBCommand, cmd.Cmd))


class TestCreateCommand(unittest.TestCase):
    """Tests the create command of the console with normal input"""

    def test_create_basemodel(self):
        """Tests that a new instance of BaseModel is created
        and shows the id of the instance"""
        from models import storage

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            test = f.getvalue()
            test_id = test.replace("\n", "")
            all_objs = storage.all()
            key = "BaseModel." + test_id
            self.assertTrue(key in all_objs)
            obj = all_objs[key]
            self.assertEqual(test_id, obj.id)

    def test_create_place(self):
        """Tests that a new instance of Place is created
        and shows the id of the instance"""
        from models import storage

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            test = f.getvalue()
            test_id = test.replace("\n", "")
            all_objs = storage.all()
            key = "Place." + test_id
            self.assertTrue(key in all_objs)
            obj = all_objs[key]
            self.assertEqual(test_id, obj.id)

    def test_create_state(self):
        """Tests that a new instance of State is created
        and shows the id of the instance"""
        from models import storage

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            test = f.getvalue()
            id = test.replace("\n", "")
            all_objs = storage.all()
            key = "State." + id
            self.assertTrue(key in all_objs)
            obj = all_objs[key]
            self.assertEqual(id, obj.id)

    def test_create_amenity(self):
        """Tests that a new instance of Amenity is created
        and shows the id of the instance"""
        from models import storage

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            test = f.getvalue()
            test_id = test.replace("\n", "")
            all_objs = storage.all()
            key = "Amenity." + test_id
            self.assertTrue(key in all_objs)
            obj = all_objs[key]
            self.assertEqual(test_id, obj.id)


class TestCreateCommandError(unittest.TestCase):
    """Tests the create command of the console with faulty input"""

    def test_create_no_class(self):
        """Tests that appropriate error is shown when create is
        called with no argument"""
        err_message = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_create_wrong_class(self):
        """Tests that appropriate error is shown when create is
        called with a class that doesn't exist"""
        err_message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            test = f.getvalue()
            self.assertEqual(test, err_message)


class TestAllCommand(unittest.TestCase):
    """Tests the all command of the console with normal input"""

    def test_all(self):
        """Tests that all command without argument works"""
        from models import storage

        obj_list = []
        objs = storage.all()
        for key in objs.keys():
            obj = objs[key]
            obj_list.append(obj.__str__())
        str_obj_list = str(obj_list) + "\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            test = f.getvalue()
            self.assertEqual(str_obj_list, test)

    def test_all_basemodel(self):
        """Tests that all works for BaseModel"""
        from models import storage

        obj_list = []
        objs = storage.all()
        for key in objs.keys():
            if "BaseModel" in key:
                obj = objs[key]
                obj_list.append(obj.__str__())
            else:
                continue
        str_obj_list = str(obj_list) + "\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            test = f.getvalue()
            self.assertEqual(str_obj_list, test)

    def test_all_place(self):
        """Tests that all works for Place"""
        from models import storage

        obj_list = []
        objs = storage.all()
        for key in objs.keys():
            if "Place" in key:
                obj = objs[key]
                obj_list.append(obj.__str__())
            else:
                continue
        str_obj_list = str(obj_list) + "\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Place")
            test = f.getvalue()
            self.assertEqual(str_obj_list, test)

    def test_all_state(self):
        """Tests that all works for State"""
        from models import storage

        obj_list = []
        objs = storage.all()
        for key in objs.keys():
            if "State" in key:
                obj = objs[key]
                obj_list.append(obj.__str__())
            else:
                continue
        str_obj_list = str(obj_list) + "\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")
            test = f.getvalue()
            self.assertEqual(str_obj_list, test)

    def test_all_amenity(self):
        """Tests that all works for Amenity"""
        from models import storage

        obj_list = []
        objs = storage.all()
        for key in objs.keys():
            if "Amenity" in key:
                obj = objs[key]
                obj_list.append(obj.__str__())
            else:
                continue
        str_obj_list = str(obj_list) + "\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Amenity")
            test = f.getvalue()
            self.assertEqual(str_obj_list, test)


class TestAllCommandError(unittest.TestCase):
    """Tests the all command of the console with faulty input"""

    def test_all_wrong_class(self):
        """Tests that appropriate error is shown when all is
        called with a class that doesn't exist"""
        err_message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            test = f.getvalue()
            self.assertEqual(test, err_message)


class TestShowCommand(unittest.TestCase):
    """Tests the show command of the console with normal input"""

    def test_show_basemodel(self):
        """Tests that show works for BaseModel instance"""
        from models.base_model import BaseModel

        basemodel = BaseModel()
        expected = f"[{BaseModel.__name__}] ({basemodel.id})\
 {basemodel.__dict__}" + "\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {basemodel.id}")
            test = f.getvalue()
            self.assertEqual(test, expected)

    def test_show_user(self):
        """Tests that show works for User instance"""
        from models.user import User

        user = User()
        expected = f"[{User.__name__}] ({user.id}) {user.__dict__}" + "\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user.id}")
            test = f.getvalue()
            self.assertEqual(test, expected)

    def test_show_city(self):
        """Tests that show works for City instance"""
        from models.city import City

        city = City()
        expected = f"[{City.__name__}] ({city.id}) {city.__dict__}" + "\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show City {city.id}")
            test = f.getvalue()
            self.assertEqual(test, expected)


class TestShowCommandError(unittest.TestCase):
    """Tests the show command of the console with faulty input"""

    def test_show_no_class(self):
        """Tests that appropriate error is shown when show is
        called with no argument"""
        err_message = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_show_no_id(self):
        """Tests that appropriate error is shown when show is
        called with only the class"""
        err_message = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_show_wrong_class(self):
        """Tests that appropriate error is shown when show is
        called with a class that doesn't exist"""
        err_message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_show_wrong_id(self):
        """Tests that appropriate error is shown when show is
        called with an id that doesn't exist"""
        err_message = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 121212")
            test = f.getvalue()
            self.assertEqual(test, err_message)


class TestDestroyCommand(unittest.TestCase):
    """Tests the destroy command of the console with normal input"""

    def test_destroy_basemodel(self):
        """Tests that destroy works for BaseModel instance"""
        from models.base_model import BaseModel
        from models import storage

        basemodel = BaseModel()
        key = "BaseModel." + basemodel.id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {basemodel.id}")
            objs = storage.all()
            self.assertFalse(key in objs)

    def test_destroy_user(self):
        """Tests that destroy works for User instance"""
        from models.user import User
        from models import storage

        user = User()
        key = "User." + user.id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {user.id}")
            objs = storage.all()
            self.assertFalse(key in objs)

    def test_destroy_review(self):
        """Tests that destroy works for Review instance"""
        from models.review import Review
        from models import storage

        review = Review()
        key = "Review." + review.id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Review {review.id}")
            objs = storage.all()
            self.assertFalse(key in objs)


class TestDestroyCommandError(unittest.TestCase):
    """Tests the destroy command of the console with faulty input"""

    def test_destroy_no_class(self):
        """Tests that appropriate error is shown when destroy is
        called with no argument"""
        err_message = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_destroy_no_id(self):
        """Tests that appropriate error is shown when destroy is
        called with only the class"""
        err_message = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_destroy_wrong_class(self):
        """Tests that appropriate error is shown when destroy is
        called with a class that doesn't exist"""
        err_message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_destroy_wrong_id(self):
        """Tests that appropriate error is shown when destroy is
        called with an id that doesn't exist"""
        err_message = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_destroy_wrong_class_with_id(self):
        """Tests that appropriate error is shown when destroy is
        called with a class that doesn't exist even when id is present"""
        err_message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel 121212")
            test = f.getvalue()
            self.assertEqual(test, err_message)


class TestUpdateCommand(unittest.TestCase):
    """Tests the update command of the console with normal input"""

    def test_update_basemodel(self):
        """Tests that update works for BaseModel instance"""
        from models.base_model import BaseModel

        basemodel = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {basemodel.id}\
 first_name \"Betty\"")
            self.assertTrue(basemodel.first_name == "Betty")

    def test_update_user(self):
        """Tests that update works for User instance"""
        from models.user import User

        user = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {user.id}\
 email \"airbnb@mail.com\"")
            self.assertTrue(user.email, "airbnb@mail.com")

    def test_update_place(self):
        """Tests that update works for Place instance"""
        from models.place import Place

        place = Place()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Place {place.id} number_rooms 3")
            self.assertTrue(place.number_rooms, 3)


class TestUpdateCommandError(unittest.TestCase):
    """Tests the update command of the console with faulty input"""

    def test_update_no_class(self):
        """Tests that appropriate error is shown when update is
        called with no argument"""
        err_message = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_update_no_id(self):
        """Tests that appropriate error is shown when update is
        called with only the class"""
        err_message = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_update_wrong_class(self):
        """Tests that appropriate error is shown when update is
        called with a class that doesn't exist"""
        err_message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_update_wrong_id(self):
        """Tests that appropriate error is shown when destroy is
        called with an id that doesn't exist"""
        err_message = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 121212")
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_update_no_attr_name(self):
        """Tests that appropriate error is shown when update is
        called with missing attribute name"""
        from models.base_model import BaseModel

        basemodel = BaseModel()
        err_message = "** attribute name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {basemodel.id}")
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_update_no_attr_value(self):
        """Tests that appropriate error is shown when update is
        called with missing attribute value"""
        from models.base_model import BaseModel

        basemodel = BaseModel()
        err_message = "** value missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {basemodel.id} first_name")
            test = f.getvalue()
            self.assertEqual(test, err_message)


class TestAdvancedCreateCommand(unittest.TestCase):
    """Tests the create command of the console with normal input (advanced)"""

    def test_advanced_create_basemodel(self):
        """Tests that a new instance of BaseModel is created
        and shows the id of the instance"""
        from models import storage

        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("BaseModel.create()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            test_id = test.replace("\n", "")
            all_objs = storage.all()
            key = "BaseModel." + test_id
            self.assertTrue(key in all_objs)
            obj = all_objs[key]
            self.assertEqual(test_id, obj.id)

    def test_advanced_create_place(self):
        """Tests that a new instance of Place is created
        and shows the id of the instance"""
        from models import storage

        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("Place.create()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            test_id = test.replace("\n", "")
            all_objs = storage.all()
            key = "Place." + test_id
            self.assertTrue(key in all_objs)
            obj = all_objs[key]
            self.assertEqual(test_id, obj.id)

    def test_advanced_create_state(self):
        """Tests that a new instance of State is created
        and shows the id of the instance"""
        from models.state import State
        from models import storage

        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("State.create()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            test_id = test.replace("\n", "")
            all_objs = storage.all()
            key = "State." + test_id
            self.assertTrue(key in all_objs)
            obj = all_objs[key]
            self.assertEqual(test_id, obj.id)

    def test_advanced_create_amenity(self):
        """Tests that a new instance of Amenity is created
        and shows the id of the instance"""
        from models.amenity import Amenity
        from models import storage

        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity.create()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            test_id = test.replace("\n", "")
            all_objs = storage.all()
            key = "Amenity." + test_id
            self.assertTrue(key in all_objs)
            obj = all_objs[key]
            self.assertEqual(test_id, obj.id)


class TestAdvancedCreateCommandError(unittest.TestCase):
    """Tests the create command of the console with faulty input (advanced)"""

    def test_advanced_create_wrong_class(self):
        """Tests that appropriate error is shown when create is
        called with a class that doesn't exist"""
        err_message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("MyModel.create()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)


class TestAdvancedAllCommand(unittest.TestCase):
    """Tests the all command of the console with normal input (advanced)"""

    def test_advanced_all_basemodel(self):
        """Tests that all works for BaseModel"""
        from models import storage

        obj_list = []
        objs = storage.all()
        for key in objs.keys():
            if "BaseModel" in key:
                obj = objs[key]
                obj_list.append(obj.__str__())
            else:
                continue
        str_obj_list = str(obj_list) + "\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("BaseModel.all()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(str_obj_list, test)

    def test_advanced_all_place(self):
        """Tests that all works for Place"""
        from models import storage

        obj_list = []
        objs = storage.all()
        for key in objs.keys():
            if "Place" in key:
                obj = objs[key]
                obj_list.append(obj.__str__())
            else:
                continue
        str_obj_list = str(obj_list) + "\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("Place.all()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(str_obj_list, test)

    def test_advanced_all_state(self):
        """Tests that all works for State"""
        from models import storage

        obj_list = []
        objs = storage.all()
        for key in objs.keys():
            if "State" in key:
                obj = objs[key]
                obj_list.append(obj.__str__())
            else:
                continue
        str_obj_list = str(obj_list) + "\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("State.all()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(str_obj_list, test)

    def test_advanced_all_amenity(self):
        """Tests that all works for Amenity"""
        from models import storage

        obj_list = []
        objs = storage.all()
        for key in objs.keys():
            if "Amenity" in key:
                obj = objs[key]
                obj_list.append(obj.__str__())
            else:
                continue
        str_obj_list = str(obj_list) + "\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity.all()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(str_obj_list, test)


class TestAdvancedAllCommandError(unittest.TestCase):
    """Tests the all command of the console with faulty input"""

    def test_all_wrong_class(self):
        """Tests that appropriate error is shown when all is
        called with a class that doesn't exist"""
        err_message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("MyModel.all()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)


class TestCountCommand(unittest.TestCase):
    """Tests the count command of the console with normal input"""

    def test_count_basemodel(self):
        """Tests that count works for BaseModel"""
        from models import storage

        obj_count = 0
        objs = storage.all()
        for key in objs.keys():
            if "BaseModel" in key:
                obj_count += 1
            else:
                continue
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("BaseModel.count()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            count = str(obj_count) + "\n"
            self.assertEqual(count, test)

    def test_count_state(self):
        """Tests that count works for State"""
        from models import storage

        obj_count = 0
        objs = storage.all()
        for key in objs.keys():
            if "State" in key:
                obj_count += 1
            else:
                continue
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("State.count()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            count = str(obj_count) + "\n"
            self.assertEqual(count, test)

    def test_count_amenity(self):
        """Tests that count works for Amenity"""
        from models import storage

        obj_count = 0
        objs = storage.all()
        for key in objs.keys():
            if "Amenity" in key:
                obj_count += 1
            else:
                continue
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity.count()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            count = str(obj_count) + "\n"
            self.assertEqual(count, test)


class TestCountCommandError(unittest.TestCase):
    """Tests the count command of the console with faulty input"""

    def test_count_wrong_class(self):
        """Tests that appropriate error is shown when count is
        called with a class that doesn't exist"""
        err_message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("MyModel.count()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)


class TestAdvancedShowCommand(unittest.TestCase):
    """Tests the show command of the console with normal input (advanced)"""

    def test_advanced_show_basemodel(self):
        """Tests that show works for BaseModel instance"""
        from models.base_model import BaseModel

        basemodel = BaseModel()
        expected = f"[{BaseModel.__name__}] ({basemodel.id})\
 {basemodel.__dict__}" + "\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd(f'BaseModel.show("{basemodel.id}")')
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, expected)

    def test_advanced_show_user(self):
        """Tests that show works for BaseModel instance"""
        from models.user import User

        user = User()
        expected = f"[{User.__name__}] ({user.id}) {user.__dict__}" + "\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd(f'User.show("{user.id}")')
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, expected)

    def test_advanced_show_city(self):
        """Tests that show works for City instance"""
        from models.city import City

        city = City()
        expected = f"[{City.__name__}] ({city.id}) {city.__dict__}" + "\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd(f'City.show("{city.id}")')
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, expected)


class TestAdvancedShowCommandError(unittest.TestCase):
    """Tests the show command of the console with faulty input"""

    def test_advanced_show_no_class(self):
        """Tests that appropriate error is shown when show is
        called with no argument"""
        from models.city import City

        city = City()
        err_message = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd(f".show({city.id})")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_advanced_show_no_id(self):
        """Tests that appropriate error is shown when show is
        called with only the class"""
        err_message = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("City.show()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_advanced_show_wrong_class(self):
        """Tests that appropriate error is shown when show is
        called with a class that doesn't exist"""
        err_message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("MyModel.show()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_advanced_show_wrong_id(self):
        """Tests that appropriate error is shown when show is
        called with an id that doesn't exist"""
        err_message = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd('BaseModel.show("121212")')
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)


class TestAdvancedDestroyCommand(unittest.TestCase):
    """Tests the destroy command of the console with normal input"""

    def test_advanced_destroy_basemodel(self):
        """Tests that destroy works for BaseModel instance"""
        from models.base_model import BaseModel
        from models import storage

        basemodel = BaseModel()
        key = "BaseModel." + basemodel.id
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd(f'BaseModel.destroy("{basemodel.id}")')
            HBNBCommand().onecmd(line)
            objs = storage.all()
            self.assertFalse(key in objs)

    def test_advanced_destroy_user(self):
        """Tests that destroy works for User instance"""
        from models.user import User
        from models import storage

        user = User()
        key = "User." + user.id
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd(f'User.destroy("{user.id}")')
            HBNBCommand().onecmd(line)
            objs = storage.all()
            self.assertFalse(key in objs)

    def test_advanced_destroy_review(self):
        """Tests that destroy works for Review instance"""
        from models.review import Review
        from models import storage

        review = Review()
        key = "Review." + review.id
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd(f'Review.destroy("{review.id}")')
            HBNBCommand().onecmd(line)
            objs = storage.all()
            self.assertFalse(key in objs)


class TestAdvancedDestroyCommandError(unittest.TestCase):
    """Tests the destroy command of the console with faulty input"""

    def test_advanced_destroy_no_class(self):
        """Tests that appropriate error is shown when destroy is
        called with no argument"""
        from models.review import Review
        from models import storage

        review = Review()
        err_message = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd(f".destroy({review.id})")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_advanced_destroy_no_id(self):
        """Tests that appropriate error is shown when destroy is
        called with only the class"""
        err_message = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("BaseModel.destroy()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_advanced_destroy_wrong_class(self):
        """Tests that appropriate error is shown when destroy is
        called with a class that doesn't exist"""
        err_message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("MyModel.destroy()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_advanced_destroy_wrong_id(self):
        """Tests that appropriate error is shown when destroy is
        called with an id that doesn't exist"""
        err_message = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd('BaseModel.destroy("121212")')
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_advanced_destroy_wrong_class_with_id(self):
        """Tests that appropriate error is shown when destroy is
        called with a class that doesn't exist even when id is present"""
        err_message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("MyModel.destroy(121212)")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)


class TestAdvancedUpdateCommand(unittest.TestCase):
    """Tests the update command of the console with normal input (advanced)"""

    def test_advanced_update_basemodel(self):
        """Tests that update works for BaseModel instance (advanced)"""
        from models.base_model import BaseModel

        basemodel = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd(f'BaseModel.update("{basemodel.id}",\
 \'first_name\', \"Betty\")')
            HBNBCommand().onecmd(line)
            self.assertTrue(basemodel.first_name == "Betty")

    def test_advanced_update_basemodel_with_dict(self):
        """Tests that update works for BaseModel instance
 using a dictionary (advanced)"""
        from models.base_model import BaseModel

        basemodel = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd(f'BaseModel.update("{basemodel.id}",\
 {{\'first_name\': "Betty", \'last_name\': "Bar"}})')
            HBNBCommand().onecmd(line)
            self.assertTrue(basemodel.first_name == "Betty")
            self.assertTrue(basemodel.last_name == "Bar")

    def test_advanced_update_user(self):
        """Tests that update works for User instance"""
        from models.user import User

        user = User()
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd(f'User.update("{user.id}",\
 email, \"airbnb@mail.com\")')
            HBNBCommand().onecmd(line)
            self.assertTrue(user.email, "airbnb@mail.com")

    def test_advanced_update_place(self):
        """Tests that update works for Place instance"""
        from models.place import Place

        place = Place()
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd(f'Place.update("{place.id}", \
number_rooms, 3)')
            HBNBCommand().onecmd(line)
            self.assertTrue(place.number_rooms, 3)


class TestAdvancedUpdateCommandError(unittest.TestCase):
    """Tests the update command of the console with faulty input (advanced)"""

    def test_advanced_update_no_id(self):
        """Tests that appropriate error is shown when update is
        called with only the class"""
        err_message = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("BaseModel.update()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_advanced_update_wrong_class(self):
        """Tests that appropriate error is shown when update is
        called with a class that doesn't exist"""
        err_message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("MyModel.update()")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_advanced_update_wrong_id(self):
        """Tests that appropriate error is shown when destroy is
        called with an id that doesn't exist"""
        err_message = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd('BaseModel.update("1212121")')
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_advanced_update_no_attr_name(self):
        """Tests that appropriate error is shown when update is
        called with missing attribute name"""
        from models.base_model import BaseModel

        basemodel = BaseModel()
        err_message = "** attribute name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd(f'BaseModel.update("{basemodel.id}")')
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_advanced_update_no_attr_value(self):
        """Tests that appropriate error is shown when update is
        called with missing attribute value"""
        from models.base_model import BaseModel

        basemodel = BaseModel()
        err_message = "** value missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd(f'BaseModel.update("{basemodel.id}",\
 \'first_name\')')
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_advanced_update_basemodel_with_dict_wrong_id(self):
        """Tests that appropriate error is shown when destroy is
        called with an id that doesn't exist"""
        err_message = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("BaseModel.update(121212,\
 {'first_name': \"Betty\", 'last_name': \"Bar\"})")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)

    def test_advanced_update_basemodel_with_dict_wrong_class(self):
        """Tests that appropriate error is shown when destroy is
        called with a class that doesn't exist"""
        err_message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            line = HBNBCommand().precmd("MyModel.update(121212,\
 {'first_name': \"Betty\", 'last_name': \"Bar\"})")
            HBNBCommand().onecmd(line)
            test = f.getvalue()
            self.assertEqual(test, err_message)
