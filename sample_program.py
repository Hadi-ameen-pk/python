class Student:
    def __init__(self,name,age,course):
        self.n=name
        self.a=age
        self.c=course
    def display(self):
        print("Name:",self.n,"\nAge:",self.a,"\nCourse:",self.c)
std=int(input("Enter the student count:"))
students=[]
for i in range(std):
    n=input("Enter name:")
    a=int(input("Enter age:"))
    c=input("Enter course:")
    students.append(Student(n,a,c))
for d in students:
    d.display()
    print("-----------------")