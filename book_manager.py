from models import Book

class BookManager:
    def __init__(self, session):
        self.session = session

    def add_book(self, title, author, genre, image):
        # Create a new Book object with the provided information
        new_book = Book(title=title, author=author, genre=genre, image=image)

        # Add the new_book object to the session
        self.session.add(new_book)
        
        # Commit the transaction to save the changes to the database
        self.session.commit()
    
    def display_books(self):
        # Query all books from the database
        books = self.session.query(Book).all()

        if not books:
            print("No books found.")
            return

        # Print information for each book
        for book in books:
            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Image: {book.image}")
