'''name=input("Enter your name: ")
age=int(input("Enter your age: "))
print(name,age)
'''

num = int(input("Enter a number: "))
j = int(input("Enter starting number: "))
k = int(input("Enter ending number: "))

for i in range(j, k + 1):
    if i%7==0:
        print(num,"*",i,"=",num*i)
