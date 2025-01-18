class Book:
    def __init__(self, title, author):
        """Initialize the book with title, author, and its checked-out status."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Check out the book if it is available."""
        if self._is_checked_out:            #if the book is checked out
            return False            #exits the operations
        self._is_checked_out = True     #otherwise checks out the book 
        return True                    #indicates the operation is successful

    def return_book(self):
        """Return the book if it is checked out."""
        if not self._is_checked_out:  #if the book is not checked out
            return False            #exits the operation
        self._is_checked_out = False #otherwise, executes return_book
        return True             #indicates the operation is successful

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    # def add_book(self, title, author):
    #     """Add a book to the library."""
    #     book = Book(title, author)

    def add_book(self, book):
        """Add a book object to the library"""
        self._books.append(book)
        # print(f"Book '{book.title}' by '{book.author}' added to library")

    def check_out_book(self, title):
        """Check out a book from the library by title."""
        for book in self._books: #loops through the list of books to find title passed
            if book.title == title:
                if book.check_out():
                    return
                    # print(f"Book '{title}' checked out successfully")
                else:
                    print(f"Book '{title}' is already checked out")
                return
        print(f"Book '{title}' not found in the library")

    def return_book(self, title):
        """Return a book to the library by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return 
                        #print(f"Book '{title}' returned successfully")
                else:
                    print(f"Book '{title}' was not checked out")
                return
        print(f"Book '{title}' not found in the library")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()] #loops through the list of books and check if the book is available 
                                                                                 #then creates a new list of available books
        if available_books:
            # print("Available books:") #prints a header message
            for book in available_books:                    #Loops through available books
                print(f"'{book.title}' by '{book.author}'") #and print title and author of each available book
        else:
            print("No books are currently available")