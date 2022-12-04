#!/usr/bin/python3
"""
Script to display all rows of states table
where name matches argument
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':

    dbs = db.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    with dbs.cursor() as dbc:
        dbc.execute(
            "SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states ON cities.state_id \
                = states.id ORDER BY cities.id ASC")
        rows = dbc.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
