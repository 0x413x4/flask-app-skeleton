import os
from dotenv import load_dotenv


base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, '.env'))


class Config(object):
    # Key used by WTF to generate Anti CSRF tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Get DB URI from the environment or fallback to a local SQLITE DB
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(base_dir, 'app-skeleton.db')

    # signal the application every time a change is about to be made in the
    # database
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG=True
    TESTING=True
