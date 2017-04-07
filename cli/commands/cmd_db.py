import click
from app import create_app, db

app = create_app()
db.app = app


@click.group()
def cli():
    """ DB related commands. """
    pass


@click.command()
def init():
    """ Initialize the db. """
    db.drop_all()
    db.create_all()
    print('Droppped and created db')


cli.add_command(init)
