# Flask
SECRET_KEY = 'supersecret'
SERVER_NAME = 'localhost:8000'
SQLALCHEMY_RECORD_QUERIES = True
DEBUG = True

# Database
SQLALCHEMY_DATABASE_URI = 'postgresql://potter:voldemort@postgres:5432/potter'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_RECORD_QUERIES = True

# Logging
LOG_LEVEL = 'DEBUG'

# Mail
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'example@gmail.com'
MAIL_PASSWORD = 'supersecret'
CC_MAIL_SUBJECT_PREFIX = '[Flask Boilerplate]'
CC_MAIL_SENDER = 'Flask Boilerplate <flask@example.com>'

# Mobile Push Notifications
ONE_SIGNAL_KEY = 'REST API Key'
ONE_SIGNAL_APP_ID = 'One Signal App ID'
