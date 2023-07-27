#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    # Create a cursor to interact with the database
    cur = db.cursor()
    # Execute the SQL query
    query = "SELECT * FROM states ORDER BY id"
    cur.execute(query)
    # Fetch all rows as a list
    states = cur.fetchall()
    # Print each state
    for state in states:
        print(state)
    # Close the database connection
    db.close()
