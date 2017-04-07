import unittest
import json
import os
from flask import url_for

from app import create_app, db
from app.blueprints.user.models import User


class BaseTest(unittest.TestCase):
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        db_uri = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
        params = {
            'DEBUG': False,
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': db_uri,
            'LIMITER_ENABLED': False
        }
        self.app = create_app(settings_override=params)
        self.app_context = self.app.app_context()
        self.app_context.push()
        with self.app_context:
            db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        with self.app_context:
            db.session.remove()
            db.drop_all()
        self.app_context.pop()

    def user_dict(self, seed):
        return dict(
            email='user' + str(seed) + '@example.com',
            username='user' + str(seed),
            password='secret')

    def register_user(self, seed):
        user = User(
            email='user' + str(seed) + '@example.com',
            username='user' + str(seed),
            password='secret')
        db.session.add(user)
        db.session.commit()
        return user

    def get_api_headers(self, token=None):
        header = {'Accept': 'application/json',
                  'Content-Type': 'application/json'}
        if token:
            header['Authorization'] = 'Token ' + str(token)
        return header

    def token_for_user(self, user):
        response = self.client.post(url_for('user.login'),
                                    headers=self.get_api_headers(),
                                    data=json.dumps(self.user_dict(user.id)))
        json_response = json.loads(response.data.decode('utf-8')).get('response')
        token = json_response.get('session_token')
        return token
