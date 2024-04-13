#!/usr/bin/python3
"""Fetches all states from the database.

Qn:
Write a script that prints the first State object from the database
hbtn_0e_6_usa
"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            db_user, db_password, db_name
        )
    )

    # session for db communication
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).first()  # the first state
    if not first_state:
        pass
    else:
        print('{}: {}'.format(first_state.id, first_state.name))

    session.close()
