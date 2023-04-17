#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get the MySQL username, password, database name, and state name as arguments
    username, password, database, state_name = sys.argv[1:]

    # Establish a connection to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute a SELECT statement to retrieve all cities of the specified state, ordered by id
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    # Retrieve all the rows returned by the query and print them to the console
    cities = cur.fetchall()
    for city in cities:
        print(city)

    # Close the cursor and database connections to release resources
    cur.close()
    db.close()
