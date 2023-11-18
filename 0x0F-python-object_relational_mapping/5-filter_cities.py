#!/usr/bin/python3

"""
A script that lists all cities of a state from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    states_name = argv[4]

    query = """SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s ORDER BY cities.id ASC"""
    cur.execute(query, (states_name,))
    query_rows = cur.fetchall()

    cities = ", ".join(city[0] for city in query_rows)
    print(cities)
    cur.close()
    conn.close()
