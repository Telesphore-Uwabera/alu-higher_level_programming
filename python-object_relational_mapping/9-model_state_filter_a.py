#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create connection to the database
    db_url = f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}"
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database
    query = session.query(State).filter(State.name.contains('a')).order_by(State.id)

    # Print the results
    for state in query.all():
        print("{}: {}".format(state.id, state.name))
