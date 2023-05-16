# Airbnb Clone - The Console
<p align="center">
  <img src="https://www.aydentownsley.com/img/hbnb.png"  width="60%" height="30%" align="center">
</p>

## Description

This is the first part in the series of four Airbnb Clones project series at ALX Africa.The goal is to build the backend of the project and a console for a client-side. Data is converted to json and stored in a file for whenever it is needed. This project was developed with `python object oriented programming`

## Description of the Console
The console is just like the bash shell, the only difference being that it can only perform limited actions and are restricted to the use of managing data/objects. This will serve as the client-side for users. It was built with the help of the python ```cmd module```

What can the console do?
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Files and Directories
* `models` directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
* `tests` directory will contain all unit tests.
* `console.py` file is the entry point of our command interpreter.
* `models/base_model.py` file is the base class of all our models. It contains common elements:
* `attributes`: id, created_at and updated_at
* `methods`: save() and to_json()
* `models/engine` directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.

## How to execute
To execute in interactive mode, run this command.
```bash
./console.py
```
In interactive mode (i.e passing commands through keyboard, stdin), 
```bash
vagrant@ubuntu-focal:~/AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
(hbnb) quit
vagrant@ubuntu-focal:~/AirBnB_clone$
$
```
In non-interactive mode (passing command through files or text),
```bash
vagrant@ubuntu-focal:~/AirBnB_clone$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
vagrant@ubuntu-focal:~/AirBnB_clone$ cat test_help
help
vagrant@ubuntu-focal:~/AirBnB_clone$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
vagrant@ubuntu-focal:~/AirBnB_clone$
```

## How to Use the Commands
1. ``Help``: Typing help will show you the list of commands avaliable
```bash
vagrant@ubuntu-focal:~/AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```
Typing help followed by a command will show you a short documentation about the command
```bash
(hbnb) help create
Creates a new instance of the given class,
        saves it (to the JSON file) and prints the id
```

2. ``create``: this creates a new data/instance
Usage:
* ``create <class name>``
```bash
(hbnb) create User
48e0069e-01f3-4ff8-8164-56aa7abca7b6
```

3. ``all``: This prints out all the objects

Usage:
* ``all <class name>`` or ``<class name>.all()``
* ``all``
```bash
(hbnb) all
["[User] (6a1b7225-27e3-4bc1-9c68-922200ff502c) {'id': '6a1b7225-27e3-4bc1-9c68-922200ff502c', 'created_at': datetime.datetime(2023, 5, 16, 3, 45, 17, 532423), 'updated_at': datetime.datetime(2023, 5, 16, 3, 45, 17, 532530)}", "[BaseModel] (2f92d5ba-8dc7-43f0-a945-5abf325f47e7) {'id': '2f92d5ba-8dc7-43f0-a945-5abf325f47e7', 'created_at': datetime.datetime(2023, 5, 16, 3, 45, 29, 444048), 'updated_at': datetime.datetime(2023, 5, 16, 3, 45, 29, 444070)}"]
(hbnb) all User
["[User] (6a1b7225-27e3-4bc1-9c68-922200ff502c) {'id': '6a1b7225-27e3-4bc1-9c68-922200ff502c', 'created_at': datetime.datetime(2023, 5, 16, 3, 45, 17, 532423), 'updated_at': datetime.datetime(2023, 5, 16, 3, 45, 17, 532530)}"]
(hbnb) User.all()
["[User] (6a1b7225-27e3-4bc1-9c68-922200ff502c) {'id': '6a1b7225-27e3-4bc1-9c68-922200ff502c', 'created_at': datetime.datetime(2023, 5, 16, 3, 45, 17, 532423), 'updated_at': datetime.datetime(2023, 5, 16, 3, 45, 17, 532530)}"]
(hbnb)
```
  
4. ``show``: this prints out the string representation of the id passed

Usage:
* ```show <class name> <id>```
* ```<class name>.show("<id>")```

```bash
(hbnb) show User 6a1b7225-27e3-4bc1-9c68-922200ff502c
[User] (6a1b7225-27e3-4bc1-9c68-922200ff502c) {'id': '6a1b7225-27e3-4bc1-9c68-922200ff502c', 'created_at': datetime.datetime(2023, 5, 16, 3, 45, 17, 532423), 'updated_at': datetime.datetime(2023, 5, 16, 3, 45, 17, 532530)}
(hbnb) User.show("6a1b7225-27e3-4bc1-9c68-922200ff502c")
[User] (6a1b7225-27e3-4bc1-9c68-922200ff502c) {'id': '6a1b7225-27e3-4bc1-9c68-922200ff502c', 'created_at': datetime.datetime(2023, 5, 16, 3, 45, 17, 532423), 'updated_at': datetime.datetime(2023, 5, 16, 3, 45, 17, 532530)}
(hbnb)
```
  
5. ``destroy``: this destroys an instance

