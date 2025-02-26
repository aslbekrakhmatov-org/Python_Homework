class BookNotFoundException(Exception):
    def __init__(self, message = "Book is not found in the library."):
        self.message = message
        super().__init__(self.message)

class BookAlreadyBorrowedException(Exception):
    def __init__(self, message = "Book is already borrowed by someone else"):
        self.message = message
        super().__init__(self.message)

class MemberLimitExceededException(Exception):
    def __init__(self, message = "Member's book limit exceeded."):
        self.message = message
        super().__init__(self.message)

class Book:
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def __str__(self):
        return f"{self.title}, {self.author}"
    
class Member:
    def __init__(self, name, ):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books)>=3:
            raise MemberLimitExceededException(f"{self.name} can't borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The {book.title} is already borrowed by someone else.")
        self.borrowed_books.append(book)
        book.is_borrowed = True
        print(f"{self.name} has borrowed the book {book.title}.")

    def return_book(self, book):
        if book not in self.borrowed_books:
            raise BookNotFoundException(f"{self.name} hasn't borrowed the {book.title}")
        self.borrowed_books.remove(book)
        book.is_borrowed = False
        print(f"{self.name} returned the {book.title}")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"The {book.title} is added to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"The {member.name} is added to the library.")

    def find_book(self, book_title):
        for book in self.books:
            if book.title != book_title:
                raise BookNotFoundException(f"The {book_title} doesn't exist in the library.")
            else:
                return book
    def find_member(self, member_name):
        for member in self.members:
            if member.name != member_name:
                raise BookNotFoundException(f"The {member_name} doesn't exist in the library.")   
            else:
                return member

library = Library()
book1 = Book("Bygone days", "Abdulla Qodiriy")
book2 = Book("Atomic habits", "James Clear")
book3 = Book("Between two doors", "O'tkir Hoshimov")
book4 = Book("Riding the Yellow Giant", "Khudotberdi Tukhtaboev")
library.add_book(book4)
library.add_book(book2)
library.add_book(book1)
library.add_book(book3)

member1 = Member("John")
member2 = Member("Alice")
library.add_member(member1)
library.add_member(member2)

# try:
#     member1.borrow_book(book1)
#     member1.borrow_book(book2)
#     member1.borrow_book(book3)
#     member2.borrow_book(book4)
#     member2.borrow_book(book1)
# except Exception as e:
#     print(e)

# try:
#     book5 = library.find_book("Non-Existent Book")  
# except Exception as e:
#     print(e)

try:
    member1.borrow_book(book1)
    member1.borrow_book(book2)
    member1.borrow_book(book3)
    member1.borrow_book(book4)
except Exception as e:
    print(e)