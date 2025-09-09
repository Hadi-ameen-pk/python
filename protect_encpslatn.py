class Car:
    def __init__(self, brand):
        self._brand = brand   # protected attribute

mycar = Car("Tesla")
print(mycar._brand)   #  Can access, but not recommended
