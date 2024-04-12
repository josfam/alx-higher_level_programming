#!/usr/bin/python3

"""Uses MySQLdb to interact with a MYSQL database.
Specifically, lists all states with a name starting with `N` (upper N) from the
database `hbtn_0e_0_usa`
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        user=db_user,
        password=db_password,
        database=db_name,
        host='localhost',
        port=3306,
    )

    cur = db.cursor()
    command = """SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"""
    cur.execute(command)

    for pair in cur.fetchall():
        print(pair)

    cur.close()
