#!/usr/bin/python3
"""
cript that adds the State object “Louisiana”
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main(username, password, db_name):
    """
    cript that adds the State object “Louisiana”
    """
    # Create the database connection
    cnt = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    # Create the engine
    engine = create_engine(cnt)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query the states and print it
    our_user = State(name="Louisiana")
    session.add(our_user)
    session.commit()
    print(our_user.id)
    # Close the session
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    main(username, password, db_name)
