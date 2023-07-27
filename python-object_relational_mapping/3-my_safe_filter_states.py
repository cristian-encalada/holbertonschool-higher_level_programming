#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
It must be safe from MySQL injections"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    # Execute the SQL query
    query = ("""SELECT * FROM states WHERE name
            LIKE BINARY '%{}%' ORDER BY id""".format(argv[4]))
    cur.execute(query)
    states = cur.fetchall()
    # Print each state
    for state in states:
        print(state)
    db.close()
