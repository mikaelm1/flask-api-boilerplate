from flask import g, jsonify
from flask_httpauth import HTTPTokenAuth
from .models import User

auth = HTTPTokenAuth(scheme='Token')


@auth.verify_token
def verify_token(token):
    g.current_user = User.verify_auth_token(token)
    return g.current_user is not None


@auth.error_handler
def auth_eror():
    return jsonify({'response': {'message': 'Invalid token'}}), 400
