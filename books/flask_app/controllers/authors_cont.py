from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.author import Author
from flask_app.models.book import Book

# Display ---------------------------------------------------

@app.route("/")
def re_direct():
    return redirect('/authors')

@app.route("/authors")
def home():
    authors = Author.get_all()
    return render_template("home.html", authors=authors)

@app.route("/books")
def home_books():
    books = Book.get_all()
    return render_template("add_book.html", books=books)

@app.route('/authors/<int:id>')
def add_author_favorite(id):
    books = Book.get_all()
    data ={ 
        "id":id
    }
    return render_template("add_author_favorite.html",authors=Author.get_one(data), Authors=Author.get_by_id(data), books=books)

@app.route('/book/<int:id>')
def add_book_favorirte(id):
    authors = Author.get_all()
    data = {
        "id":id
    }
    return render_template('add_book_favorite.html',books=Book.get_one(data),book=Book.get_by_id(data),authors=authors)

# Active ---------------------------------------------------

@app.route('/authors/create', methods=["POST"])
def add_author():
    data = {
        "name": request.form["name"],
    }
    Author.save(data)
    return redirect('/authors')

@app.route('/books/create', methods=["POST"])
def add_book():
    data = {
        "title": request.form["title"],
        "num_of_pages": request.form["num_of_pages"],
    }
    Book.save(data)
    return redirect('/books')

@app.route('/join/book', methods=["POST"])
def join_book():
    data = {
        "author_id": request.form["author_id"],
        "book_id": request.form["book_id"],
    }
    Author.add_favorite(data)
    return redirect(f"/authors/{request.form['author_id']}")

@app.route('/join/author',methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")
