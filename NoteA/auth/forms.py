from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange
from models import User


class UserLogin(FlaskForm):
    Username = StringField('Username', validators=[DataRequired()])
    Password = PasswordField('Password', validators=[DataRequired()])
    Login = SubmitField('Login')


class CreateAccount(FlaskForm):
    Username = StringField('Username', validators=[DataRequired()])
    Password = PasswordField('Password', validators=[DataRequired()])
    PasswordRetype = PasswordField('PasswordRetype', validators=[DataRequired(), EqualTo('Password', 'Passwords must match')])
    CreateAccount = SubmitField('CreateAccount')

    def validate_username(self, Username):
        user = User.query.filter_by(username=Username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')