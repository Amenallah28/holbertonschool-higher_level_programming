#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys


def main(username, passsword, db_name, state_name):
    """
    Access to the database and get the states
    from the database.
    """

    db = MySQLdb.connect(
        host="localhost", user=username, port=3306, passwd=passsword, db=db_name
    )
    cur = db.cursor()

    cur.execute(
        """
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """,
        {"name": state_name},
    )
    [print(state) for state in cur.fetchall()]


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    main(username, password, db_name, state_name)
