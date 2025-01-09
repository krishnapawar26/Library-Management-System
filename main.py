from user import User
from book import Book
from database import Database

def main():
    db = Database('data/library.db')
    user = User(db)
    book = Book(db)
    
    # Example: Add a book to the system
    book.add_book('The Great Gatsby', 'F. Scott Fitzgerald', '1234567890', 5)
    print("Book added.")

if __name__ == "__main__":
    main()
