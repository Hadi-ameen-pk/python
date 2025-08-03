"""
a = int(input("Enter the first number:"))
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
"""
"""
for i in "python":
    print(i)

for j in {79,"python",8.98,28}:
    print(j)

for k in ["cherry",1.8,75]:
    print(k)

for l in ("fort",24,7.5):
    print(l)

for m in {"name":"Hadi","age":20}:
    print(m)
"""
'''
for i in range(5):
    print(i)
'''
'''
num = int(input("Enter a number: "))
j = int(input("Enter starting number: "))
k = int(input("Enter ending number: "))
for i in range(j, k + 1):
    if i%7==0:
        print(num,"*",i,"=",num*i)
'''
'''
for i in range(1,6):
    print("* "*i)
'''
'''
num = int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of ",num,"is",fact)
'''
'''
my_list=["apple","banana","Anar","orange"]
for item in my_list:
    if item[0]=="a" or item[-1]=="e":
        print(item)
'''
'''
my_list=["oneteam",8.2,"apple",38,"python",3.83,12]
print(my_list[-1:-8:-2])
'''

for r in range(5,0,-1):
    for s in range(r):
        print("*",end=" ")
    print()