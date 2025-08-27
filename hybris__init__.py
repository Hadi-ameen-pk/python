# Base class
class LivingBeing:
    def __init__(self):
        print("LivingBeing created")
    def breathe(self):
        print("All living beings breathe.")
# Derived class 1 (from LivingBeing)
class Animal(LivingBeing):
    def __init__(self):
        super().__init__()  # Calls LivingBeing's constructor
        print("Animal created")
    def sound(self):
        print("Animals make sounds.")
# Derived class 2 (from LivingBeing)
class Bird(LivingBeing):
    def __init__(self):
        super().__init__()  # Calls LivingBeing's constructor
        print("Bird created")
    def fly(self):
        print("Birds can fly.")
# Hybrid child class (inherits from both Animal and Bird)
class Parrot(Animal, Bird):
    def __init__(self):
        super().__init__()  # Uses MRO (Animal → Bird → LivingBeing)
        print("Parrot created")
    def talk(self):
        print("Parrot can talk!")
# Create object
p = Parrot()
p.breathe()  # From LivingBeing
p.sound()  # From Animal
p.fly()  # From Bird
p.talk()  # From Parrot
