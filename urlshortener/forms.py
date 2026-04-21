from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Optional, Length, Regexp

class URLShortenForm(FlaskForm):
    original_url = StringField('Long URL', validators=[
        DataRequired(message="Please enter a URL"),
        URL(message="Please enter a valid URL (include http/https)")
    ])
    custom_alias = StringField('Custom Alias (Optional)', validators=[
        Optional(),
        Length(min=3, max=50),
        Regexp(r'^[a-zA-Z0-9_-]+$', message="Alias can only contain letters, numbers, hyphens, and underscores")
    ])
    submit = SubmitField('Shorten Now')
