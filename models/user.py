#!/usr/bin/python3
"""This is the user class implementation"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class User(BaseModel, Base):
    """defines a class for user
    Attributes:
        email
        password
        first_name
        last_name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
