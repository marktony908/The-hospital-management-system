# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Create the database engine
engine = create_engine('sqlite:///hospital.db')

# Create a configured "Session" class
Session = sessionmaker(bind=engine)
