import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://new-books-collection.db"
db = sqlite3.connect("new-books-collection.db")

db= SQLAlchemy()
db.init_app(app)
cursor = db.cursor()


#create table
class Book(db.Model):
    id = db.column(db.Integer,primary_key=True)
    title=db.column(db.String(250),unique=True,nullable=False)
    author=db.column(db.String(250),nullable =False)
    rating=db.column(db.Float,nullable=False)

def __repr__(self):
    return f'<book{self.title}>'


with app.app_context():
    db.create_all()

with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit(c


git