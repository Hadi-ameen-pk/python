# Parent class
class Animal:
    def sound(self):
        print("This animal makes a sound.")

# Child class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("The dog barks: Woof! Woof!")

# Create object of child class
d = Dog()
d.sound()   # Inherited from Animal
d.bark()    # Own method
