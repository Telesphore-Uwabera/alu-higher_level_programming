#!/usr/bin/python3
"""
Creates the State
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Add cities to different states
    california = State(name='California')
    san_francisco = City(name='San Francisco')
    san_jose = City(name='San Jose')
    los_angeles = City(name='Los Angeles')
    fremont = City(name='Fremont')
    livermore = City(name='Livermore')

    arizona = State(name='Arizona')
    page = City(name='Page')
    phoenix = City(name='Phoenix')

    texas = State(name='Texas')
    dallas = City(name='Dallas')
    huston = City(name='Huston')
    austin = City(name='Austin')

    new_york = State(name='New York')
    new_york_city = City(name='New York')

    nevada = State(name='Nevada')
    las_vegas = City(name='Las Vegas')
    reno = City(name='Reno')
    henderson = City(name='Henderson')
    carson_city = City(name='Carson City')

    # Add cities to their respective states
    california.cities.append(san_francisco)
    california.cities.append(san_jose)
    california.cities.append(los_angeles)
    california.cities.append(fremont)
    california.cities.append(livermore)

    arizona.cities.append(page)
    arizona.cities.append(phoenix)

    texas.cities.append(dallas)
    texas.cities.append(huston)
    texas.cities.append(austin)

    new_york.cities.append(new_york_city)

    nevada.cities.append(las_vegas)
    nevada.cities.append(reno)
    nevada.cities.append(henderson)
    nevada.cities.append(carson_city)

    # Add states to session and commit changes
    session.add(california)
    session.add(arizona)
    session.add(texas)
    session.add(new_york)
    session.add(nevada)
    session.commit()

    # Add another city to California and commit changes
    san_francisco_ca = City(name='San Francisco', state=california)
    session.add(san_francisco_ca)
    session.commit()
