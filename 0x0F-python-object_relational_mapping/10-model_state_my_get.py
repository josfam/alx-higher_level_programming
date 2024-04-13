#!/usr/bin/python3

"""Prints the id of the state that matches the given state, if it exists.
Otherwise, prints `Not found`
"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            db_user, db_password, db_name
        )
    )

    # session for db communication
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == state_name)
    if states.count() == 0:
        print('Not found')
    for state in states:
        print(state.id)

    session.close()
