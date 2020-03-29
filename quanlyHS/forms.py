from flask_wtf import FlaskForm
from wtforms import (StringField,
                     PasswordField,
                     SubmitField,
                     BooleanField,
                     DateField,
                     IntegerField,
                     ValidationError)
from wtforms.validators import DataRequired, Length, Email, EqualTo
from quanlyHS.models import User
from datetime import datetime



class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def valdation_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username has been used, \
                                    please choose the other')

    def valdation_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This username has been used, \
                                    please choose the other')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class Lophoc(FlaskForm):
    MaLop = StringField('Malop', validators=[DataRequired()])
    GVCN = StringField('GVCN', validators=[DataRequired()])
    PhongHoc = StringField('PhongHoc', validators=[DataRequired()])
    submit = SubmitField('Submit')


class HocSinh(FlaskForm):
    MaHS = StringField('MaHS', validators=[DataRequired()])
    TenHS = StringField('TenHS', validators=[DataRequired()])
    NgaySinh = DateField('NgaySinh', validators=[DataRequired()])
    GioiTinh = StringField('GioiTinh', validators=[DataRequired()])
    MaLop = StringField('MaLop', validators=[DataRequired()])
    PhuHuynh = StringField('PhuHuynh')
    DiaChi = StringField('DiaChi')
    SDT = StringField('SDT')
    Email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')


class Giaovien(FlaskForm):
    MaGV = StringField('MaGV', validators=[DataRequired()])
    TenGV = StringField('TenGV', validators=[DataRequired()])
    NgaySinh = DateField('NgaySinh', validators=[DataRequired()])
    GioiTinh = StringField('GioiTinh', validators=[DataRequired()])
    Email = StringField('Email', validators=[DataRequired()])

    submit = SubmitField('Submit')


class Lichday(FlaskForm):
    MaLop = StringField('MaLop', validators=[DataRequired()])
    MaGV = StringField('MaGV', validators=[DataRequired()])
    MaMH = StringField('MaMH', validators=[DataRequired()])
    NamHoc = IntegerField('NamHoc', validators=[DataRequired()])
    KyHoc = IntegerField('KyHoc', validators=[DataRequired()])
    Monday = StringField('Monday')
    Tuesday = StringField('Tuesday')
    Wednesday = StringField('Wednesday')
    Thursday = StringField('Thursday')
    Friday = StringField('Friday')
    Email = StringField('Email', validators=[DataRequired()])

    submit = SubmitField('Submit')


class Diemdanh(FlaskForm):
    MaGV = StringField('MaGV', validators=[DataRequired()])
    MaLop = StringField('MaLop', validators=[DataRequired()])
    submit = SubmitField('Submit')