#!/bin/bash

# Enter MySQL credentials
MYSQL_USER="your_username"
MYSQL_PASSWORD="your_password"

# Get a list of all databases
DATABASES=$(mysql -u $MYSQL_USER -p$MYSQL_PASSWORD -e "SHOW DATABASES;" | grep -Ev "(Database|information_schema|performance_schema)")

# Loop through the list and output each database name
for DB in $DATABASES; do
  echo "- $DB"
done