Usage:
* ```destroy <class name> <id>``` or ``<class name>.destroy("<id>")``
```bash
(hbnb) all User
["[User] (6a1b7225-27e3-4bc1-9c68-922200ff502c) {'id': '6a1b7225-27e3-4bc1-9c68-922200ff502c', 'created_at': datetime.datetime(2023, 5, 16, 3, 45, 17, 532423), 'updated_at': datetime.datetime(2023, 5, 16, 3, 45, 17, 532530)}"]
(hbnb) destroy User 6a1b7225-27e3-4bc1-9c68-922200ff502c
(hbnb) all User
[]
(hbnb)
```
  
6. ``update``: This updates an instance based on the class name and id by adding or updating attribute
  
  Usage:
  * ``update <class name> <id> <attribute name> "<attribute value>"``
  * ``<class name>.update("<id>", "<attribute name>", "<attribute value>")``
  * ``<class name>.update("<id>", <python dictionary>)``

**Note**: typing ``enter`` on the console will do nothing
```bash
(hbnb) all
["[BaseModel] (2f92d5ba-8dc7-43f0-a945-5abf325f47e7) {'id': '2f92d5ba-8dc7-43f0-a945-5abf325f47e7', 'created_at': datetime.datetime(2023, 5, 16, 3, 45, 29, 444048), 'updated_at': datetime.datetime(2023, 5, 16, 3, 45, 29, 444070)}"]
(hbnb)
(hbnb) create User
875ca4b2-9e57-4faa-a09f-31ec5cae75e5
(hbnb)
(hbnb) all
["[BaseModel] (2f92d5ba-8dc7-43f0-a945-5abf325f47e7) {'id': '2f92d5ba-8dc7-43f0-a945-5abf325f47e7', 'created_at': datetime.datetime(2023, 5, 16, 3, 45, 29, 444048), 'updated_at': datetime.datetime(2023, 5, 16, 3, 45, 29, 444070)}", "[User] (875ca4b2-9e57-4faa-a09f-31ec5cae75e5) {'id': '875ca4b2-9e57-4faa-a09f-31ec5cae75e5', 'created_at': datetime.datetime(2023, 5, 16, 4, 1, 55, 494066), 'updated_at': datetime.datetime(2023, 5, 16, 4, 1, 55, 494095)}"]
(hbnb)
(hbnb) User.update("875ca4b2-9e57-4faa-a09f-31ec5cae75e5", "Name", "James")
(hbnb)
(hbnb) User.show("875ca4b2-9e57-4faa-a09f-31ec5cae75e5")
[User] (875ca4b2-9e57-4faa-a09f-31ec5cae75e5) {'id': '875ca4b2-9e57-4faa-a09f-31ec5cae75e5', 'created_at': datetime.datetime(2023, 5, 16, 4, 1, 55, 494066), 'updated_at': datetime.datetime(2023, 5, 16, 4, 3, 23, 813876), 'Name': 'James'}
(hbnb)
(hbnb)  update User 875ca4b2-9e57-4faa-a09f-31ec5cae75e5 Hobby "coding"
(hbnb)
(hbnb) User.show("875ca4b2-9e57-4faa-a09f-31ec5cae75e5")
[User] (875ca4b2-9e57-4faa-a09f-31ec5cae75e5) {'id': '875ca4b2-9e57-4faa-a09f-31ec5cae75e5', 'created_at': datetime.datetime(2023, 5, 16, 4, 1, 55, 494066), 'updated_at': datetime.datetime(2023, 5, 16, 4, 5, 58, 819808), 'Name': 'James', '"Hobby"': 'coding'}
(hbnb)
(hbnb) User.update("875ca4b2-9e57-4faa-a09f-31ec5cae75e5", {'first_name': "John", "age": 89})
(hbnb) User.show("875ca4b2-9e57-4faa-a09f-31ec5cae75e5")
[User] (875ca4b2-9e57-4faa-a09f-31ec5cae75e5) {'id': '875ca4b2-9e57-4faa-a09f-31ec5cae75e5', 'created_at': datetime.datetime(2023, 5, 16, 4, 1, 55, 494066), 'updated_at': datetime.datetime(2023, 5, 16, 4, 7, 14, 990551), 'Name': 'James', '"Hobby"': 'coding', 'first_name': 'John', 'age': '89'}
(hbnb)
```
7. ``quit``: this exits the console
```bash
(hbnb) User.show("875ca4b2-9e57-4faa-a09f-31ec5cae75e5")
[User] (875ca4b2-9e57-4faa-a09f-31ec5cae75e5) {'id': '875ca4b2-9e57-4faa-a09f-31ec5cae75e5', 'created_at': datetime.datetime(2023, 5, 16, 4, 1, 55, 494066), 'updated_at': datetime.datetime(2023, 5, 16, 4, 7, 14, 990551), 'Name': 'James', '"Hobby"': 'coding', 'first_name': 'John', 'age': '89'}
(hbnb) quit
vagrant@ubuntu-focal:~/AirBnB_clone$
```
  
## Authors
* Olayinkascott Andee (andeeolayinkascott@gmail.com)
* Tobi Tijani (tobi_tijani@yahoo.com)
