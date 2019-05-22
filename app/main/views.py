from flask import render_template, session, redirect, \
    url_for, current_app, flash, abort
from .. import db
from ..models import User, Book, Review
from . import main
from .forms import UserForm, SearchForm, ReviewForm


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is not None and user.pwd == form.name.data:
            session['have_login'] = True
            session['user_id'] = user.id
            flash('successfully login!')
            return redirect(url_for('.index'))
        else:
            session['have_login'] = False
            flash('Wrong username or password!')
    return render_template('login.html', form=form,
                           have_login=session.get('have_login', False))


@main.route('/logout', methods=['GET'])
def logout():
    session['have_login'] = False
    del session['user_id']
    return redirect(url_for('.index'))


@main.route("/", methods=['GET'])
def index():
    session['search_success'] = False
    return render_template('index.html',
                           have_login=session.get('have_login', False))


@main.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    results = None
    if form.validate_on_submit():
        book_query = Book.query
        if len(form.author.data.strip())>0: 
            book_query = book_query.filter_by(author=form.author.data)
        if len(form.isbn.data.strip()) > 0:
            book_query = book_query.filter_by(isbn=form.isbn.data)
        if len(form.title.data.strip()) > 0:
            book_query = book_query.filter_by(title=form.title.data)
        results = book_query.all()
        if results:
            session['search_success'] = True
        else:
            session['search_success'] = False
    return render_template('search.html', form=form, results=results,
                           search_success=session.get('search_success', False),
                           have_login=session.get('have_login', False))


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
            session['user_id'] = user.id
            return redirect(url_for('.index'))
        else:
            flash("This username has been registered, please use another name.")
            session['have_login'] = False
    return render_template('register.html', form=form,
                           have_login=session.get('have_login', False))


@main.route('/book/<string:isbn>', methods=['GET'])
def book(isbn: str):
    if isbn is None:
        abort(400)
    result = Book.query.filter_by(isbn=isbn).first()
    if result is None:
        abort(404)
    else:
        for review in result.reviews:
            user = review.user # load user field
        return render_template('book.html', book=result, reviews=result.reviews,
                               have_login=session.get('have_login', False))


@main.route('/add-review/<string:isbn>', methods=['GET', 'POST'])
def add_review(isbn: str):
    if isbn is None or session.get('have_login', False):
        abort(400)
    form = ReviewForm()
    result = Book.query.filter_by(isbn=isbn).first()
    user = User.query.filter_by(id=session.get('user_id')).first()
    if result is None or user is None:
        abort(404)
    if form.validate_on_submit():
        new_review = Review(content=form.content.data,
                            user_id=session.get('user_id', -1),
                            book_isbn=isbn)
        result.reviews.push(new_review)
        user.reviews.push(new_review)
        db.session.add_all([new_review, result, user])
        db.session.commit()
        flash("Thank You for Your Review!")
    return render_template('add-review.html', form=form,
                           have_login=session.get('have_login', False))

