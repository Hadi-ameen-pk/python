# Parent class
class Animal:
    def __init__(self):
        print("Animal created")
    def sound(self):
        print("Animals make different sounds.")
# Child class 1
class Dog(Animal):
    def __init__(self):
        super().__init__()  # Call Animal's constructor
        print("Dog created")
    def bark(self):
        print("Dog barks: Woof! Woof!")
# Child class 2
class Cat(Animal):
    def __init__(self):
        super().__init__()  # Call Animal's constructor
        print("Cat created")
    def meow(self):
        print("Cat meows: Meow! Meow!")
# Create objects
d = Dog()
c = Cat()
d.sound()  # From Animal
d.bark()  # Specific to Dog
c.sound()  # From Animal
c.meow()  # Specific to Cat