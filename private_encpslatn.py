class Car:
    def __init__(self, brand):
        self.__brand = brand   # private attribute

    def show_brand(self):      # public method to access private data
        return self.__brand

mycar = Car("Tesla")
# print(mycar.__brand)   #  AttributeError
print(mycar.show_brand())   #  Tesla
