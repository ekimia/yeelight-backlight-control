import os

from flask import Flask


DEBUG = True


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )


    #  Logging
    app.url_map.strict_slashes = False

    _configure_blueprints(app)

    #  a simple page that says hello
    @app.route('/status')
    def hello():
        return 'Hello, World!'

    return app


def _configure_blueprints(app: Flask):
    # apply the blueprints to the app
    from yeelight_control import yeelight_control
    app.register_blueprint(yeelight_control.bp)
