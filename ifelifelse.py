score = int(input("Enter your score: "))
if score >= 90:
    print("Distinction")
elif score >= 50:
    print("Passed")
else:
    print("Failed")

num=int(input("Enter a number: "))
if num > 0:
    print(num, "is positive")
elif num == 0:
    print(num, "is zero")
else:
    print(num, "is negative")