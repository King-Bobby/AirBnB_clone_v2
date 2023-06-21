#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""


from os import getenv


envv = getenv("HBNB_TYPE_STORAGE", "fs")
if envv == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
