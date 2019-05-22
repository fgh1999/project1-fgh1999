from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm


class UserForm(FlaskForm):
    name = StringField('用户名', validators=[Length(5, 15)])
    pwd = PasswordField('密码', validators=[Length(9, 15)])
    submit = SubmitField('确定')


class SearchForm(FlaskForm):
    isbn = StringField('ISBN')
    title = StringField('标题', validators=[Length(0, 100)])
    author = StringField('作者', validators=[Length(0, 30)])
    submit = SubmitField('查找')


class ReviewForm(FlaskForm):
    content = StringField('评论内容', validators=[Length(0, 65535)])
    submit = SubmitField('添加评论')

