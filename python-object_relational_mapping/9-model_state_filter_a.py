#!/usr/bin/python3
"""
script that lists all State objects that contain the letter a
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main(username, password, db_name):
    """
    Access to the database and get the states
    from the database.
    """
    # Create the database connection
    cnt = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    # Create the engine
    engine = create_engine(cnt)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query the State object
    first_state = session.query(State).order_by(State.id)

    # Print the State name that contains "a"
    if first_state is not None:
        for state in first_state.filter(State.name.contains("a")):
            print("{}: {}".format(state.id, state.name))
    # Close the session
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    main(username, password, db_name)
