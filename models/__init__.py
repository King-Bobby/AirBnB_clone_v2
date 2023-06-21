#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""


from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


envv = getenv("HBNB_TYPE_STORAGE", "fs")
if envv == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}

storage.reload()
