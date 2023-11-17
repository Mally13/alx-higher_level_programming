#!/usr/bin/python3

"""
Filters states that start with N from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM `states` ORDER BY `id` ASC"
    )
    query_rows = cur.fetchall()
    for state in query_rows:
        if (state[1][0] == "N"):
            print(state)
    cur.close()
    conn.close()
