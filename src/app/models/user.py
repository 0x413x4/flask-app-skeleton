import validators
from app import db, login
from flask_login import UserMixin
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(id):
    """ Flask-Login User Loader Function """
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    """
    User Class
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(256), index=True, unique=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    # Password hash should only be accessed through helper functions
    _password_hash = db.Column(db.String(128))
    projects = db.relationship('Project', backref='owner', lazy='dynamic')
    dummy_var = db.Column(db.String(64))

    """
    Constructor and dunder methods
    """
    def __init__(self, username, email, firstname='', lastname='',
                 password=None):
        self.username = username
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        if password:
            self.set_password(password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    """
    Field validation
    """
    @validates('username')
    def validate_username(self, key, username):
        if not username:
            # Username cannot be Null
            raise AssertionError('No username provided.')

        if User.query.filter_by(username=username).first():
            # Username must be unique
            raise AssertionError('User is already in use')

        if len(username) > 32:
            # Username cannot exceed 32 chars
            raise AssertionError('Username must be 32 charactes maximum')

        if not validators.slug(username):
            # Username should only accept a restricted set of characters
            message = 'The username can only contain alphanumeric characters, hyphens and underscores.'
            raise AssertionError(message)

        return username

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            # Email cannot be Null
            raise AssertionError('No email provided.')

        if User.query.filter_by(email=email).first():
            # Email address must be unique
            raise AssertionError('Email address is already in use.')

        if len(email) > 256:
            # Email address cannot exceed 256 characters
            raise AssertionError('Email address cannot exceed 256 characters.')

        if not validators.email(email):
            # Email complies with RFC 8398
            raise AssertionError('Provided email is not an email address.')

        return email

    @validates('firstname', 'lastname')
    def validate_name(self, key, value):
        if len(value) > 64:
            # Value cannot exceed 64 characters
            message = 'First and lastnames cannot exceed 64 characters'
            raise AssertionError(message)

        if not validators.slug(value) and value != '':
            # Username should only accept a restricted set of characters
            message = 'First and lastnames can only contain alphanumeric characters, hyphens and underscores.'
            raise AssertionError(message)

        return value

    """
    Helper functions
    """
    def set_password(self, password):
        """ Set user password """
        self._password_hash = generate_password_hash(password)

    def check_password(self, password):
        """ Check user password """
        return check_password_hash(self._password_hash, password)

    def save(self):
        """ Save user object to database """
        db.session.add(self)
        db.session.commit()
