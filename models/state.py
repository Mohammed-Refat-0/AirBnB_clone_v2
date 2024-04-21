#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """ return all cities in the storage assosicated with the state """
        vars = models.storage.all()
        add = []
        result = []
        for key in vars:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                add.append(vars[key])
        for i in add:
            if (i.state_id == self.id):
                result.append(i)
        return (result)
