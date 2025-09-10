class Student:
    @staticmethod
    def Validate(mark):
        if mark>=50:
            return "Pass"
        else:
            return "Fail"

    def __init__(self,n,a,m):
        self.nam=n
        self.age=a
        self.mark=m

    def display(self):
        print(self.Validate(self.mark))

ob=Student("Ebin",27,67)
ob.display()