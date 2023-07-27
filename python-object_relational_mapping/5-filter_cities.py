#!/usr/bin/python3
"""Script that takes in the name of a state as an argument
and lists all cities of that state"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = ("""SELECT cities.name FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name LIKE BINARY %s""")
    cur.execute(query, (argv[4],))
    cities = cur.fetchall()
    # Add the city names into a list
    city_names = []
    for city in cities:
        city_names.append(city[0])
    # Join the city names with commas
    cities_str = ", ".join(city_names)
    print(cities_str)
    db.close()
