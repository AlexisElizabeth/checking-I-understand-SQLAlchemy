# CRUD:  Create, Read, Update, Delete
# When working with any new database technology, know how to CRUD data records

# To CREATE a new database
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)



# To CREATE a new table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()


# To CREATE a new record
# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# with app.app_context():
#     db.session.add(new_book)
#     db.session.commit()

# To READ all records
with app.app_context():
    all_books = db.session.query(Book).all()

# To READ A Particular Record By Query
with app.app_context():
    book = Book.query.filter_by(title="Harry Potter").first()

# To UPDATE A Particular Record By Query
# with app.app_context():
#     book_to_update = Book.query.filter_by(title="Harry Potter").first()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()

# To Update A Record By PRIMARY KEY
with app.app_context():
    book_id = 1
    book_to_update = Book.query.get(book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()


# # To Delete A Particular Record By PRIMARY KEY
with app.app_context():
    book_id = 1
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

print(all_books)
