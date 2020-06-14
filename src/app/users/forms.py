from app.models.user import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp
from wtforms.validators import ValidationError


# Validators
# EqualTo is passed as a function so we can pass parameters to it.
_veq = EqualTo
_vreq = DataRequired()
_vml32 = Length(max=32)
_vml64 = Length(max=64)
_vml128 = Length(max=128)
_vml256 = Length(max=256)
_vemail = Email()
_valnum = Regexp('^[a-zA-Z0-9_-]*$', message="This field only allows \
                 alphanumeric characters, along with '-' and '_'.")


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[_vreq, _vml32, _valnum])
    email = StringField('Email', validators=[_vreq, _vml256, _vemail])
    password = PasswordField('Password', validators=[_vreq, _vml128])
    password2 = PasswordField('Confirm', validators=[_vreq, _vml128,
                                                     _veq('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        # Check the username is unique
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('Please use a different email address.')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[_vreq, _vml32, _valnum])
    firstname = StringField('Firstname', validators=[_vml32, _valnum])
    lastname = StringField('Lastname', validators=[_vml32, _valnum])
    submit_profile = SubmitField('Save')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class ChangeEmailForm(FlaskForm):
    email = StringField('Email', validators=[_vreq, _vml256, _vemail])
    password = PasswordField('Current Password', validators=[_vreq, _vml128])
    submit_email = SubmitField('Save')

    def __init__(self, original_email, *args, **kwargs):
        super(ChangeEmailForm, self).__init__(*args, **kwargs)
        self.original_email = original_email

    def validate_email(self, email):
        if email.data != self.original_email:
            email = User.query.filter_by(email=email.data).first()
            if email is not None:
                raise ValidationError('Please use a different email address.')


class ChangePasswordForm(FlaskForm):
    password = PasswordField('Current Password', validators=[_vreq, _vml128])
    new_password = PasswordField('New Password', validators=[_vreq, _vml128])
    new_password2 = PasswordField('Confirm', validators=[_vreq, _vml128,
                                                         _veq('new_password')])
    submit = SubmitField('Submit')
