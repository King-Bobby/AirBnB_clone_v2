#!/usr/bin/python3
"""
Defines Class DatabaseStorage/DBstorage
"""


from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import Base
from models.state import State
from models.city import City


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Create engine and link to MySQL databse (hbnb_dev, hbnb_dev_db)"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        envv = getenv("HBNB_ENV", "none")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        if envv == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query the current database session"""
        dictionary = {}

        if cls != "":
            objects = self.__session.query(models.classes[cls]).all()
            for obj in objects:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                dictionary[key] = obj
            return dictionary
        else:
            for key, value in models.classes.items():
                if key != "BaseModel":
                    objects = self.__session.query(v).all()
                    if len(objects) > 0:
                        for obj in objects:
                            key = "{}.{}".format(obj.__class__.__name__,
                                                 obj.id)
                            dictionary[key] = obj
            return dictionary

    def new(self, obj):
        """ add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create the current database session"""
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        """remove private session attributes"""
        self.__session.close()
