from flask import Blueprint
from .models import User

user = Blueprint('user', __name__)


@user.route('/users')
def index():
    return 'Users index'


@user.route('/users/register', methods=['POST'])
def register():
    return 'Register'


@user.route('/users/login', methods=['POST'])
def login():
    return 'Login'
