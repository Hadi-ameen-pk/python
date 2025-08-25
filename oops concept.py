#Perfect 👍 Let’s carefully *explain each program* step by step.



# 🔹 Program 1: *Student Class*

#python
class Student:
    def __init__(self, name, age):   # constructor (__init__)
        self.name = name             # attribute
        self.age = age               # attribute

# create objects
s1 = Student("Rahul", 20)
s2 = Student("Asha", 19)

print("Name:", s1.name, "| Age:", s1.age)
print("Name:", s2.name, "| Age:", s2.age)


### Explanation:
'''
* class Student: → Creates a *class* named Student.
* __init__ → Constructor, runs automatically when an object is created.
* self.name = name → Stores the student’s name in the object.
* s1 = Student("Rahul", 20) → Creates an object with name="Rahul", age=20.
* Printing shows the values stored inside each object.
'''
'''
✅ Output:

Name: Rahul | Age: 20
Name: Asha | Age: 19
'''


# 🔹 Program 2: *Book Class*

#python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b1 = Book("Python Basics", "Guido")
b2 = Book("AI Intro", "Andrew")

print(b1.title, "by", b1.author)
print(b2.title, "by", b2.author)


### Explanation:
'''
* class Book: → Class that represents books.
* __init__ → Takes title and author when a new object is created.
* b1 = Book("Python Basics", "Guido") → Creates first book.
* b2 = Book("AI Intro", "Andrew") → Creates second book.
* Printing shows book details.
'''
'''
✅ Output:

Python Basics by Guido
AI Intro by Andrew
'''

# 🔹 Program 3: *Circle Class (with method)*

#python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):   # method to calculate area
        return 3.14 * self.radius * self.radius

c1 = Circle(5)
c2 = Circle(7)

print("Area of circle 1:", c1.area())
print("Area of circle 2:", c2.area())


### Explanation:
'''
* class Circle: → Blueprint for a circle.
* __init__(self, radius) → Stores radius when object is created.
* def area(self): → A *method* to calculate the area of the circle.
* c1 = Circle(5) → Circle with radius 5.
* c1.area() → Calls the method, calculates 3.14 * 5 * 5 = 78.5.
* c2 = Circle(7) → Circle with radius 7.
* c2.area() → Calculates 3.14 * 7 * 7 = 153.86.
'''
'''
✅ Output:


Area of circle 1: 78.5
Area of circle 2: 153.86
'''

'''
👉 Summary:

* **class** → Defines the blueprint.
* **__init__** → Special method to set initial values (constructor).
* *Objects* → Created from the class, each with its own data.
* *Methods* → Functions inside class that work with the object’s data.
'''