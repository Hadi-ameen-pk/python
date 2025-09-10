from abc import ABC, abstractmethod   # For abstraction

# ---------- Abstraction ----------
class Serviceable(ABC):   # Abstract class
    @abstractmethod
    def service_cost(self):   # Abstract method
        pass


# ---------- Base Class ----------
class Vehicle(Serviceable):   # Inheritance from abstract class
    def __init__(self, brand, model, price):   # Constructor
        self.brand = brand
        self.model = model
        self.__price = price   # Encapsulation (private variable)

    # Getter (Encapsulation)
    def get_price(self):
        return self.__price

    # Setter (Encapsulation)
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

    # Polymorphism (can be overridden in subclasses)
    def details(self):
        return f"Vehicle: {self.brand} {self.model}, Price: {self.__price}"

    # Operator Overloading (+ to add two vehicle prices)
    def __add__(self, other):
        return self.__price + other.__price

    # Abstract method (must be implemented in subclasses)
    def service_cost(self):
        pass

    # Static Method
    @staticmethod
    def is_valid_registration(reg_no):
        return reg_no.isalnum() and len(reg_no) == 6

    # Class Method (Alternative constructor)
    @classmethod
    def from_string(cls, data_str):
        brand, model, price = data_str.split("-")
        return cls(brand, model, int(price))


# ---------- Subclasses (Inheritance + Polymorphism) ----------
class Car(Vehicle):   # Inherits from Vehicle
    def service_cost(self):   # Implements abstract method
        return 5000

    def details(self):   # Overriding (Polymorphism)
        return f"Car: {self.brand} {self.model}, Price: {self.get_price()}"
class Bike(Vehicle):
    def service_cost(self):
        return 2000
    def details(self):
        return f"Bike: {self.brand} {self.model}, Price: {self.get_price()}"
# ---------- Multiple Inheritance ----------
class Electric:   # Extra class
    def battery_info(self):
        return "Battery: 80 kWh"


class ElectricCar(Car, Electric):   # Multiple Inheritance
    def service_cost(self):
        return 3000   # Cheaper service for EVs


# ---------- Testing the System ----------
if __name__ == "__main__":
    # Create objects (Class & Objects)
    car1 = Car("Toyota", "Corolla", 15000)
    bike1 = Bike("Yamaha", "R15", 3000)

    # Alternative constructor (Class Method)
    car2 = Vehicle.from_string("Honda-City-20000")

    # Electric Car (Multiple Inheritance)
    ecar = ElectricCar("Tesla", "Model 3", 35000)

    # Show details (Polymorphism)
    print(car1.details())
    print(bike1.details())
    print(ecar.details())
    print(ecar.battery_info())

    # Service cost (Abstraction implemented)
    print("Car service cost:", car1.service_cost())
    print("Bike service cost:", bike1.service_cost())
    print("Electric Car service cost:", ecar.service_cost())

    # Operator overloading (+)
    total = car1 + bike1
    print("Total price (car + bike):", total)

    # Encapsulation (getter & setter)
    car1.set_price(16000)
    print("Updated Car Price:", car1.get_price())

    # Static method
    print("Valid reg:", Vehicle.is_valid_registration("AB123C"))
    print("Invalid reg:", Vehicle.is_valid_registration("12!@"))
