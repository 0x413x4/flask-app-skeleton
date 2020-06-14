from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


# Validators
# EqualTo is passed as a function so we can pass parameters to it.
_vreq = DataRequired()
_vml32 = Length(max=32)
_vml128 = Length(max=128)
_valnum = Regexp('^[a-zA-Z0-9_-]*$', message="This field only allows \
                 alphanumeric characters, along with '-' and '_'.")


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[_vreq, _vml32, _valnum])
    password = PasswordField('Password', validators=[_vreq, _vml128])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
