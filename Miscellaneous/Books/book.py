class Book:
    def __init__(self):
        self._isbn = None
        self._title = None
        self._author = None

    # Getter and setter for ISBN
    def set_isbn(self, isbn):
        self._isbn = isbn

    def get_isbn(self):
        return self._isbn

    # Getter and setter for title
    def set_title(self, title):
        self._title = title

    def get_title(self):
        return self._title

    # Getter and setter for author
    def set_author(self, author):
        self._author = author

    def get_author(self):
        return self._author
