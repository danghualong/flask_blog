from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length

class RegisterForm(FlaskForm):
    email=StringField('Email:',validators=[DataRequired(message='Email不能为空'),Length(max=20,message='不能超过20个字符')],render_kw={'placeholder':'请输入邮箱地址'})
    password=PasswordField('密码:',validators=[DataRequired(message='密码不能为空'),Length(max=20,message='不能超过20个字符')],render_kw={'placeholder':'请输入密码'})
    confirmPassword=PasswordField('确认密码:',validators=[DataRequired(message='密码不能为空'),Length(max=20,message='不能超过20个字符')],render_kw={'placeholder':'请确认密码'})
    submit=SubmitField('提交')