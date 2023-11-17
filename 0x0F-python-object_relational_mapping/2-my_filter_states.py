#!/usr/bin/python3

"""
A script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
Usage:
./1-filter_states.py <mysql username> <mysql password> \
<database name> <state name>
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Takes in an argument and displays all values in the state table
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    state_name = argv[4]
    cur.execute("SELECT * FROM states WHERE name = %s", (state_name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
