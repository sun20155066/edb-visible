import os

from flask import (Flask,render_template)


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev',
    )

    # register the database commands
    from flaskr import db
    db.init_app(app)

    # apply the blueprints to the app
    from flaskr import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('base.html')

    return app






