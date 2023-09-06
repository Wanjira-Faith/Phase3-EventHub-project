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

   