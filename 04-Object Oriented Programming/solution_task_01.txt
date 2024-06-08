class Book:
    def __init__(self, title, author, ISBN, year, available_copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.year = year
        self.available_copies = available_copies

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.ISBN}, Year: {self.year}, Available copies: {self.available_copies})"

class Member:
    def __init__(self, name, member_id, contact_info):
        self.name = name
        self.member_id = member_id
        self.contact_info = contact_info
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available_copies > 0:
            book.available_copies -= 1
            self.borrowed_books.append(book)
        else:
            print("This book is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available_copies += 1
            self.borrowed_books.remove(book)
        else:
            print("This book was not borrowed by the member.")

    def __str__(self):
        return f"Member: {self.name}, ID: {self.member_id}, Contact: {self.contact_info}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, ISBN):
        self.books = [book for book in self.books if book.ISBN != ISBN]

    def search_book(self, **kwargs):
        for book in self.books:
            if all(getattr(book, key) == value for key, value in kwargs.items()):
                return book
        return None

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member_id):
        self.members = [member for member in self.members if member.member_id != member_id]

    def borrow_book(self, member_id, ISBN):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = self.search_book(ISBN=ISBN)
        if member and book:
            member.borrow_book(book)

    def return_book(self, member_id, ISBN):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = self.search_book(ISBN=ISBN)
        if member and book:
            member.return_book(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def list_members(self):
        for member in self.members:
            print(member)

# Example usage
library = Library()

# Adding books
book1 = Book("1984", "George Orwell", "1234567890", 1949, 5)
library.add_book(book1)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321", 1960, 3)
library.add_book(book2)

# Adding members
member1 = Member("Alice", "1", "alice@example.com")
library.add_member(member1)
member2 = Member("Bob", "2", "bob@example.com")
library.add_member(member2)

# Borrowing and returning books
library.borrow_book("1", "1234567890")
library.return_book("1", "1234567890")

# Listing all books and members
library.list_books()
library.list_members()


"""

Explanation:
Book Class: Represents a book in the library. It includes details like title, author, ISBN, year of publication, and available copies. Methods include those for basic book management.
Member Class: Represents a library member. It includes details like name, member ID, and contact information. Methods allow a member to borrow and return books.
Library Class: Manages the collection of books and members. Methods handle adding/removing books and members, as well as borrowing and returning books.


"""