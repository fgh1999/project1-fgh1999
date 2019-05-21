from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm


class UserForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    pwd = PasswordField('Password', validators=[Length(9, 15)])
    submit = SubmitField('确定')


class SearchForm(FlaskForm):
    isbn = StringField('ISBN')
    title = StringField('Title', validators=[Length(0, 100)])
    author = StringField('Author', validators=[Length(0, 30)])
    submit = SubmitField('查找')


class ReviewForm(FlaskForm):
    content = StringField('Content', validators=[Length(0, 65535)])
    submit = SubmitField('添加评论')

