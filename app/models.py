from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True)
    pwd = db.Column(db.String(16))
    reviews = db.relationship('Review', backref='user')

    def __repr__(self):
        return "<User {0}: {1}>".format(self.id, self.username)


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(2048))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_isbn = db.Column(db.String(10), db.ForeignKey('books.isbn'))

    def __repr__(self):
        return '<Review {0}: {1}>'.format(self.id, self.content)


class Book(db.Model):
    __tablename__ = 'books'
    isbn = db.Column(db.String(10), primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    reviews = db.relationship('Review', backref='book')

    def __repr__(self):
        return '<Book {0}: {1} {2} {3}>'.format(self.isbn, self.title, self.author, self.year)


