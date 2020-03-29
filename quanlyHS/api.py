from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, logout_user, login_required
from wtforms import ValidationError

from quanlyHS.main import bcrypt, db, login_manager
from quanlyHS.forms import RegisterForm, LoginForm
from quanlyHS.models import User


bp = Blueprint('api1', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp.route("/")
@bp.route("/home")
def home():
    return render_template('home.html')


@bp.route("/about")
def about():
    return render_template('about.html', title='About')


@bp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            raise ValidationError('This username has been used, please choose the other')
        elif User.query.filter_by(email=form.email.data).first():
            raise ValidationError('This username has been used, please choose the other')

        else:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('api1.login'))

    return render_template('register.html', title='Register', form=form)


@bp.route("/login", methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('api1.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', title='Login', form=form)


@bp.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for("api1.home"))


@bp.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
