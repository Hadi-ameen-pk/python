class Car:
    def __init__(self, brand):
        self.brand = brand   # public attribute

mycar = Car("Tesla")
print(mycar.brand)   #  Accessible
