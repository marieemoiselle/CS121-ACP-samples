from book import Book

def main():
    # Create a Book object
    book = Book()
    
    # Prompt user for input and set properties
    isbn = input("Enter the book's ISBN: ")
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    
    book.set_isbn(isbn)
    book.set_title(title)
    book.set_author(author)
    
    # Display book details
    print("\nBook Details:")
    print(f"ISBN: {book.get_isbn()}")
    print(f"Title: {book.get_title()}")
    print(f"Author: {book.get_author()}")

# Run the program
if __name__ == "__main__":
    main()
