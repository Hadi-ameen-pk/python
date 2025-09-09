#choice using if_elif_else
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
#choice using match
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
#datatypes
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
#forloop
'''
for i in range(5):
    print(i)
'''
#pattern
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
#factorial
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
#list
'''
my_list=["oneteam",8.2,"apple",38,"python",3.83,12]
print(my_list[-1:-8:-2])
'''
'''
for r in range(5,0,-1):
    for s in range(r):
        print("*",end=" ")
    print()
'''
#pattern printing
'''
rows=5
for i in range(1,rows+1):
    num=i
    k=rows-1
    for j in range(1,i+1):
        print(num,end=" ")
        num+=k
        k-=1
    print("")
'''
#print 1 to 5 usng while loop
''' 
num=1
while num<=5:
    print(num,end=" ")
    num+=1
'''
#multiplication table
'''
count=1
num=int(input("Enter a number: "))
while count<=10:
    print(count,"*",num,"=",count*num)
    count+=1
'''
#control statement in for loop
'''
for i in range(1,11):
    if i==5:
        break
    print(i,end=" ")
'''
#cntrol statement in while loop
'''
count=1
num=int(input("Enter a number: "))
while count<=10:
    if count==5:
        count+=1
        break
    print(count,"*",num,"=",count*num)
    count+=1
'''
'''
i=1
while i<=10:
    if i==5:
        i+=1
        continue
    print(i,end=" ")
    i+=1
'''
#while loop choice
'''
while True:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    choice=int(input("Enter your choice:"))
    if choice==1:
       print(num1+num2)
    elif choice==2:
       print(num1-num2)
    elif choice==3:
       print(num1*num2)
    elif choice==4:
        print(num1/num2)
    else:
        print("Invalid choice")
    con=input("Do you want to continue(y/n)?")
    if con.lower() != 'y':
        break
'''
#prime or not
'''
n=int(input("Enter a number:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(n," is not a prime number")
            break
    else:
         print(n," is prime number")
else:
    print(n,"is not a prime number")
'''
#cgpt static method
'''
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def check_even_odd(n):
        if n % 2 == 0:
            return f"{n} is Even"
        else:
            return f"{n} is Odd"
# Main program
result = MathOperations.add(4, 6)   # sum = 10
print("Sum:", result)
print(MathOperations.check_even_odd(result))
'''