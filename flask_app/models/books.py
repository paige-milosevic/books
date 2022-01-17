from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.authors import Author

class Book:
    def __init__(self, data):
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM books;'
        books_db = connectToMySQL('booksDB').query_db(query)
        books = []
        for i in books_db:
            books.append(cls(i))
        return books
    
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);'
        book_id = connectToMySQL('booksDB').query_db(query,data)
        return book_id
    
    @classmethod
    def getAuthors(cls,data):
        query = 'SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON autros.id = favorites.authors_id WHERE books.id = %(id)s;'
        results = connectToMySQL('booksDB').query_db(query,data)
        book = cls(results[0])
        for row in results:
            if row['authros.id'] == None:
                break
            data = {
                "id": row['autors.id'],
                "name": row['name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authros.updated_at']
            }
            book.authors_who_favorited.append(author.Author(data))
