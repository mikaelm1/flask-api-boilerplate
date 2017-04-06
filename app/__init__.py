from flask import Flask


def create_app(setting_overrides=None):
    """
    Create a Flask application using the factory pattern.
    :param settings_overrides: dict Override default app settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings', silent=True)

    return app
