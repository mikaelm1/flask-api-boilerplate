from flask import Blueprint, jsonify, g, request
from .models import User, db

user = Blueprint('user', __name__)


@user.route('/users')
def index():
    users = User.query.all()
    return jsonify({'response': [u.to_json() for u in users]}), 200


@user.route('/users/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    if username and password and email:
        if User.find_by_identity(username) or User.find_by_identity(email):
            return jsonify({'response':
                           {'message':
                            'User with that email or username already exists'}}), 400
        elif len(password.strip()) < 6:
            return jsonify({'response':
                           {'message':
                            'Password must be at least 6 characters long'}}), 400
        elif len(username.strip()) < 3:
            return jsonify({'response':
                           {'message':
                            'Username must be at least 3 characters long'}}), 400
        user = User(username=username.lower(),
                    email=email.lower(), password=password)
        session_token = user.generate_auth_token(3600)
        user.session_token = session_token
        db.session.add(user)
        db.session.commit()
        g.current_user = user
        response = user.to_json()
        return jsonify({"response": response}), 200
    else:
        return jsonify({'response':
                       {'message': 'Invalid values provided'}}), 500


@user.route('/users/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username and password:
        user = User.find_by_identity(username)
        if user and user.authenticated(password):
            g.current_user = user
            session_token = user.generate_auth_token(3600)
            user.session_token = session_token
            db.session.commit()
            response = user.to_json()
            return jsonify({'response': response}), 200
        else:
            return jsonify({'response':
                           {'message': 'Username or password is wrong'}}), 404
    return jsonify({'response':
                   {'message': 'Password and username not provided'}}), 500
