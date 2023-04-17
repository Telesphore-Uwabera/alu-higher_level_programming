#!/usr/bin/python3
"""module documentation"""
import MySQLdb
import sys

# Get command line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
search = sys.argv[4]

# Connect to MySQL server
db = MySQLdb.connect(host="localhost",
                     user=username,
                     passwd=password,
                     db=database)

cur = db.cursor()

# Use a parameterized query to avoid SQL injection
query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
cur.execute(query, (search,))

# Fetch all the rows and display them
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the database connection
cur.close()
db.close()
