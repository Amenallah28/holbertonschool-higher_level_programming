#!/usr/bin/python3
"""
script that lists all cities from
the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def main(username, passsword, db_name):
    """
    lists all cities
    """

    db = MySQLdb.connect(
        host="localhost", user=username, port=3306, passwd=passsword, db=db_name
    )
    cur = db.cursor()

    cur.execute(
        """
            SELECT
                cities.id, cities.name ,states.name
            FROM
                states

                INNER JOIN cities
                ON states.id =  cities.state_id;
                ORDER BY  cities.id ASC;
        """,
    )
    [print(cities) for cities in cur.fetchall()]


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    main(username, password, db_name)
