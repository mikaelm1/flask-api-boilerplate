import os
import click
import shutil


@click.group()
def cli():
    """
    Utilility commands.
    """
    pass


@click.command(name='create')
@click.argument('name')
def create_blueprint(name):
    """
    Creates a new blueprint.
    """
    print('Creating {} Blueprint...'.format(name))
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
        s_code = ('from flask import Blueprint, jsonify, g, request\n'
                  'from .models import {}\n\n\n'
                  '{} = Blueprint(\'{}\', __name__)\n'
                  .format(name.title(), name, name))
        f.write(s_code)
    with open(model, 'w+') as f:
        m_code = ('from datetime import datetime\n'
                  'from app import db\n\n\n'
                  'class {}(db.Model):\n'
                  '    __tablename__ = \'{}s\'\n\n'
                  '    id = db.Column(db.Integer, primary_key=True)\n'
                  '    created_on = db.Column(db.DateTime, default=datetime.utcnow)\n'
                  .format(name.title(), name))
        f.write(m_code)
    print('Adding test file for {}...'.format(name))
    filename = './app/tests/test_{}s.py'.format(name)
    if os.path.isdir(filename):
        print('A test file with that name already exists')
        return
    with open(filename, 'w+') as f:
        t_code = ('from .test_base import BaseTest\n\n\n'
                  'class {}TestCase(BaseTest):\n'
                  '    pass\n'.format(name.title()))
        f.write(t_code)


@click.command(name='delete')
@click.argument('name')
def remove_blueprint(name):
    """
    Deletes a blueprint and all of its contents.
    """
    msg = 'Are you sure you want to delete the {} Blueprint?'.format(name)
    if click.confirm(msg):
        print('Deleting {} Blueprint...'.format(name))
        shutil.rmtree('./app/blueprints/{}'.format(name))
    else:
        print('Canceled delete')


cli.add_command(create_blueprint)
cli.add_command(remove_blueprint)
