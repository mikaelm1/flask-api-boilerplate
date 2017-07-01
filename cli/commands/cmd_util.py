import os
import click
import shutil


@click.group()
def cli():
    """
    Utilility commands.
    """
    pass


@click.command(name='cb')
@click.argument('name')
def create_blueprint(name):
    """
    Creates a new blueprint.
    """
    print('Creating {}...'.format(name))
    filename = './app/blueprints/{}/__init__.py'.format(name)
    if os.path.isdir('./app/blueprints/{}'.format(name)):
        print('A blueprint with that name already exists')
        return
    os.makedirs(os.path.dirname(filename))
    route = './app/blueprints/{}/routes.py'.format(name)
    model = './app/blueprints/{}/models.py'.format(name)
    with open(filename, 'w+') as f:
        f.write('')
    with open(route, 'w+') as f:
        s_code = ('from flask import Blueprint, jsonify, g, request\n\n\n'
                  '{} = Blueprint(\'{}\', __name__)\n'.format(name, name))
        f.write(s_code)
    with open(model, 'w+') as f:
        f.write('')


@click.command(name='rb')
@click.argument('name')
def remove_blueprint(name):
    """
    Deletes a blueprint and all of its contents.
    """
    msg = 'Are you sure you want to delete the {} Blueprint?'.format(name)
    if click.confirm(msg):
        print('Deleting {} Blueprint...'.format(name))
        shutil.rmtree('./app/blueprints/{}'.format(name))


cli.add_command(create_blueprint)
cli.add_command(remove_blueprint)
