import click
from models import Base, Event, Participant, Speaker, Venue
from utils import create_session, create_db_engine

engine = create_db_engine()
Base.metadata.create_all(engine)

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Event Name', help='Name of the event')
@click.option('--date', prompt='Event Date (YYYY-MM-DD)', help='Date of the event')
@click.option('--description', prompt='Event Description', help='Description of the event')
@click.option('--capacity', prompt='Event Capacity', type=int, help='Maximum capacity of the event')
def create_event(name, date, description, capacity):
    """Create a new event."""

# Create a session using create_session from utils.py
    session = create_session(engine)   

    event = Event(name=name, date=date, description=description, capacity=capacity)
    session.add(event)
    session.commit()

    click.echo(f'Event "{name}" created successfully.')

# Register a participant for an event
@cli.command()
@click.option('--event-name', prompt='Event Name', help='Name of the event')
@click.option('--participant-name', prompt='Participant Name', help='Name of the participant')
def register_participant(event_name, participant_name):
    """Register a participant for an event."""
  
    # Create a session using create_session from utils.py
    session = create_session(engine)    

    # Find the event by name
    event = session.query(Event).filter_by(name=event_name).first()
