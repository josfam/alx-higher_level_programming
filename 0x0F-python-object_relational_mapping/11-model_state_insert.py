#!/usr/bin/python3

"""Adds the state `Louisiana` to the database
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

    session.add(State(name='Alabama'))
    session.commit()
    # print the new state's id
    new_state = session.query(State).filter(State.name == 'Alabama').first()
    print(new_state.id)
    session.close()
