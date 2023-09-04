from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define database connection
engine = create_engine('sqlite:///event_hub.db')

# Base class for all classes
Base = declarative_base()
