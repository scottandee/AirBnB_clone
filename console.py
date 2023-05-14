#!/usr/bin/python3
"""
HBNBCommand Class
This module contains the definition of the HBNBCommand Class
that inherits from the Cmd class in the cmd module
"""

import ast
import re
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models import storage
CLASSES = dir()


class HBNBCommand(cmd.Cmd):
    """Defines the HBNBCommand class that inherits from the
    Cmd class in the cmd module"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exits the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Determines what happens with an empty line + ENTER"""
        pass

    def precmd(self, line):
        if not sys.stdin.isatty():
            print()

        if "(" not in line:
            return line
        line = line.strip()
        compiled = []
        cmd_string = re.compile(r'((?<=\.)[a-z]+(?=\())')
        cmd = re.search(cmd_string, line)
        if cmd is None:
            cmd = ''
            compiled.append(cmd)
        if cmd.group(0) == 'update':
            if '{' in line:
                HBNBCommand().convert(line)
                return ""
        if cmd is not None:
            compiled.append(cmd.group(0))

        klass_str = re.compile(r'(^\w+)')
        klass = re.search(klass_str, line)
        if klass is None:
            klass = ''
            compiled.append(klass)
        else:
            compiled.append(klass.group(0))

        args_str = re.compile(r'(?<="|\s|\')[a-z0-9A-Z-_@\.]+')
        args = re.findall(args_str, line)
        if args is not None:
            for arg in args:
                compiled.append(arg)
        joined = " ".join(compiled)
        return joined

    def convert(self, line):
        compiled = []
        klass_str = re.compile(r'(^\w+)')
        klass = re.search(klass_str, line)
        if klass is None:
            klass = ''
        compiled.append(klass.group(0))

        args_str = re.compile(r'(?<="|\s|\')[a-z0-9A-Z-_@\.]+')
        args = re.findall(args_str, line)
        if len(args) == 1:
            compiled.append(args[0])
            joined = joined = " ".join(compiled)
            HBNBCommand().do_update(joined)
        elif args is not None:
            compiled.append(args[0])
            pair = []
            copy = compiled.copy()
            for i in range(1, len(args)):
                pair.append(args[i])
                if i % 2 == 0:
                    copy.extend(pair)
                    joined = " ".join(copy)
                    HBNBCommand().do_update(joined)
                    copy = compiled.copy()
                    pair = []
            if len(pair) != 0:
                copy.extend(pair)
                joined = " ".join(copy)
                HBNBCommand().do_update(joined)
        else:
            joined = joined = " ".join(compiled)
            HBNBCommand().do_update(joined)

    def do_count(self, line):
        """Retrieve the number of instances of a class"""
        if not line:
            print("** class name missing **")
            return
        class_name = line
        num = 0
        if class_name in CLASSES:
            objs = storage.all()
            for keys in objs:
                if class_name in keys:
                    num += 1
                else:
                    continue
            print(num)
        else:
            print("** class doesn't exist **")

    def do_create(self, line):
        """Creates a new instance of the given class,
        saves it (to the JSON file) and prints the id"""
        if not line:
            print("** class name missing **")
            return
        class_name = line
        if class_name in CLASSES:
            klass = globals()[class_name]
            instance = klass()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in CLASSES:
            if len(args) == 1:
                print("** instance id missing **")
                return
        else:
            print("** class doesn't exist **")
            return
        class_name, instance_id = args
        key = class_name + "." + instance_id
        all_objs = storage.all()
        if key in all_objs:
            obj = all_objs[key]
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in CLASSES:
            if len(args) == 1:
                print("** instance id missing **")
                return
        else:
            print("** class doesn't exist **")
            return
        class_name, instance_id = args
        key = class_name + "." + instance_id
        all_objs = storage.all()
        if key in all_objs:
            del (all_objs[key])
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name."""
        args = line.split()
        objs_list = []
        all_objs = storage.all()
        if len(args) == 0:
            for key in all_objs.keys():
                obj = all_objs[key]
                objs_list.append(obj.__str__())
        elif len(args) == 1:
            class_name = args[0]
            if class_name in CLASSES:
                for key in all_objs.keys():
                    if class_name in key:
                        obj = all_objs[key]
                        objs_list.append(obj.__str__())
                    else:
                        continue
            else:
                print("** class doesn't exist **")
                return
        print(objs_list)

    def do_update(self, line):
        """Updates an instance based on the class name and
 id by adding or updating attribute"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in CLASSES:
            if len(args) == 1:
                print("** instance id missing **")
                return
            elif len(args) == 2:
                print("** attribute name missing **")
                return
            elif len(args) == 3:
                print("** value missing **")
                return
        else:
            print("** class doesn't exist **")
            return
        class_name = args[0]
        instance_id = args[1]
        attr_name = args[2]
        if "\"" in args[3]:
            value = args[3].replace("\"", "")
        else:
            value = args[3]
        key = class_name + "." + instance_id
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        obj = all_objs[key]
        if attr_name in type(obj).__dict__:
            attr_type = type(type(obj).__dict__[attr_name])
            attr_val = attr_type(value)
        else:
            attr_val = value
        setattr(obj, attr_name, attr_val)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
