from datetime import datetime
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
    email_confirmed = db.Column(db.Boolean(), server_default='0')
    session_token = db.Column(db.String(512))
    is_active = db.Column(db.Boolean(), nullable=False, server_default='1')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return '<User %r>'.format(self.username)

    def to_json(self):
        res = {
            'email': self.email,
            'username': self.username,
            'session_token': self.session_token
        }
        return res
