from flask import Blueprint, jsonify
from .models import User

user = Blueprint('user', __name__)


@user.route('/users')
def index():
    users = User.query.all()
    return jsonify({'response': [u.to_json() for u in users]}), 200


@user.route('/users/register', methods=['POST'])
def register():
    return 'Register'


@user.route('/users/login', methods=['POST'])
def login():
    return 'Login'
