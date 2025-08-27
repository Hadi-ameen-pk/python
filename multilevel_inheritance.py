# Base class
class Vehicle:
    def info(self):
        print("This is a vehicle.")
# Derived class from Vehicle
class Car(Vehicle):
    def car_info(self):
        print("This is a car.")
# Derived class from Car
class SportsCar(Car):
    def sportscar_info(self):
        print("This is a sports car.")
# Create object
obj = SportsCar()
obj.info()           # From Vehicle
obj.car_info()       # From Car
obj.sportscar_info() # From SportsCar
