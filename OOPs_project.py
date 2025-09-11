from abc import ABC, abstractmethod


# ------------------------------
# Abstraction & Encapsulation
# ------------------------------
class Item(ABC):
    def __init__(self, title, author):
        self._title = title  # Encapsulation (protected)
        self._author = author
        self.__available = True  # Encapsulation (private)

    @abstractmethod
    def display(self):
        pass

    def is_available(self):
        return self.__available

    def borrow(self):
        if self.__available:
            self.__available = False
            print(f"'{self._title}' borrowed successfully.")
        else:
            print(f"'{self._title}' is not available.")

    def return_item(self):
        self.__available = True
        print(f"'{self._title}' returned successfully.")
# ------------------------------
# Inheritance & Polymorphism
# ------------------------------
class Book(Item):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def display(self):  # Polymorphism
        print(f" Book: {self._title} by {self._author}, {self.pages} pages")


class Magazine(Item):
    def __init__(self, title, author, issue):
        super().__init__(title, author)
        self.issue = issue

    def display(self):  # Polymorphism
        print(f" Magazine: {self._title}, Issue: {self.issue}")


# ------------------------------
# Operator Overloading
# ------------------------------
class Library:
    total_items = 0  # Class variable

    def __init__(self, name):
        self.name = name
        self.items = []
        Library.total_items = 0

    def add_item(self, item):
        self.items.append(item)
        Library.total_items+=1
    @staticmethod
    def library_info():
        print("A library stores books and magazines for readers.")


# ------------------------------
# Usage (Testing the system)
# ------------------------------

Library.library_info()

# Create Libraries
lib1 = Library("City Library")
lib2 = Library("Community Library")

# Add items
b1 = Book("Python OOP", "John Doe", 350)
b2 = Book("Data Science", "Alice", 420)
m1 = Magazine("Tech Today", "Editor X", "Sep 2025")

lib1.add_item(b1)
lib1.add_item(m1)
lib2.add_item(b2)

# Display items
for item in lib1.items:
    item.display()
b1.borrow()
b1.borrow()  # already borrowed
b1.return_item()