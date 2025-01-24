class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title:str, author:str, file_size:int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title:str, author:str, page_count:int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print (book)
            elif isinstance(book, PrintBook):
                print (book)
            elif isinstance(book, Book):
                print (book)
            else:
                print("Unknown book type")

    def list_books(self):
        for book in self.books:
            match book:
                case EBook():
                    print (book) # print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
                case PrintBook():
                    print (book) # print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
                case Book():
                    print (book) # print(f"Book: {book.title} by {book.author}")
                case _:
                    print("Unknown book type")
    
    