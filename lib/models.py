from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define database connection
engine = create_engine('sqlite:///event_hub.db', echo=True)

# Base class for all classes
Base = declarative_base()

# Many-to-Many Relationship Table (Events - Speakers)
event_speaker_association = Table(
    'event_speaker_association',
    Base.metadata,
    Column('event_id', Integer, ForeignKey('events.id')),
    Column('speaker_id', Integer, ForeignKey('speakers.id'))
)

class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    date = Column(Date)
    description = Column(String(255))
    capacity = Column(Integer)


    # Define the many-to-many relationship with speakers
    speakers = relationship('Speaker', secondary=event_speaker_association, back_populates='events')


class Participant(Base):
    __tablename__ = 'participants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))  

class Speaker(Base):
    __tablename__ = 'speakers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    # Define the many-to-many relationship with events
    events = relationship('Event', secondary=event_speaker_association, back_populates='speakers')


class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))    
        
    