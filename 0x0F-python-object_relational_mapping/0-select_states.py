#!/usr/bin/python3

import MySQLdb
from sys import argv

"""Lists all states from database hbtn_0e_0_usa"""
if __name__ == "__main__":
    """Lists all states from database hbtn_0e_0_usa"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
