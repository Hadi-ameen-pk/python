class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)
    def describe(self):
        return f"{self.title} by {self.author}, Price: {self.price}"
class SpecialEditionBook(Book):
    def __init__(self, title, author, price, feature):
        super().__init__(title, author, price)
        self.feature = feature
    def describe(self):
        return f"{self.title} by {self.author}, Price: {self.price}, Feature: {self.feature}"
b1 = Book("Python Basics", "John Smith", 500)
b1.apply_discount(10)
print(b1.describe())
b2 = SpecialEditionBook("Python Advanced", "Alice Brown", 1000, "Autographed Copy")
print(b2.describe())
