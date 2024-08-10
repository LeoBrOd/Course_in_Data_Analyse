# 1
class Dog():
    def __init__(self, name_of_the_dog, amount_of_legs):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog
        self.amount_of_legs = amount_of_legs

    def _str_(self):
        return (f'Name: {self.name} amount_of_legs: {self. amount_of_legs}')

    def names(self, other_dog):
        print(self.name + ' ' + other_dog.name)

    def add(a, b):
        print(a+b)


shelter_dog = Dog("Rex", 4)
other_shelter_dog = Dog("Jimmy", 3)

print(shelter_dog)
shelter_dog.names(other_shelter_dog)
Dog.add(1, 2)
shelter_dog.name = "Spot"
shelter_dog.name


# 2
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


# create an instance of the class
p = Point(3, 4)
# access the attributes
print("p.x is:", p.x)
print("p.y is:", p.y)

# 3


class BankAccount():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)

    def withdraw(self, amount):  # rebuild later
        if self.balance < amount:
            print(f"you dont have enough money\nYour balance: {self.balance}")
        else:
            self.balance -= amount
            print(self.balance)

    def get_balance(self):
        return self.balance
       # print(f"{self.owner} you balance is: {self.balance}")

    def transfer(self, other_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer sucseded")
        else:
            print("You dont have enough money")


alice = BankAccount("Alice", 1000)
print(alice.balance)
alice.deposit(500)
print(alice.balance)
alice.withdraw(2000)
pete = BankAccount("Pete", 2000)
alice.transfer(pete, 2500)
alice.transfer(pete, 500)
print(alice.balance)
print(pete.balance)

# 4
# Problem: Library Management System
# Create a Python class named Book that models a book in a library system. This class will handle various operations related to book management, such as issuing and returning books. Here are the details:
# Attributes:
# title: Title of the book (string).
# author: Author of the book (string).
# isbn: ISBN number of the book (string).
# available: Boolean indicating if the book is available for loan (initially True).
# Methods:
# __init__(self, title, author, isbn): Initializes a new book with the given title, author, and ISBN. The book should be available for loan by default.
# issue_book(self): If the book is available, marks the book as not available and prints that the book is issued. If the book is not available, prints that the book is already issued.
# return_book(self): Marks the book as available again and prints that the book has been returned.
# __str__(self): Returns a string representation of the book, showing its title, author, and availability status.
# Additional Class: Library
# To manage a collection of Book instances, create a class Library:
# Attributes:
# books: A list to store instances of Book.
# Methods:
# __init__(self): Initializes the library with an empty list of books.
# add_book(self, book): Adds a Book instance to the library.
# find_books_by_title(self, title): Returns a list of books that match the given title.
# find_books_by_author(self, author): Returns a list of books that match the given author.
# list_available_books(self): Prints all books that are currently available.
# list_all_books(self): Prints all books in the library, including their availability.
# Your tasks:
# Define the Book and Library classes with the described functionalities.
# Create several Book instances and add them to the Library.
# Test issuing and returning a book.
# Display books by a specific author or title.
# Print lists of all books and only available books.


# class Book():
#     def __init__(self, title, author, isbn, available=True):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.available = available

#     def issue_book(self,):
#         if self.available:
#             self.available = False
#         else:
#             print(f"`{self.title}` not available right now")

#     def return_book(self):
#         if not self.available:
#             self.available = True
#         else:
#             print(f"`{self.title}` already in a library")

#     def __str__(self):
#         return (self.title + " " + self.author + " " + self.isbn + " " + str(self.available))


# class Library():
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def find_books_by_title(self, title):
#         for i in self.books:
#             if title in i.title:
#                 print(i.title)


# first = Book("first book", "first author", "first isbn", True)
# second = Book("second book", "second author", "second isbn", True)
# third = Book("third book", "third author", "third isbn", True)

# print(third.__str__())

# library1 = Library(first)
# library1.find_books_by_title("first")

# # Teachers solution


class Book:
    def _init_(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def issue_book(self):
        if self.available:
            self.available = False
            print(f"Book '{self.title}' has been issued.")
        else:
            print(f"Book '{self.title}' is already issued.")

    def return_book(self):
        self.available = True
        print(f"Book '{self.title}' has been returned.")

    def _str_(self):
        availability = "Available" if self.available else "Issued"
        return f"'{self.title}' by {self.author} - {availability}"


class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book, amount=1):
        isbn_book1 = book.isbn
        if amount > 1:
            for i in range(amount):
                self.books.append(
                    Book(book.title, book.author, str(int(book.isbn)+i)))
        elif amount == 1:
            self.books.append(book)

    def issue_by_name(self, name):
        for book in self.books:
            if book.title == name:
                book.available = False
                break
        else:
            print("there is no book with that name")

    def find_books_by_title(self, title):
        return [book for book in self.books if book.title == title]

    def find_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def list_available_books(self):
        print("Available books:")
        for book in self.books:
            if book.available:
                print(book)

    def list_all_books(self):
        print("All books in the library:")
        for book in self.books:
            print(book)


# Example of using the classes
library = Library()
library.add_book(Book("1984", "George Orwell", "9780451524935"), 4)
library.add_book(Book("Brave New World", "Aldous Huxley", "9780060850524"))
# Issue some books and return them
library.books[0].issue_book()
# Use search functions
books_by_title = library.find_books_by_title("1984")
books_by_author = library.find_books_by_author("George Orwell")
print("\nBooks by title '1984':")
for book in books_by_title:
    print(book)
print("\nBooks by author 'George Orwell':")
for book in books_by_author:
    print(book)
library.list_all_books()
library.list_available_books()
library.issue_by_name("1984")
library.list_available_books()