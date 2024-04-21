#!/usr/bin/python3

"""database abstraction storage class "DBStorage" """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import os
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """DB storage class
    """

    __engine = None
    __session = None

    def __init__(self):
        """create the engine (self.__engine)"""

        usr = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        db = os.getenv("HBNB_MYSQL_DB")
        host = os.getenv("HBNB_MYSQL_HOST")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(usr, password, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)
        all objects depending of the class name """

        class_list = [State, City, User, Place, Review, Amenity]
        dict = {}

        if cls is None:
            for clss in class_list:
                results = self.__session.query(clss)
                for result in results:
                    dict[result.__class__.__name__ + '.' + result.id] = result
            return dict

        if cls.__class__ == str:
            classa = eval(cls)
            results = self.__session.query(classa).all()
            for result in results:
                dict[result.__class__.__name__ + '.' + result.id] = result
            return dict

    def new(self, obj):
        """add new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """save changes in db
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in table of db
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        start_session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = sqlalchemy.orm.scoped_session(start_session)
        self.__session = Session()

    def close(self):
        """ calls close() of the current session
        """
        self.__session.close()
