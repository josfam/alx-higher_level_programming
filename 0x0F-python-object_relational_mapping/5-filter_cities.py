#!/usr/bin/python3

"""Uses MySQLdb to interact with a MYSQL database.

Question snippet:
Write a script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        user=db_user,
        passwd=db_password,
        database=db_name,
        host='localhost',
        port=3306,
    )

    cur = db.cursor()
    command = """
        SELECT cities.name
        FROM cities
        WHERE state_id =
        (
            SELECT id
            FROM states
            WHERE name = %s
        );
    """
    cur.execute(command, (state,))

    cities = []
    for city in cur.fetchall():
        cities.extend(list(city))
    print(', '.join(cities))

    cur.close()
    db.close()
