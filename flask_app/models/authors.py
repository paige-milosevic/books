from flask_app.config.mysqlconnection import connectToMySQL


class Author:
    def __init__(self,data) -> None:
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM authors;'
        authors_db = connectToMySQL('booksDB').query_db(query)
        authors = []
        for i in authors_db:
            authors.append(cls(i))
        return authors
    
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO authors (name) VALUES (%(name)s);'
        author_id = connectToMySQL('booksDB').query_db(query,data)
        return author_id