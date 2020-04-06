from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask_login import current_user
from database.models import *


class SearchForm(FlaskForm):
    search_type = SelectField('Search Options', validators=[DataRequired()],
                              choices=[('albums', 'Album'), ('artists', 'Artist'), ('genres', 'Genre')])
    search_name = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')


class InventoryAccessForm(FlaskForm):
    search_type = SelectField('Inventory Options', validators=[DataRequired()],
                              choices=[('records', 'Records'), ('artists', 'Artists')])
    submit = SubmitField('Alter Inventory')


class RecordInventoryAccessForm(FlaskForm):
    update_type = SelectField("Record Inventory", validators=[DataRequired()],
                              choices=[('add', 'Add'), ('delete', 'Delete'), ('update', 'Update')])
    submit = SubmitField('Update Record')


class ArtistInventoryAccessForm(FlaskForm):
    update_type = SelectField('Artist Inventory', validators=[DataRequired()],
                              choices=[('add', 'Add'), ('delete', 'Delete'), ('update', 'Update')])
    submit = SubmitField('Update Artist')


class UpdateInventoryAccessForm(FlaskForm):
    update_type = SelectField('Update Inventory', validators=[DataRequired()],
                              choices=[('add', 'Add'), ('delete', 'Delete'), ('update', 'Update')])
    submit = SubmitField('Update')


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    street_address = StringField('Street Address')
    city_address = StringField('City')
    state_address = StringField('State')
    zip_code = StringField('Zip Code')
    submit = SubmitField('Update Account Info')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
