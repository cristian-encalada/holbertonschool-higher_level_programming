#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT id, name FROM cities ORDER BY id"
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)
    db.close()
