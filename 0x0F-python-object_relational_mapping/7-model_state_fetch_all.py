#!/usr/bin/python3

"""Fetches all states from the database.

Qn:
Write a script that lists all State objects from the database hbtn_0e_6_usa
"""

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

all_states = session.query(State).order_by(State.id.asc())
for state in all_states:
    print('{}: {}'.format(state.id, state.name))

session.close()
