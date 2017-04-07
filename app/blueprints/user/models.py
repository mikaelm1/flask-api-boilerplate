from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.String(64), nullable=False, index=True,
                     server_default='member')
    email = db.Column(db.String(128), unique=True, nullable=False, index=True)
    username = db.Column(db.String(64), unique=True, nullable=False,
                         index=True)
    password = db.Column(db.String(128), nullable=False)
    session_token = db.Column(db.String(512))
    is_active = db.Column(db.Boolean(), nullable=False, server_default='1')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = User.encrypt_password(kwargs.get('password'))

    def __repr__(self):
        return '<User %r>'.format(self.username)

    def to_json(self):
        res = {
            'email': self.email,
            'username': self.username,
            'session_token': self.session_token
        }
        return res

    @classmethod
    def encrypt_password(cls, password):
        """
        Hash a plaintext password.
        :param password: str Plaintext password
        :return: str Hashed password
        """
        return generate_password_hash(password)

    def authenticated(self, password):
        """
        Authenticate plaintext password against hashed password saved in
        the db.
        :param password: str Plaintext password
        :return: bool
        """
        return check_password_hash(self.password, password)

    def generate_auth_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    # DB Helpers
    @classmethod
    def find_by_identity(cls, identity):
        """
        Find a user by either their email or username.
        :param identity: Email or username
        """
        return User.query.filter(
            (User.email == identity) | (User.username == identity)).first()
