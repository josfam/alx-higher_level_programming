#!/usr/bin/python3

"""Uses MySQLdb to interact with a MYSQL database.

Question:
Write a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
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
    db.close()
