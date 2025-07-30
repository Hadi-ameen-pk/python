"""a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
print("1=Addition\n2=Subtraction\n3=Multiplication\n4=Division")
choice=int(input("Enter your choice:"))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a*b)
elif choice==4:
    print(a/b)
else:
    print("Invalid choice")
"""

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
print("1=Addition\n2=Subtraction\n3=Multiplication\n4=Division")
choice=int(input("Enter your choice:"))
match choice:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case _:
        print("Invalid choice")


