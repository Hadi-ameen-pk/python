from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):   # abstract method (no implementation here)
        pass

# Child Class
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Usage
dog = Dog()
cat = Cat()
print(dog.make_sound())   # Woof!
print(cat.make_sound())   # Meow!

# Trying to instantiate Animal directly will give an error
# animal = Animal()   #  TypeError: Can't instantiate abstract class
