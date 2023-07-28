#!/usr/bin/python3
"""Script that that prints the first State object
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    )

    Session = sessionmaker(engine)
    session = Session()

    states = (
        session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    )

    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()
