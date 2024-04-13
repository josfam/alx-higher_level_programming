#!/usr/bin/python3

"""Prints the first state returned from a query of existing states
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
        print('Nothing')
    else:
        print('{}: {}'.format(first_state.id, first_state.name))

    session.close()
