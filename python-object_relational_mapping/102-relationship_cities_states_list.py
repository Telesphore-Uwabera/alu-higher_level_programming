#!/usr/bin/env python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    # Get credentials from command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL server
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")

    # Create metadata and session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database to retrieve all City objects
    query = session.query(City).order_by(City.id).all()

    # Print the City objects and their corresponding State objects
    for city in query:
        print(f"{city.id}: {city.name} -> {city.state.name}")
