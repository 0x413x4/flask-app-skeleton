import validators
from app import db
from app.models.user import User
from datetime import datetime
from sqlalchemy.orm import validates


class Project(db.Model):
    """
    Project Class
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    client = db.Column(db.String(64), index=True)
    description = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    """
    Constructor and dunder methods
    """
    def __init__(self, name, owner, client='', description=''):
        self.name = name
        self.client = client
        self.description = description
        self.owner = owner

    def __repr__(self):
        return '<Project: {}>'.format(self.name)

    """
    Field validation
    """
    def validate_project_name(self, key, name):
        if not name:
            # Project name must exist
            raise AssertionError('Project name cannot be null.')

        if Project.query.filter_by(name=name).first():
            # Project name must be unique
            raise AssertionError('This project already exists.')

        if len(name) > 64:
            # Name should not exceed 64 chars
            raise AssertionError('Project name cannot exceed 64 characters.')

        if not validators.slug(name) and name != '':
            # Username should only accept a restricted set of characters
            message = 'Project name can only contain alphanumeric characters, hyphens and underscores.'
            raise AssertionError(message)

        return name

    def validate_client_name(self, key, client):
        if not client:
            # Client name must exist
            raise AssertionError('Client name cannot be null.')

        if len(client) > 64:
            # Name should not exceed 64 chars
            raise AssertionError('Client name cannot exceed 64 characters.')

        if not validators.slug(client) and client != '':
            # Username should only accept a restricted set of characters
            message = 'Client name can only contain alphanumeric characters, hyphens and underscores.'
            raise AssertionError(message)

        return client

    @validates('description')
    def validate_description(self, key, description):
        if description is None:
            # Description can be empty but not null
            raise AssertionError('Description cannot be null.')

        if len(description) > 140:
            # Description cannot exceed 140 characters
            raise AssertionError('Description cannot exceed 140 characters.')

        if '<' in description or '>' in description:
            raise AssertionError('Description cannot contain brackets')

        return description

    @validates('user_id')
    def validate_user_id(self, key, user_id):
        if not user_id:
            # User ID cannot be null
            raise AssertionError('User ID cannot be null.')

        if not isinstance(user_id, int):
            # User ID is an Integer
            raise AssertionError('User ID must be an Integer.')

        if not User.query.filter_by(id=user_id).first():
            # User ID must be associated to an existing user
            raise AssertionError('User does not exist.')

        return user_id

    """
    Helper functions
    """
    def save(self):
        """ Save project object to database """
        db.session.add(self)
        db.session.commit()
