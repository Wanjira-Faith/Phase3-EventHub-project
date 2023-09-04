from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define database connection
engine = create_engine('sqlite:///event_hub.db', echo=True)

# Base class for all classes
Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    date = Column(Date)
    description = Column(String(255))
    capacity = Column(Integer)

class Participant(Base):
    __tablename__ = 'participants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))  

class Speaker(Base):
    __tablename__ = 'speakers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))    
        
    