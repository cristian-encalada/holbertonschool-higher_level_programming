#!/usr/bin/python3
"""Script that deletes all State objects with a name containing the letter a
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    )

    Session = sessionmaker(engine)
    session = Session()

    states = (
        session.query(State, City)
        .filter(State.id == City.state_id)
        .all()
    )

    for state, city in states:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
