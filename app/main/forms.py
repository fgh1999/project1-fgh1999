from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm


class UserForm(FlaskForm):
    # form config
    name = StringField('Username', validators=[DataRequired()])
    pwd = PasswordField('Password', validators=[Length(9, 15)])
    submit = SubmitField('确定')
