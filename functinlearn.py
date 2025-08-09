#function intro
'''
def fun(name):
    print("Hi", name)
fun("Hadi")
fun("Ameen")
fun("PK")
'''
#oddeven using function
'''
def oddeven():
    num=int(input("Enter a number: "))
    if num%2==0:
        print("Number is even")
    else:
        print("Number is odd")
oddeven()
'''
#addition with default value
'''
def Addition(x,y=6):
    print(x+y)
a=10
b=10
Addition(a)
'''
#factorial using python
'''
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of ", num, "is", fact)
num = int(input("Enter a number: "))
factorial(num)
'''
#prime or not

#functin with return
'''
def sum(a,b,c):
    return a-b-c
s=sum(10,2,3)
print("Sum is",s)
'''
#global and local
'''
def func():
    print(a)
a=20
func()
print(a)
'''
#factorial using function
'''
def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
num=int(input("Enter a number: "))
print(f"Factorial of {num} is {fact(num)}.")
'''
#string reverse using recursion
'''
def strrev(s):
    if len(s) <= 1:
        return s
    else:
        return strrev(s[1:]) + s[0]
print(strrev(input("Enter a string: ")))
'''
