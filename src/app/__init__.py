import logging
import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler


# Database
db = SQLAlchemy()
migrate = Migrate()

# Login manager
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'You must log in to access this page.'

# CSS Framework
bootstrap = Bootstrap()


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Logging configuration
    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')

        file_handler = RotatingFileHandler('logs/app-skeleton.log',
                                           maxBytes=10240,
                                           backupCount=10)

        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: \
             %(message)s [in %(pathname)s:%(lineno)d]'))

        file_handler.setLevel(logging.INFO)

        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Project mongoose startup')

    # Import and register blueprints
    # Main application
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Authentication module
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # User management
    from app.users import bp as users_bp
    app.register_blueprint(users_bp)

    # Error Blueprint
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    return app


# Bottom import to avoid circular imports
from app import models
