##61.	Create an application that manages a library system with classes for Book and Library.

class Book:
    def __init__(self,title):
        self.title=title
class library:
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)
        print(f"added: {book.title}")

    def list_books(self):
        if self.books:
            print("books in library:")
            for book in self.books:
                print(f"- {book.title}")
        else:
            print("no books in library.")

library = library()
library.add_book(Book("the great gatsby"))
library.add_book(Book("1984"))
library.list_books()