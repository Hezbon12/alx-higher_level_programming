#!/usr/bin/python3
"""
update state: given id, change state name
parameters given to script: username, password, database

"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # make engine for database
    mysql username = argv[1]
    mysql password = argv[2]
    database name = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                            format(mysql username, mysql password, database name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # add new state and commit to table
    new = State(name="Louisiana")
    session.add(new)
    session.commit()

    print("{:d}".format(new.id))

    session.close()
