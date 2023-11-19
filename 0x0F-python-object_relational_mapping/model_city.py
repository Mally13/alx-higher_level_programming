#!/usr/bin/python3
"""
Contains the class definition of a City that inherits from
Base imported from state
"""
from sqlalchemy import ForeignKey, Column, Integer, String

from model_state import Base, State


class City (Base):
    """Defines the City class that inherits from Base
    Args:
    __tablename__: Name of table to store cities
    id: city's id
    name: city's name
    states_id: foreign key to states.id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
