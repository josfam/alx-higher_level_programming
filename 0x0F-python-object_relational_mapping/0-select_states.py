#!/usr/bin/python3

"""Uses MySQLdb to interact with a MYSQL database"""

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
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")

    for pair in cur.fetchall():
        print(pair)

    cur.close()
    db.close()
