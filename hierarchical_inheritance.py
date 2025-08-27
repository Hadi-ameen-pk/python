# Parent class
class Animal:
    def sound(self):
        print("Animals make different sounds.")
# Child class 1
class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof! Woof!")
# Child class 2
class Cat(Animal):
    def meow(self):
        print("Cat meows: Meow! Meow!")
# Create objects
d = Dog()
c = Cat()
d.sound()  # Inherited from Animal
d.bark()   # Specific to Dog
c.sound()  # Inherited from Animal
c.meow()   # Specific to Cat
