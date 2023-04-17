#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa"""

#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=db_name)

    # Create cursor to execute queries
    cursor = db.cursor()

    # Execute the query to get cities of a given state
    cursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ASC", (state_name,))

    # Fetch all the rows as a list of tuples
    rows = cursor.fetchall()

    # Print the results
    for city in cities:
        print(", ".join(city[0] for city in cursor.fetchall()))

    # Close cursor and database connection
    cursor.close()
    db.close()
