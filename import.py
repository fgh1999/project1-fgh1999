import pandas as pd
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql://postgres:123456@127.0.0.1:5432/postgres')

class BookRecord(Base):
    __tablename__ = 'book_record'
    isbn = Column(String(10), primary_key=True)
    title = Column(String(200), nullable=False)
    author = Column(String(200), nullable=False)
    year = Column(Integer, nullable=False)

# read data
df = pd.read_csv('books.csv')

Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

## Insert data into table 'book_record'
for index, row in df.iterrows():
    record = BookRecord(isbn=row['isbn']
                        , title=row['title']
                        , author=row['author']
                        , year=row['year'])
    session.add(record)

session.commit()
