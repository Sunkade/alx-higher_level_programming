from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

# Replace 'mysql://user:password@localhost:3306/database' with your actual MySQL connection string
db_url = 'mysql://user:password@localhost:3306/database'
engine = create_engine(db_url, echo=True)  # Set echo to True for debugging purposes

# Create the table
Base.metadata.create_all(engine)

# Example of using the State class with a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a new state
new_state = State(name='New State')
session.add(new_state)
session.commit()

# Query the states
states = session.query(State).all()
for state in states:
    print(f"State ID: {state.id}, Name: {state.name}")

# Don't forget to close the session
session.close()
