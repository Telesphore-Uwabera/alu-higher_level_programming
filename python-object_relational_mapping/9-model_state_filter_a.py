#!/usr/bin/python3
"""
lists all State objects that contain the letter a
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Set up connection to the database
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    engine = create_engine(
        "mysql+mysqldb://" + mysql_username + ":" + mysql_password +
        "@localhost:3306/" + database_name, pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the database for State objects that contain the letter 'a'
    query = session.query(State)\
            .filter(State.name.like('%a%')).order_by(State.id)

    # Print out the results
    for state in query:
        print("{}: {}".format(state.id, state.name))
