class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
person1 = Person("Alice", 30)
print(person1.name, person1.age)
employee1 = Employee("Bob", 25, "E101")
print(employee1.name, employee1.age, employee1.employee_id)
