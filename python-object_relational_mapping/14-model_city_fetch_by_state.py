#!/usr/bin/env python3
"""Module for fetching cities by state."""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    database = argv[3]

    # Prepare ORM engine
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}",
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create session and fetch states with their cities
    session = sessionmaker(bind=engine)()
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Print results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
