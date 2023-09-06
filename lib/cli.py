import click
from models import Base, Event, Participant, Speaker, Venue
from utils import create_session, create_db_engine

engine = create_db_engine()
Base.metadata.create_all(engine)

@click.group()
def cli():
    pass

   