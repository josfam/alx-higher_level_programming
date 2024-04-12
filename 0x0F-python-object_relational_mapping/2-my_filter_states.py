#!/usr/bin/python3

"""Uses MySQLdb to interact with a MYSQL database.

Question snippet:
Once again, write a script that takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    to_find = sys.argv[4]

    db = MySQLdb.connect(
        user=db_user,
        password=db_password,
        database=db_name,
        host='localhost',
        port=3306,
    )

    cur = db.cursor()
    command = """SELECT * FROM states WHERE name='{}'"""
    cur.execute(command.format(to_find))

    for pair in cur.fetchall():
        print(pair)

    cur.close()
    db.close()
