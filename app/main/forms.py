from wtforms import StringField,TextAreaField, SubmitField, SelectField 
from wtforms.validators import Required, Email, Length
from flask_wtf import FlaskForm

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell Us About Yourself...',validators = [Required()])
    submit = SubmitField('Submit')

class UpdateProfileForm(FlaskForm):
    name = StringField('Name', validators=[Required(), Length(1, 64)])
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    bio = TextAreaField('About...', validators=[Required(), Length(1, 100)])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    pitch_title = StringField('Pitch title', validators=[Required()])
    pitch_category = SelectField('Pitch category',choices=[('Select a category','Select a category'),('Pickup lines', 'Pickup lines'),('Interview','Interview'),('Religion','Religion'),('Business','Business')], validators=[Required()])
    pitch_content = StringField('What is in your mind?')
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Body', validators=[Required()])
    submit = SubmitField('Submit')
    
