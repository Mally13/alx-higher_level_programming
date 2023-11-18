#!/usr/bin/python3

"""
Prints the State object with the name passed as argument from
the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state_query = "{}".format(argv[4])
    state_found = session.query(State).filter(
        State.name == state_query).first()
    if (state_found):
        print("{}".format(state_found.id))
    else:
        print("Not found")
