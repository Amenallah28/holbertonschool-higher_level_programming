#!/usr/bin/python3
"""
script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main(username, password, db_name, state_name):
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
    state = session.query(State).filter_by(name=state_name).first()

    # Print the State id that contains state name
    if state is not None:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    main(username, password, db_name, state_name)
    