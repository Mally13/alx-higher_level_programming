#!/usr/bin/python3
"""
Contains the class definition of a State and an instance
Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Defines the State class that inherits from Base
    Args:
    __tablename__: Name of table yo store states
    id: state's id
    name: state's name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
