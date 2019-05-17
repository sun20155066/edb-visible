from flask import (Flask,render_template,redirect,url_for)


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__,static_folder="templates")
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev',
    )

    # register the database commands
    from flaskr import db
    db.init_app(app)

    # apply the blueprints to the app
    from flaskr import auth,visible,web

    app.register_blueprint(auth.bp)
    app.register_blueprint(visible.bp)
    app.register_blueprint(web.bp)

    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    return app






