from flask import render_template, session, redirect, \
    url_for, current_app, flash
from .. import db
from ..models import User
from . import main
from .forms import UserForm


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            flash("Wrong username!")
            session['have_login'] = False
        elif user.pwd == form.name.data:
            session['have_login'] = True
        return redirect(url_for('.index'))
    return render_template('login.html', form=form,
                           have_login=session.get('have_login', False))


@main.route("/", methods=['GET'])
def index():
    return render_template('index.html',
                           have_login=session.get('have_login', False))


@main.route('/search', methods=['GET', 'POST'])
def search():
    pass


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data,
                        pwd=form.pwd.data)
            db.session.add(user)
            db.session.commit()
            flash("successfully registered!")
            session['have_login'] = True
            return redirect(url_for('.index'))
        else:
            flash("This username has been registered, please use another name.")
            session['have_login'] = False
    return render_template('register.html', form=form,
                           have_login=session.get('have_login', False))


@main.route('/book/<isbn: string>', methods=['GET'])
def book(isbn: str):
    pass

