# Flask
SECRET_KEY = 'supersecret'
SERVER_NAME = 'localhost:8000'
SQLALCHEMY_RECORD_QUERIES = True
DEBUG = True

# Database
SQLALCHEMY_DATABASE_URI = 'postgresql://potter:voldemort@postgres:5432/potter'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_RECORD_QUERIES = True


# Mail
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'example@gmail.com'
MAIL_PASSWORD = 'supersecret'
CC_MAIL_SUBJECT_PREFIX = '[Flask Boilerplate]'
CC_MAIL_SENDER = 'Flask Boilerplate <flask@example.com>'
