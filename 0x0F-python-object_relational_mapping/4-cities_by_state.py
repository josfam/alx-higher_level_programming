#!/usr/bin/python3

"""Uses MySQLdb to interact with a MYSQL database.

Question snippet:
Write a script that lists all cities, by state, from the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        user=db_user,
        passwd=db_password,
        database=db_name,
        host='localhost',
        port=3306,
    )

    cur = db.cursor()
    command = """
        SELECT
        cities.id,
        cities.name,
        (
            SELECT states.name
            FROM states
            WHERE states.id = cities.state_id
        ) AS state_name
        FROM cities
        ORDER BY cities.id ASC;
    """
    cur.execute(command)

    for pair in cur.fetchall():
        print(pair)

    cur.close()
    db.close()
