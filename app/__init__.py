from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


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

    # Blueprints
    from app.blueprints.user.routes import user
    app.register_blueprint(user, url_prefix='/api/v1')

    @app.route('/health')
    def health_check():
        return jsonify({'response': {'message': 'App is healthy'}}), 200

    return app
