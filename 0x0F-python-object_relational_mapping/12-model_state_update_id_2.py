#!/usr/bin/python3

"""Updates the name of the state with the id 2 to `New Mexico`
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

    state = session.query(State).filter(State.id == 2)
    state.update({'name': 'New Mexico'})
    session.commit()
    session.close()
