from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.authors import Author

@app.route('/')
def home():
    return redirect('/authors')

@app.route('/authors')
def getAuthors():
    return render_template("authors.html", authors=Author.getAll())

@app.route('/author/new', methods=['POST'])
def addAuthor():
    Author.save(request.form)
    return redirect('/authors')
