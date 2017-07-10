from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import logging
from logging.handlers import RotatingFileHandler


db = SQLAlchemy()
mail = Mail()


def create_app(settings_override=None):
    """
    Create a Flask application using the factory pattern.
    :param settings_override: dict Override default app settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings', silent=True)
    if settings_override:
        app.config.update(settings_override)
    # Extensions
    db.init_app(app)
    mail.init_app(app)
    # Logging
    app_logger(app)
    # Blueprints
    from app.blueprints.user.routes import user
    app.register_blueprint(user, url_prefix='/api/v1')

    @app.route('/health')
    def health_check():
        app.logger.info('Got request to /health route')
        return jsonify({'response': {'message': 'App is healthy'}}), 200

    return app


def app_logger(app):
    """
    Set up logger for the app.
    :param app: The Flask app
    :return: None
    """
    format_string = (
        '=================================================================\n'
        '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s\n'
        '=================================================================\n'
        )
    formatter = logging.Formatter(format_string)
    handler = RotatingFileHandler(filename='logs/app.log', maxBytes=10000000,
                                  backupCount=1)
    handler.setLevel(app.config['LOG_LEVEL'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    return
