from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.books import Book

@app.route('/books')
def getBooks():
    return render_template("books.html", books=Book.getAll())

@app.route('/book/new', methods=['POST'])
def addBook():
    data = {
        "title": request.form['title'],
        "num_of_pages": request.form['num_of_pages']
    }
    Book.save(data)
    return redirect('/books')

@app.route('/book/<int:id>')
def bookFavorite(id):
    data = {
        "id": id
    }
    return render_template('bookfavorite.html', book=Book.getFavorites(data))
