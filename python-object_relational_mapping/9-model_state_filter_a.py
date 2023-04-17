#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Creating engine and connecting to the database
    db_url = f"mysql+mysqldb://{mysql_username}:{mysql_password}\
            @localhost:3306/{database_name}"
    engine = create_engine(db_url)

    # Creating metadata
    Base.metadata.create_all(engine)

    # Creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying database for states containing letter 'a'
    query = session.query(State).filter(State.name.like('%a%')).\
            order_by(State.id)

    # Displaying the results
    for state in query.all():
        print(f"{state.id}: {state.name}")

    # Closing the session
    session.close()
