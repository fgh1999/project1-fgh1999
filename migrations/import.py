import csv
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class BookRecord(Base):
    __tablename__ = 'books'
    isbn = Column(String(10), primary_key=True)
    title = Column(String(200), nullable=False)
    author = Column(String(200), nullable=False)
    year = Column(Integer, nullable=False)


engine = create_engine('postgresql://postgres:123456@127.0.0.1:5432/postgres')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# read data
with open('books.csv') as file:
    rows = csv.reader(file)
    next(rows)
    for row in rows:
        record = BookRecord(isbn=row[0], title=row[1],
                            author=row[2], year=int(row[3]))
        session.add(record)

session.commit()
