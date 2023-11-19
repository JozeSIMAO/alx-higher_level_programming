#!/usr/bin/python3
"""prints the State object with the name
passed as argument from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    name = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    find_name = (session.query(State)
                 .filter(State.name == name)
                 .first())

    if find_name is not None:
        print("{}".format(find_name.id))
    else:
        print("Not found")

    session.close()
