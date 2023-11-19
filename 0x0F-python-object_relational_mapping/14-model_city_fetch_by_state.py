#!/usr/bin/python3

"""
Lists all city objects from the database hbtn_0e_6_usa
"""
from model_city import City
from model_state import Base, State
from sys import argv

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).join(State).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
