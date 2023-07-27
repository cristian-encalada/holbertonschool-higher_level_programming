#!/usr/bin/python3
"""Script that lists all states with a name starting with N"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    # Execute the SQL query
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id"
    cur.execute(query)
    states = cur.fetchall()
    # Print each state
    for state in states:
        print(state)
    db.close()
