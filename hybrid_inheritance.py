# Base class
class LivingBeing:
    def breathe(self):
        print("All living beings breathe.")
# Derived class 1 (hierarchical from LivingBeing)
class Animal(LivingBeing):
    def sound(self):
        print("Animals make sounds.")
# Derived class 2 (hierarchical from LivingBeing)
class Bird(LivingBeing):
    def fly(self):
        print("Birds can fly.")
# Hybrid child class (multiple inheritance: Animal + Bird)
class Parrot(Animal, Bird):
    def talk(self):
        print("Parrot can talk!")
# Create object
p = Parrot()
p.breathe()  # From LivingBeing
p.sound()    # From Animal
p.fly()      # From Bird
p.talk()     # From Parrot
