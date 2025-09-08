from abc import ABC,abstractmethod
class Fruits(ABC):
    @abstractmethod
    def taste(self):
        pass
class Mango(Fruits):
    def taste(self):
        return "Sweet"
class Chilly(Fruits):
    def taste(self):
        return "Spicy"
mango = Mango()
chilly = Chilly()
print(mango.taste())
print(chilly.taste())