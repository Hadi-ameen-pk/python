# Base class
class Vehicle:
    def __init__(self):
        print("Vehicle class constructor")
    def info(self):
        print("This is a vehicle.")
# Derived class from Vehicle
class Car(Vehicle):
    def __init__(self):
        super().__init__()  # Call parent constructor
        print("Car class constructor")
    def car_info(self):
        print("This is a car.")
# Derived class from Car
class SportsCar(Car):
    def __init__(self):
        super().__init__()  # Call Car's constructor (which calls Vehicle's too)
        print("SportsCar class constructor")
    def sportscar_info(self):
        print("This is a sports car.")
# Create object
obj = SportsCar()
obj.info()  # From Vehicle
obj.car_info()  # From Car
obj.sportscar_info()  # From SportsCar
