#!/usr/bin/python3
"""Takes an argument and displays all values in the states table
of htbn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    match = sys.argv[4]
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
